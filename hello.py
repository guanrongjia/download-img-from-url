#encoding=utf-8
from tools import check_url, filterImageUrls, downloadImages
import urllib
import json

def application(environ, start_response):
    request_path = environ.get('PATH_INFO')
    print request_path
    result = ''
    # here is the way to get html
    if request_path in [r'/', r'/home']:
        # 响应
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open('./homepage.html', 'rb') as f:
            result = f.read()
        return [result]

    # here is the way to download static files such as .css, .js etc
    elif request_path.startswith(r'/lib'):
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open('.' + request_path, 'rb') as f:
            result = f.read()
        return [result]

    # here is the way to download files from server
    elif request_path == r'/download-img-zip':
        start_response('200 OK', [('Content-Type', 'application/zip, application/octet-stream'),
                                  ('Content-Disposition', 'attachment;filename=file.zip')])

        try:
            with open('./server.zip', 'rb') as f:
                result = f.read()
        except Exception:
            result = ['ERROR']

        return result

    # here is the interface to download images form souce url
    elif request_path == r'/download-img':
        start_response('200 OK', [('Content-Type', 'text/html')])
        query_string = environ.get('QUERY_STRING')
        query_arg_list = query_string.split('&')
        query_arg_dict = dict([(kvstring.split('=')[0], kvstring.split('=')[1]) for kvstring in query_arg_list])
        source_url = query_arg_dict.get('source_url')
        source_url = urllib.unquote(source_url)
        if check_url(source_url):
            dirname, img_objs = filterImageUrls(source_url)
            result_str = downloadImages(dirname, img_objs)
            result_json = {
                'retcode' : 'SUCC',
                'describe': result_str,
                'dirname' : dirname,
            }
            return [json.dumps(result_json)]
        else:
            result_json = {
                'retcode': 'ERROR',
                'describe': 'source_url is invalided',
            }
            return [json.dumps(result_json)]
    else:
        return ['arguments is not correct!']