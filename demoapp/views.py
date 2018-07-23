# coding: utf-8
from crogull_sync.http import HttpResponse
from crogull_sync.templates import render_template


def index(request):
    data = {
        'title': 'demo index ',
        'foo': 'bar',
    }
    return render_template('demo/index.html', request, data=data)
