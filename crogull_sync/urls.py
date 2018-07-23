# coding: utf-8
def path(route, view, name=None, prefix=None):
    if prefix:
        route = '/' + prefix + route
    else:
        route = '/' + route

    if not name:
        name = view.__name__.replace('.', '_')

    return route, view, name

