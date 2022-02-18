"""
What's the minimum/maximum number of good swaps
in an array?
"""

import itertools
from collections import Counter
from S import T

def good_swaps(A):
    swaps = list(itertools.combinations(range(len(A)), 2))
    good = []
    for i, j in swaps:
        if A[i] == j or A[j] == i:
            good.append((i, j))

    return len(good)

def count(N):
    c = Counter()
    for perm in itertools.permutations(list(range(N))):
        if not any(i == perm[i] for i in range(N)):
            swaps = good_swaps(perm)
            c[swaps] += 1
            swaps
    return c

def print_counter(c):
    for k, v in c.items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    N = 8
    c = count(N)
    for k, v in c.items():
        assert T(N, k) == v
