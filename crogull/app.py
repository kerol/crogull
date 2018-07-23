# coding: utf-8
import importlib

from .settings import settings
from .views import views
from .server import run as _run


class Crogull:

    def __init__(self):
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

    def run(self):
        _run()


app = Crogull()
