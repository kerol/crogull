# coding: utf-8
from signal import SIGINT, SIGTERM
from functools import partial
import asyncio
import uvloop

from .protocol import HttpProtocol
from .settings import settings

#asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def run():
    loop = asyncio.get_event_loop()
    host, port = '127.0.0.1', settings.PORT
    protocol_factory = partial(HttpProtocol, loop=loop)
    server_coroutine = loop.create_server(protocol_factory, host=host, port=port)
    http_server = loop.run_until_complete(server_coroutine)
    print('start server ok')
    print('running at:', 'http://%s:%s' % (host, port))

    # register stop signal
    _signals = (SIGINT, SIGTERM)
    for _signal in _signals:
        loop.add_signal_handler(_signal, loop.stop)

    try:
        loop.run_forever()
    finally:
        http_server.close()
        loop.run_until_complete(http_server.wait_closed())

        loop.close()
        print('close loop ok')
