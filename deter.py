from math import factorial, e, floor, comb
from functools import lru_cache
from collections import defaultdict

def D(N):
    return floor((factorial(N) + 1) / e)


@lru_cache(None)
def T(N):
    if N == 2: return 1
    K = N // 2
    pf = precompute(N, K)

    # def pf(f):
    #     return ((comb(K, f)) * D(N - 1 - f)) / D(N)

    ans = K
    for f in range(K):
        ans += pf[f] * T(N - 1 - f)

    return ans

def derangements(N):
    A = list(range(N))

    def go(i):
        if i == N:
            yield A.copy()
        else:
            for j in range(i, N):
                if A[j] != i:
                    A[i], A[j] = A[j], A[i]
                    yield from go(i+1)
                    A[i], A[j] = A[j], A[i]

    yield from go(0)

@lru_cache(None)
def pf(N, k, f):
    count = 0
    for a in derangements(N):
        cf = 0
        for i in range(k):
            if a[i] == i + 1:
                cf += 1

        if cf == f:
            count += 1
            # print(a)

    return count / D(N)

def precompute(N, k):
    pf = defaultdict(int)
    for a in derangements(N):
        cf = 0
        for i in range(k):
            if a[i] == i + 1:
                cf += 1

        pf[cf] += 1

    for k in pf:
        pf[k] /= D(N)

    return pf

def mypf(N, k, f):
    choose = D(N - f)
    total = D(N)
    return choose / total
    return (choose * rest) / total

if __name__ == '__main__':
    N = int(input('N: '))
    k = N // 2
    f = 2

    print('N: {} k: {} f: {}'.format(N, k ,f))
    print('actual pf: {}'.format(pf(N, k, f)))
    print('expected pf: {}'.format(mypf(N, k, f)))
    # print(T(N))
