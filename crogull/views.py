# coding: utf-8
def path(route, view, name=None, prefix=None):
    """
    :param route: route url, example: /api/v1/index/, /../../../
    :param view: view function
    :param name: name
    :param prefix: prefix
    :return:
    """
    def fix_route(rt):
        if not rt:
            return
        if rt[0] == '/':
            rt = rt[1:]
        if rt[-1] != '/':
            rt += '/'
        return rt
    route = fix_route(route)
    prefix = fix_route(prefix)
    if prefix:
        route = '/' + prefix + route
    else:
        route = '/' + route

    if not name:
        name = view.__name__.replace('.', '_')

    return route, view, name


class Views:
    def __init__(self):
        self.routed_paths = {}
        self.named_paths = {}

    def add_path(self, path_lst):
        for path in path_lst:
            route, view, name = path
            self.routed_paths[route] = view
            if name in self.named_paths:
                raise ValueError('path name conflict: %s' % name)
            self.named_paths[name] = view

    def routed_path_view(self, path):
        if path[-1] != '/':
            path += '/'
        return self.routed_paths.get(path)


views = Views()
