# coding: utf-8
from crogull_sync.urls import path

from demoapp import views
from demoapp import receivers

urlpatterns = [
    path('foo/', views.index, name='demo_hello', prefix='api/')
]
