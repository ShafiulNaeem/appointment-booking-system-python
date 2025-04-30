from io import BytesIO
from werkzeug.formparser import parse_form_data
from werkzeug.wrappers import Request


class RequestWrapper:
    @staticmethod
    def parse_request(headers, body_bytes):
        environ = {
        'REQUEST_METHOD': 'POST',
        'CONTENT_TYPE': headers['Content-Type'],
        'CONTENT_LENGTH': headers['Content-Length'],
        'wsgi.input': BytesIO(body_bytes)
        }
        _,form, files = parse_form_data(environ)
        for key in files.keys():
            form[key] = files[key]
        return form