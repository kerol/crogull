# coding: utf-8
class Request:

    __slots__ = ('method', 'path', 'args', 'protocol', 'protocol_version', 'headers')

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
