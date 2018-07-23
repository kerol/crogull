# coding: utf-8
class HttpRequest:
    """
    Http Request
    """
    def __init__(self, environ):
        self.environ = environ

    @property
    def method(self):
        return self.environ['REQUEST_METHOD']

    @property
    def args(self):
        _args = {}
        if self.environ['QUERY_STRING']:
            for item in self.environ['QUERY_STRING'].split('&'):
                k, v = item.split('=')
                _args[k] = v

        return _args

    @property
    def headers(self):
        _headers = {}
        for k, v in self.environ.items():
            if k[:4] == 'HTTP':
                _headers[k[5:].lower().replace('_', '-')] = v
        if self.environ.get('CONTENT_TYPE'):
            if self.environ['CONTENT_TYPE'][:19] == 'multipart/form-data':
                _headers['content-type'] = 'multipart/form-data'
            else:
                _headers['content-type'] = self.environ['CONTENT_TYPE']

        return _headers

    @property
    def data(self):
       return self.environ['wsgi.input'].read().decode()

    @property
    def form(self):
        _form = {}
        if self.environ.get('CONTENT_TYPE'):
            if self.environ['CONTENT_TYPE'][:19] == 'multipart/form-data':
                boundary = '--' + self.environ['CONTENT_TYPE'].split('=')[-1]
                data = self.data
                if data:
                    for item in data.split(boundary)[1:-1]:
                        kv_list = item.split('=')[-1].split('\r\n')
                        k, v = kv_list[0][1:-1], kv_list[2]
                        _form[k] = v

        return _form

    @property
    def path(self):
        _path = self.environ['PATH_INFO']
        return _path if _path[-1] == '/' else _path + '/'
