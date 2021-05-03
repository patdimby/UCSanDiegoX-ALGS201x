import sys

''' Input Format
The first line of input consists of the number of test cases, T
Next T lines each consists of two space-separated integers, L and R
'''


def main():
    T = int(input())
    result = ""
    for k in range(T):
        a = input()
        b = a.replace('\n', ' ')
        c = b.split()
        L, R = int(c[0]), int(c[1])
        if T < 1 or T > 10:
            print("-1")
            return
        if L < 2 or R < 2:
            print("-1")
            return
        if L > 10**6 or R > 10**6:
            print("-1")
            return
        L, R = L - 1, R + 1
        if L < 2 or R < 2:
            print("-1")
            return
        if R < L:
            print("-1")
            return
        if L == R:
            print("0")
            return
        numbers = [num for num in range(L, R)]
        arr = [i for i in numbers for r in range(L) if r % i > 0]
        if len(arr) < 1:
            print("-1")
            return
        print(max(arr) - min(arr))


main()
