# coding: utf-8
import crogull_rust

print(crogull_rust.sum_as_string(1, 4))
assert crogull_rust.sum_as_string(1, 4) == '5'
print(crogull_rust.parser_header('aa'))
assert crogull_rust.parser_header('aa') != None
