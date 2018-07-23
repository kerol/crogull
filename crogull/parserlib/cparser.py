# coding: utf-8
import os
from cffi import FFI

from .baseparser import BaseHttpParser

ffi = FFI()
lib = ffi.dlopen(os.path.abspath(os.path.join(os.path.dirname(__file__), './crogull_c.so')))

ffi.cdef("""
    struct phr_header {
        const char *name;
        size_t name_len;
        const char *value;
        size_t value_len;
    };

    int phr_parse_request(const char *buf, size_t len, const char **method,
                          size_t *method_len, const char **path,
                          size_t *path_len, int *minor_version,
                          struct phr_header *headers, size_t *num_headers,
                          size_t last_len);
""")


class CHttpParser(BaseHttpParser):

    def __init__(self):
        self.c_method = ffi.new('char **')
        self.method_len = ffi.new('size_t *')
        self.c_path = ffi.new('char **')
        self.path_len = ffi.new('size_t *')
        self.minor_version = ffi.new('int *')
        self.c_headers = ffi.new('struct phr_header[10]')
        self.num_headers = ffi.new('size_t *')
        self.chunked_offset = ffi.new('size_t*')

    def parse_request(self, buffer):
        result = lib.phr_parse_request(buffer, len(buffer), self.c_method, self.method_len, self.c_path, self.path_len,
                                       self.minor_version, self.c_headers, self.num_headers, 0)
        print(result)
        print(self.c_method)
        method = ffi.cast('char[{}]'.format(self.method_len[0]), self.c_method[0])
        method = ffi.buffer(method)[:]
        print(method)
