# coding: utf-8
default_settings = {
    'DEBUG': False,
    'PORT': 8120,
    'TIME_ZONE': 'Asia/Shanghai',
}

class DefaultSettings:
    def __init__(self):
        for k, v in default_settings.items():
            self.__dict__[k] = v


settings = DefaultSettings()
