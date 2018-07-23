# coding: utf-8
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
        return self.routed_paths.get(path)


views = Views()
