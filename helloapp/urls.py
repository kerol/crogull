# coding: utf-8
from crogull.views import path

from . import views

urlpatterns = [
    path('hello', views.index, name='demo_hello', prefix='api')
]