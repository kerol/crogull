# coding: utf-8
from inspect import isawaitable
from asyncio import Protocol

from .parser import HttpParser
from .request import Request
from .response import Response, ErrorResponse
from .views import views


class HttpProtocol(Protocol):

    def __init__(self, *, loop, keep_alive=True, keep_alive_timeout=5, **kwargs):
        self.loop = loop
        self.transport = None
        self.parser = HttpParser()
        self.keep_alive = keep_alive
        self.keep_alive_timeout = keep_alive_timeout
        self._keep_alive_timeout_handler = None

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        try:
            # self.request = Request(**self.parser.parse_request(data))
            self.request = Request()
        except Exception as e:
            print(e)

        # get response
        self._request_handler_task = self.loop.create_task(
            self.handle_request(self.request, self.write_response)
        )

    def eof_received(self):
        pass

    def connection_lost(self, exc):
        pass

    def keep_alive_timeout_callback(self):
        self.transport.close()
        self.transport = None

    async def handle_request(self, request, write_callback):
        try:
            # path = request.path
            path = '/api/hello/'
            func = views.routed_path_view(path)
            if func is None:
                resp = ErrorResponse(404)
            else:
                resp = func(request)
                if isawaitable(resp):
                    resp = await resp
                if not isinstance(resp, Response):
                    resp = Response(resp)
        except Exception as e:
            print(e)
            resp = ErrorResponse(500)
        write_callback(resp)

    def write_response(self, resp):
        if self._keep_alive_timeout_handler:
            self._keep_alive_timeout_handler.cancel()
            self._keep_alive_timeout_handler = None
        try:
            self.transport.write(resp.output(
                keep_alive=self.keep_alive, keep_alive_timeout=self.keep_alive_timeout))
        except Exception as e:
            print(e)
        finally:
            if not self.keep_alive:
                self.transport.close()
                self.transport = None
            else:
                self._keep_alive_timeout_handler = self.loop.call_later(
                    self.keep_alive_timeout,
                    self.keep_alive_timeout_callback
                )
                self._request_handler_task = None


class WebsocketProtocol:
    # todo
    def __init__(self):
        pass
