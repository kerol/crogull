# coding: utf-8
from http.client import responses


class HttpResponse:
    """
    Http Response
    """
    def __init__(self, content, status=None, content_type=None):
        self.content = content
        self.status_code = status or 200
        self.status_phrase = responses.get(self.status_code, 'UNKNOWN_STATUS_CODE')
        self.headers = {
            'Content-type': content_type or 'text/plain',
            'Cookie': 'password',
        }
