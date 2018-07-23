# coding: utf-8
from .parserlib import BaseHttpParser


def expect_char_check(itr, ch):
    assert next(itr) == ch


def expect_char(itr, ch, end):
    ret, ended = '', False
    for _ch in itr:
        if _ch == end:
            ended = True
            break
        if _ch == ch:
            break
        ret += _ch
    return ret, ended


class HttpParser(BaseHttpParser):

    def parse_request(self, data):
        """
        :param data: bytes
        :return:
        """
        args = {}
        headers = {}

        itr = iter(data.decode())
        method, ended = expect_char(itr, ' ', ' ')
        path, ended = expect_char(itr, '?', ' ')
        if not ended:
            while True:
                k, ended = expect_char(itr, '=', ' ')
                if ended:
                    break
                v, ended = expect_char(itr, '&', ' ')
                if ended:
                    args[k] = v
                    break
                args[k] = v
        protocol, ended = expect_char(itr, '/', '\r')
        protocol_version, ended = expect_char(itr, '\r', '\r')
        expect_char_check(itr, '\n')
        # headers
        while True:
            ch = next(itr)
            if ch == '\r':
                expect_char_check(itr, '\n')
                break
            k, ended = expect_char(itr, ':', '\r')
            if ended:
                expect_char_check(itr, '\n')
                continue
            k = ch + k
            expect_char_check(itr, ' ')
            v, ended = expect_char(itr, '\r', '\r')
            headers[k] = v
            expect_char_check(itr, '\n')

        return {
            'method': method,
            'path': path,
            'args': args,
            'protocol': protocol,
            'protocol_version': protocol_version,
            'headers': headers,
        }

