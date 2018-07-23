# coding: utf-8
import ujson as json
from functools import wraps, partial
from crogull_sync.http import HttpResponse


def render_json(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        ret = func(request, *args, **kwargs)
        if isinstance(ret, HttpResponse):
            ret.mimetype = 'application/json'
            return ret
        else:
            return HttpResponse(json.dumps(ret), content_type='application/json')

    return wrapper
