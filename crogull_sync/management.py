# coding: utf-8
from wsgiref.simple_server import make_server

from crogull_sync.settings import settings


def run_from_command(sys_args):
    from crogull_sync.app import wsgi_app
    args = sys_args[1:]
    port = settings.PORT
    with make_server('', port, wsgi_app().__call__) as httpd:
        print("Serving on port {}...".format(port))
        httpd.serve_forever()
