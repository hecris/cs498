"""
Simulation code for sorting by blindly
swapping randomly or deterministically.
"""

import random
import itertools
from adversary import Adversary

def probabilistic(n):
    A = Adversary(n)
    swaps = 0
    frozen = set()

    while len(frozen) < n:
        candidates = set(range(n)) - frozen
        pairs = list(itertools.combinations(candidates, 2))
        i, j = random.choice(pairs)
        swaps += 1
        frozen.update(A.swap(i, j))

    return swaps

def simulate(N=20, runs=100):
    total = 0
    for _ in range(runs):
        total += probabilistic(N)

    print('total: {}\nruns: {}\navg: {}'.format(total, runs, total / runs))

simulate(N=20, runs=100)
