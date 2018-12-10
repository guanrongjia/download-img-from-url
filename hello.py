#encoding=utf-8
from scripy_img import
def application(environ, start_response):
    print(environ)
    if environ.PATH_INFO == r'/':
        status = '200 OK'  # HTTP Status
        headers = [('Content-type', 'text/plain')]  # HTTP Headers
        start_response(status, headers)

        return "Hello World"

    start_response('200 OK', [('Content-Type', 'application/zip, application/octet-stream'),
                              ('Content-Disposition', 'attachment;filename=file.zip')])
    # return ["Hello World".encode("utf-8")]
    result = ''
    try:
        with open('./server.zip', 'rb') as f:
            result = f.read()
    except Exception:
        result = ['ERROR']

    return result