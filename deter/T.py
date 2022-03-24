from math import factorial, comb
from functools import lru_cache

@lru_cache(None)
def T(n):
    k = n // 2
    def pf(f):
        num = factorial(n - f - 1)
        den = n * factorial(n - 2)
        return num / den

    if n == 2: return 1
    return k + sum(pf(f) * T(n - 1 - f) for f in range(k))
                    

@lru_cache(None)
def ET(n):
    return T(n)
    if n == 1: return 0
    if n == 2: return 1
    pk = 1 / (n - 1)
    return sum(pk * T(n, k) for k in range(1, n))

if __name__ == '__main__':
    n = int(input('N: '))
    for i in range(n+1):
        print(i, T(i), comb(i, 2) / 3)
    # print(ET(n))
