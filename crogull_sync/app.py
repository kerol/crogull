# coding: utf-8
import importlib

from crogull_sync.http import HttpRequest, HttpHandler
from crogull_sync.settings import settings
from crogull_sync.views import views
from crogull_sync.signals import request_started, request_finished, got_request_exception


def wsgi_app():
    croture.init()
    return WSGIHandler()


class WSGIHandler(HttpHandler):
    """
    PEP 3333 & 0333: Python Web Server Gateway Interface Handler
    """
    def __init__(self, *args, **kwargs):
        super(HttpHandler, self).__init__(*args, **kwargs)

    def __call__(self, environ, start_response):

        response = None
        try:
            request = HttpRequest(environ)
            request_started.send(self, request=request)

            response = self.get_response(request)
            request_finished.send(self, response=response)
        except Exception as e:
            got_request_exception.send(self, exception=e)

        if not response:
            raise ValueError('response none')

        wsgi_status = str(response.status_code) + ' ' + response.status_phrase
        wsgi_headers = list(response.headers.items())
        wsgi_content = [response.content.encode()]

        start_response(wsgi_status, wsgi_headers)

        return wsgi_content


class Croture:
    """
    Croture App
    """
    def __init__(self):
        pass

    def init(self):
        """
        Because you may modify settings before app created, so you should init your app manually.
        :return:
        """
        if hasattr(settings, 'INSTALLED_APPS'):
            self.register_urls()

    def register_urls(self):
        for app_name in settings.INSTALLED_APPS:
            urls = importlib.import_module(app_name + '.urls')
            views.add_path(urls.urlpatterns)

    def config(self, config_dct):
        if not isinstance(config_dct, dict):
            raise ValueError('dict configuration required')
        for k, v in config_dct.items():
            settings.__dict__[k.upper()] = v


croture = Croture()
