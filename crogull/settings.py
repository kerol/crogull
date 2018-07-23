# coding: utf-8
import os
import importlib


default_settings = {
    'DEBUG': False,
    'PORT': 8000,
    'TIME_ZONE': 'Asia/Shanghai',
}

class Settings:
    def __init__(self):
        for k, v in default_settings.items():
            self.__dict__[k] = v
        extra_env = os.environ.get('CROGULL_SETTINGS_MODULE')
        if extra_env is not None:
            extra_settings = importlib.import_module(extra_env)
            for attr in dir(extra_settings):
                if not attr.isupper():
                    continue
                self.__dict__[attr] = getattr(extra_settings, attr)


settings = Settings()
