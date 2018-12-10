#encoding=utf-8
from tools import check_url, filterImageUrls, downloadImages


def application(environ, start_response):
    request_path = environ.get('PATH_INFO')
    if environ['REQUEST_METHOD'] == 'GET' and request_path in [r'/', r'/home']:
        # 响应
        start_response('200 OK', [('Content-Type', 'text/html')])
        file_content = 'empty'
        with open('./homepage.html', 'rb') as f:
            file_content = f.read()
            print(file_content)
        return [file_content]


    elif request_path == r'/download-img':
        start_response('200 OK', [('Content-Type', 'application/zip, application/octet-stream'),
                                  ('Content-Disposition', 'attachment;filename=file.zip')])

        return "12123";

        try:
            with open('./server.zip', 'rb') as f:
                result = f.read()
        except Exception:
            result = ['ERROR']

        return result