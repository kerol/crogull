# coding: utf-8
from crogull.parser import HttpParser
from tests import constants as const

parser = HttpParser()

parser.parse_request(const.HTTP_GET)
parser.parse_request(const.HTTP_FORM_POST)
print(parser.method)
print(parser.path)
print(parser.params)
print(parser.protocol)
print(parser.protocol_version)
print(parser.headers)
