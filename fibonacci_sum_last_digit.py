# Uses python3
import sys
import math
import time
import multiprocessing
import os
from functools import lru_cache
import numpy as np


@lru_cache(maxsize=128)
def sum_fibonacci(n):
    total = 0
    if n <= 2:
        total = total + n
        return total
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        total += a
    return total


@lru_cache(maxsize=128)
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=128)
def calculate_fibonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def math_fib(n):
    Phi = (math.sqrt(5) + 1) / 2
    x = math.pow(Phi, n)
    factor = -1 * math.pow(-1, n)
    y = factor / x
    x += y
    return round(x / math.sqrt(5))


# Function that computes sum Fibonacci numbers with lru_cache
@lru_cache(maxsize=128)
def array_fibonacci(n):
    x = sum([calculate_fibonacci(i) for i in range(n + 1)])
    return x


fib_table = {0: 0, 1: 1, 2: 2}


# Function that computes Fibonacci numbers with lru_cache
@lru_cache(maxsize=128)
def dict_fibonacci(n):
    if n in fib_table:
        return fib_table[n]
    else:
        fib_table[n] = sum_array_fibonacci(n - 1) + sum_array_fibonacci(n - 2)
        return fib_table[n]


@lru_cache(maxsize=128)
def fib_dict(n):
    n = n + 2
    return dict_fibonacci(n) - 1


def fibonacci_sum_naive(p):
    if p <= 999999:
        y = fibonacci(p + 2) - 1
    else:
        y = math_fib(p + 2) - 1
    return int(str(y)[-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
