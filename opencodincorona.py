import sys
from functools import lru_cache

''' Input Format
The first line of the input consists of the virus composition, V
The second line of he input consists of the number of people, N
Next N lines each consist of the blood composition of the ith person, Bi
'''

lru_cache(maxsize=None)
def test(T, P):
    found = {}
    result = "NEGATIVE"
    # length of strings.
    n = len(T)
    # length of pattern
    m = len(P)
    # length of element matched in P
    q = 0
    counter = 0
    while counter < n and q < m:
        if found.get(T[counter]) is not None:
            counter += 1
            n = len(T)
            return
        if T[counter] == P[q]:
            q += 1
            if q == m:
                result = "POSITIVE"
                break
        else:
            found[counter] = 0
        counter += 1
    print(result)


def main():
    T = str(input())
    N = int(input())
    for i in range(N):
        P = str(input())
        test(T, P)

main()
