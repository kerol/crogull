# coding: utf-8
from blinker import Namespace


_signals = Namespace().signal

request_started = _signals('request_started')
request_finished = _signals('request_finished')
got_request_exception = _signals('got_request_exception')
template_rendered = _signals('template_rendered')
before_render_template = _signals('before_render_template')

