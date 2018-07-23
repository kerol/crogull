# coding: utf-8
from crogull_sync.signals import request_started, request_finished, got_request_exception


@request_started.connect
def request_started_receiver(sender, **kwargs):
    print('request startd signal from: %r' % sender)
    print('kwargs: %r' % kwargs)
    request = kwargs['request']
    print('method:\n', request.method)
    print('path:\n', request.path)
    print('args:\n', request.args)
    print('form:\n', request.form)
    print('data:\n', request.data)
    print('headers:\n', request.headers)


@request_finished.connect
def request_finished_receiver(sender, **kwargs):
    print('request finished signal from: %r' % sender)
    print('kwargs: %r' % kwargs)
    response = kwargs['response']


@got_request_exception.connect
def got_request_exception_receiver(sender, **kwargs):
    print('got requeset exception from: %r' % sender)
    print(kwargs['exception'])
