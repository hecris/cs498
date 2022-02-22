import itertools
from collections import Counter
from S import T, count_derangements
from math import factorial, floor, e

def good_swaps(A):
    swaps = list(itertools.combinations(range(len(A)), 2))
    good = []
    for i, j in swaps:
        if A[i] == j or A[j] == i:
            good.append((i, j))

    return len(good)

def derangements(N):
    ans = []
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

def count(N):
    c = Counter()
    num_derangements = 0
    for perm in derangements(N):
        num_good_swaps = good_swaps(perm)
        c[num_good_swaps] += 1
        num_derangements += 1

    assert num_derangements == count_derangements(N)
    return c

def print_counter(c):
    for k, v in c.items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    N = int(input('Enter N: '))

    c = count(N)
    for k, v in c.items():
        print('Brute force: There are {} permutations with {} good swaps'.format(v, k))
        print('My algorithm: There are {} permutations with {} good swaps'.format(v, k))
        assert T(N, k) == v
