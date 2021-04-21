# Uses python3
import sys

def calculate_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibonacci_sum_naive(p):
    x = calculate_fibonacci(p)
    return int(str(x[0])[-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
