from math import floor, factorial, e
import threading
from concurrent.futures import ThreadPoolExecutor

def count_derangements(N):
    return floor((factorial(N) + 1) / e)

def derangements(N):
    # ans = []
    A = list(range(N))

    def go(i):
        if i == N:
            yield A.copy()
            # ans.append(A.copy())
        else:
            for j in range(i, N):
                if A[j] != i:
                    A[i], A[j] = A[j], A[i]
                    yield from go(i+1)
                    A[i], A[j] = A[j], A[i]
                    pass

    # go(0)
    # assert len(ans) == count_derangements(N)
    yield from go(0)

def valid(A, k):
    indices = [A.index(i) for i in range(k)]
    return indices == sorted(indices)

if __name__ == '__main__':
    N = int(input('N: '))
    k = int(input('k: '))

    count = 0
    for A in derangements(N):
        if valid(A, k):
            count += 1

    print('actual: {}'.format(count))
    expected = count_derangements(N) / factorial(k)
    # expected = factorial(N) / factorial(k)
    print('expected: {}'.format(expected))


