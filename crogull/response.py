# coding: utf-8
from http import HTTPStatus
import ujson as json


class Response:

    def __init__(self, body, status=200, headers=None, content_type='text/plain'):
        self.body = body if type(body) is bytes else body.encode()
        self.status = status
        self.headers = headers or {}
        self.content_type = content_type

    def output(self, keep_alive=False, keep_alive_timeout=None):
        timeout_header = b''
        if keep_alive and keep_alive_timeout is not None:
            timeout_header = b'Keep-Alive: %d\r\n' % keep_alive_timeout
        self.headers['Content-Type'] = self.content_type if self.content_type else 'text/plain'
        headers = b''
        for k, v in self.headers.items():
            headers += (b'%b: %b\r\n' % (k.encode(), v.encode('utf-8')))

        return (b'HTTP/1.1 %d %b\r\n'
                b'Connection: %b\r\n'
                b'%b'
                b'%b\r\n'
                b'%b') % (
                   self.status, HTTPStatus(self.status).phrase.encode(),
                   b'keep-alive' if keep_alive else b'close',
                   timeout_header,
                   headers,
                   self.body,
               )


class ErrorResponse(Response):

    def __init__(self, status):
        self.status = status
        self.body = HTTPStatus(self.status).phrase.encode()
        self.headers = {}
        self.content_type = 'text/plain'


class JsonResponse(Response):

    def __init__(self, body, status=200, headers=None):
        self.body = json.dumps(body).encode()
        self.status = status
        self.headers = headers or {}
        self.content_type = 'application/json'
