# coding: utf-8
from crogull.parserlib import CHttpParser
from . import constants as const


parser = CHttpParser()
parser.parse_request(const.HTTP_GET)
