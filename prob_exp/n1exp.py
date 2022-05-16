import itertools
import random
import threading
from math import factorial, ceil, e, floor
from collections import Counter
import numpy

def is_derangement(a):
    return not any(a[i] == i for i in range(len(a)))

def random_derangement(n):
    a = list(range(n))
    while not is_derangement(a):
        a = numpy.random.permutation(a)
    return a


def reduce(derangement):
    ans = [x for i, x in enumerate(derangement) if x != i]
    s = sorted(ans)
    ranks = {x: i for i, x in enumerate(s)}
    return [ranks[x] for x in ans]

def print_counter(c):
    for k in sorted(c, key=lambda k: c[k]):
        print(k, c[k])

def experiment(n, runs=100):

    count = Counter()

    for _ in range(runs):
        # pick a random derangement
        d = random_derangement(n)

        pairs = itertools.combinations(list(range(n)), 2)
        swaps1 = [(i, j) for i, j in pairs if (d[i] == j) ^ (d[j] == i)]

        if not swaps1:
            continue

        i, j = random.choice(swaps1)
        d[i], d[j] = d[j], d[i]

        # map to reduced-problem size
        r = tuple(reduce(d))
        count[r] += 1

    return count

if __name__ == '__main__':
    # N = int(input("Enter N: "))
    n = 9

    c = experiment(n, 1000000)
    print(set(c.values()))
