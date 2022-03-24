"""
Simulation code for sorting by blindly
swapping randomly or deterministically.
"""

import random
import itertools
from BlindArray import BlindArray

def probabilistic(A):
    swaps = 0
    while not A.is_sorted():
        candidates = filter(
                lambda idx: not A.is_frozen(idx), range(len(A)))

        pairs = list(itertools.combinations(candidates, 2))
        i, j = random.choice(pairs)
        if not A.is_frozen(i) and not A.is_frozen(j):
            swaps += 1
            A.swap(i, j)

    return swaps

def deterministic(A):
    swaps = 0
    for i in range(len(A)):
        j = i + 1
        while not A.is_frozen(i):
            if not A.is_frozen(j):
                A.swap(i, j)
                swaps += 1
            j += 1

    return swaps

def simulate(N=20, runs=100):
    total = 0
    for _ in range(runs):
        A = BlindArray(N)
        total += deterministic(A)

    print('total: {}\nruns: {}\navg: {}'.format(total, runs, total / runs))
    print((N * (N - 1)) / 3)

simulate(N=30, runs=10000)
