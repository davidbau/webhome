# Inspired by:
# https://github.com/geopython/demo.pywps.org/blob/master/PyWPS/webhook-deploy.wsgi

import hashlib
import hmac
import json
import os
import subprocess
import datetime
import shutil

BASEDIR = '/srv/baulab/www'
SECRETS = [b'LeCun'] # Rotate this secret for each semester

def process_request(request, sitename='expo', event=None):
    if not any(e == 'push' for e in request.get('events', []) + [event]):
        return f'Ignored event {str(request["events"])}.'
    owner_name = request['repository']['owner']['name']
    repo_name = request['repository']['name']
    if '..' in repo_name or '..' in owner_name:
        return f'Ignored bad repo name.'
    visibility = request['repository']['visibility']
    if visibility != 'public':
        return f'Ignored push of nonpublic repository.'
    default_branch = request['repository']['default_branch']
    clone_url = request['repository']['clone_url']
    datedir = date_dir()
    website_dir = f'{BASEDIR}/{sitename}/{datedir}/{owner_name}/{repo_name}'
    try:
        os.chdir(website_dir)
        subprocess.check_call(['git', 'fetch', '--depth=1'])
        subprocess.check_call(['git', 'reset', '--hard', '@{u}'])
    except:
        shutil.rmtree(website_dir, ignore_errors=True)
        os.makedirs(website_dir, exist_ok=True)
        os.chdir(website_dir)
        subprocess.call(['git', 'clone', '--depth=1', clone_url, '.'])

def application(environ, start_response):
    """WSGI application to update expo.baulab.info/2022-Fall/username/repo"""

    error = 0
    response = {
        'status': '400 Bad Request',
        'message': 'Could not update repository'
    }

    # read the request
    length = int(environ.get('CONTENT_LENGTH', '0'))
    signature = environ.get('HTTP_X_HUB_SIGNATURE_256', None)
    event = environ.get('HTTP_X_GITHUB_EVENT', None)
    sitename = environ.get('HTTP_HOST', 'expo').split('.')[0]
    payload = environ['wsgi.input'].read(length)

    # parse the payload and check the signature
    request = None
    secured = False
    message = 'Did nothing.'
    try:
        request = json.loads(payload)
        secured = any(is_valid_signature(s, signature, payload) for s in SECRETS)
    except ValueError as e:
        error = 1
        request = {'error': str(e), 'payload': repr(payload) }
        import traceback
        message = traceback.format_exc()

    # log the request
    with open(f'{BASEDIR}/pushlog/log.txt', 'a') as f:
        f.write(json.dumps(request, indent=1) + '\n')


    if secured and not error:
        try:
            message = process_request(request, sitename=sitename, event=event)
        except Exception as e:
            error = 1
            message = str(e)

    if error:
        response = {
            'status': '500 Script error.',
            'message': f'Could not process webhook {message}.'
        }
    elif not secured:
        response = {
            'status': '403 Forbidden',
            'message': 'Webhook secret is wrong.'
        }
    else:
        response = {
            'status': '200 OK',
            'secured': f'{secured}',
            'message': message
        }

    output = json.dumps(response).encode('utf-8')

    response_headers = [('Content-type', 'application/json'),
                        ('Content-Length', str(len(output)))]
    start_response(response['status'], response_headers)
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

