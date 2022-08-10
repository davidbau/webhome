import os, sys

def application(environ, start_response):
    status = '200 OK'
    e = []
    e.extend([f'{k}: {v}' for k, v in environ.items()])
    e.extend(['os.environ:'] + [f'{k}: {v}' for k, v in os.environ.items()])
    e.extend(['\nsys:'] + [f'sys.{k}: {getattr(sys, k)}' for k in ['path', 'argv', 'abiflags', 'base_prefix', 'base_exec_prefix', 'byteorder', 'exec_prefix', 'executable', 'flags', 'platform', 'prefix', 'thread_info', 'version']])
    output = b'Hello World!\n\n' + '\n'.join(e).encode('utf-8')
    response_headers = [('Content-type', 'text/plain'),
                  ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
