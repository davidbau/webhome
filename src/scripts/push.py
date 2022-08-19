# WSGI application to automaticallly deploy expo.baulab.info/2022-Fall/username
# inspired by:
# https://github.com/geopython/demo.pywps.org/blob/master/PyWPS/webhook-deploy.wsgi

import hashlib
import hmac
import json
import os
from subprocess import check_call, check_output
import datetime
import shutil
import urllib.parse

BASEDIR = '/srv/baulab/www'
BASESITE = 'baulab.info'
SECRETS = [b'LeCun'] # Rotate this secret for each semester
SITES = ['expo'] # Sites where this is allowed

def process_request(request, sitename='expo', event=None):
    if sitename not in SITES:
        return f'Ignored push to {sitename}.'
    events = request.get('events', []) + [event]
    if not any(e == 'push' for e in events):
        return f'Ignored event {events}.'
    owner_name = request['repository']['owner']['login']
    repo_name = request['repository']['name']
    if '..' in repo_name or '..' in owner_name:
        return f'Ignored bad repo name.'
    visibility = request['repository']['visibility']
    if visibility != 'public':
        return f'Ignored push of nonpublic repository.'
    default_branch = request['repository']['default_branch']
    clone_url = request['repository']['clone_url'].strip()
    datedir = date_dir()
    # With this template, each github user only gets one website per semester.
    subdir = f'{datedir}/{owner_name}'
    website_dir = f'{BASEDIR}/{sitename}/{subdir}'
    website_url = f'https://{sitename}.{BASESITE}/{subdir}'
    try:
        # If the website exists and is the right repository, update it.
        if not os.path.isfile(f'{website_dir}/.git/HEAD'):
            raise RuntimeError('New repo')
        os.chdir(website_dir)
        repo_url = check_output(['git', 'remote', 'get-url', 'origin']).decode('utf-8').strip()
        if clone_url != repo_url:
            raise RuntimeError(f'Repo url changed {repo_url} to {clone_url}')
        repo_branch = check_output(['git', 'branch', '--show-current']).decode('utf-8').strip()
        if default_branch != repo_branch:
            raise RuntimeError(f'Branch changed {repo_branch} to {default_branch}')
        check_call(['git', 'fetch', '--depth=1'])
        check_call(['git', 'reset', '--hard', '@{u}'])
        return f'Fetched {default_branch} of {clone_url} to {website_url}.'
    except Exception as e:
        # If there is some other problem, clean and recreate the website.
        shutil.rmtree(website_dir, ignore_errors=True)
        os.makedirs(website_dir, exist_ok=True)
        os.chdir(website_dir)
        check_call(['git', 'clone', '--depth=1', clone_url, '.'])
        return f'Cloned {default_branch} of {clone_url} to {website_url}. {e}.'

def application(environ, start_response):
    """WSGI application to update expo.baulab.info/2022-Fall/username"""

    # parse the payload and check the signature
    error = 0
    request = None
    secured = False
    message = 'Did nothing.'
    status = '400 Bad request'
    stamp = datetime.datetime.now().isoformat()
    try:
        # read the request
        length = int(environ.get('CONTENT_LENGTH', '0'))
        signature = environ.get('HTTP_X_HUB_SIGNATURE_256', None)
        event = environ.get('HTTP_X_GITHUB_EVENT', None)
        sitename = environ.get('HTTP_HOST', 'expo').split('.')[0]
        ctype = environ.get('CONTENT_TYPE', 'application/json')
        payload = environ['wsgi.input'].read(length)
        # unwrap form-urlencoded payload
        if ctype == 'application/x-www-form-urlencoded':
            request = json.loads(urllib.parse.parse_qs(payload)[b'payload'][0])
        else:
            request = json.loads(payload)
        # check the signature
        secured = any(is_valid_signature(s, signature, payload) for s in SECRETS)
        if not secured:
            message = 'Webhook secret is wrong.'
            status = '403 Forbidden'
        else:
            # process the action
            message = process_request(request, sitename=sitename, event=event)
            status = '200 OK'
    except Exception as e:
        error = 1
        import traceback
        message = repr(traceback.format_exc())
        with open(f'{BASEDIR}/pushlog/errors.txt', 'a') as f:
            f.write(f'{stamp} ERROR {message} PAYLOAD {repr(payload)}\n')
            for k, v in environ.items():
                f.write(f'{stamp} {k} {v}\n')

    # log the action
    with open(f'{BASEDIR}/pushlog/log.txt', 'a') as f:
        f.write(f'{stamp} {message}\n')

    # send the response
    response = {'status': status, 'message': message}
    output = json.dumps(response).encode('utf-8')
    start_response(response['status'], [
        ('Content-type', 'application/json'),
        ('Content-Length', str(len(output)))])
    return [output]

def is_valid_signature(secret, signature, payload):
    """Validate a GitHub webhook signature"""
    if signature is None or '=' not in signature:
        return False
    sha_name, signature = signature.split('=')
    if sha_name not in ['sha1', 'sha256']:
        return False
    is_valid = False
    mac = hmac.new(secret, msg=payload, digestmod=getattr(hashlib, sha_name))
    try:
        is_valid = hmac.compare_digest(str(mac.hexdigest()), signature)
    except AttributeError:
        is_valid = str(mac.hexdigest()) == str(signature)
    return is_valid

def date_dir():
    today = datetime.date.today()
    semester = "Fall" if today.month >= 9 else "Spring" if today.month <= 4 else "Summer"
    return f'{today.year}-{semester}'

