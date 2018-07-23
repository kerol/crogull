# coding: utf-8
import time
from crogull_rust import sum_as_string as sum_as_string_rs

num = 1000000

t0 = time.time()
for item in range(num):
    sum_as_string_rs(1, 2)
print(time.time() - t0)


def sum_as_string_py(a, b):
    return str(a + b)

t1 = time.time()
for item in range(num):
    sum_as_string_py(1, 2)
print(time.time() - t1)
