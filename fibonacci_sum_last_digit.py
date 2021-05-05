import sys
import time
import multiprocessing
from decimal import *
import os
import math
from functools import lru_cache
import numpy as np


@lru_cache(None)
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


@lru_cache(None)
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def np_fib(n):
    matrice = np.array([[1, 1], [1, 0]])
    x = np.linalg.matrix_power(matrice, n)
    y = np.array([1, 0])
    return x * y


def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


@lru_cache(None)
def calculate_fibonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# Function that computes sum Fibonacci numbers with lru_cache
@lru_cache(None)
def array_fibonacci(n):
    x = sum([calculate_fibonacci(i) for i in range(n + 1)])
    return x


fib_table = {0: 0, 1: 1, 2: 2}


# Function that computes Fibonacci numbers with lru_cache
@lru_cache(None)
def dict_fibonacci(n):
    if n in fib_table:
        return fib_table[n]
    else:
        fib_table[n] = dict_fibonacci(n - 1) + dict_fibonacci(n - 2)
        return fib_table[n]


@lru_cache(maxsize=128)
def math_fib(n):
    if n <= 2:
        if n == 0:
            return 0
        return 1
    phi = (1 + math.sqrt(5)) / 2
    return int(round(pow(phi, n) / math.sqrt(5)))


@lru_cache(maxsize=128)
def fib_dict(n):
    n = n + 2
    return dict_fibonacci(n) - 1


@lru_cache(maxsize=128)
def fibonacci_sum_naive(p):
    if p == 0:
        return 0
    if p <= 2:
        return p
    y = np_fib(p + 2)[0][0] - 1
    return int(str(y)[-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
