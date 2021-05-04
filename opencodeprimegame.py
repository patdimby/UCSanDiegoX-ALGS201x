import sys
from functools import lru_cache

''' Input Format
The first line of input consists of the number of test cases, T
Next T lines each consists of two space-separated integers, L and R
'''

lru_cache(maxsize=None)
def setArrayPrime(L, R):
    primes = []
    for possiblePrime in range(2, R + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            if possiblePrime >= L:
                primes.append(possiblePrime)
    return(primes)


def clean():
    str1 = str(input())
    a = str1.split(' ')
    x = int(a[0].strip())
    y = int(a[1].strip())
    return x, y


def main():
    T = int(input())
    result = ""
    for k in range(T):
        L, R = clean()
        if T < 1 or T > 10:
            print(-1)
        else:
            if (L < 2 or R < 2) or (L > 10**6 or R > 10**6):
                print(-1)
            else:
                arr = setArrayPrime(L, R)
                if len(arr) < 1:
                    print(-1)
                else:
                    if len(arr) == 1:
                        print(0)
                    else:
                        print(max(arr) - min(arr))


main()
