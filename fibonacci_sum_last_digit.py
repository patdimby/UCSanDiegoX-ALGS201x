# Uses python3
import sys

def calculate_fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = calculate_fibonacci(n // 2)
        print(a,b)
        c, d = a * (b * 2 - a), a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

def fibonacci_sum_naive(p):
    x = calculate_fibonacci(p)
    return int(str(x[0])[-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
