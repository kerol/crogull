# coding: utf-8
from crogull_sync.http import HttpResponse
from crogull_sync.views import views


class HttpHandler:
    def __init__(self):
        self.response = None

    def get_response(self, request):
        path = request.path
        view_func = views.routed_path_view(path)
        if not view_func:
            return HttpResponse('', status=400)
        response = view_func(request)  # HttpResponse Object
        if not response:
            raise ValueError('view func no return')

        return response
