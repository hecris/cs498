import itertools
import random
import threading
from math import factorial, ceil, e, floor
from collections import Counter

def count_derangements(N):
    return floor((factorial(N) + 1) / e)

def derangements(N):
    ans = []
    A = list(range(N))

    def go(i):
        if i == N:
            ans.append(A.copy())
        else:
            for j in range(i, N):
                if A[j] != i:
                    A[i], A[j] = A[j], A[i]
                    go(i+1)
                    A[i], A[j] = A[j], A[i]

    go(0)
    assert len(ans) == count_derangements(N)
    return ans

def reduce(derangement):
    ans = [x for i, x in enumerate(derangement) if x != i]
    s = sorted(ans)
    ranks = {x: i for i, x in enumerate(s)}
    return [ranks[x] for x in ans]

def print_counter(c):
    for k in sorted(c, key=lambda k: c[k]):
        print(k, c[k])

def experiment(derangements, runs=100):

    count = Counter()

    for _ in range(runs):
        # pick a random derangement
        d = random.choice(derangements).copy()
        n = len(d)

        # perform random swaps until element is frozen
        while True:
            pairs = list(itertools.combinations(list(range(n)), 2))
            i, j = random.choice(pairs)
            d[i], d[j] = d[j], d[i]

            if d[i] == i or d[j] == j:
                break

        # map to reduced-problem size
        r = tuple(reduce(d))
        count[r] += 1

    return count

if __name__ == '__main__':
    # N = int(input("Enter N: "))
    N = 5

    ds = derangements(N)

    trials = 1000
    master_c = Counter()
    for _ in range(trials):
        c = experiment(ds, 1000)
        for k in c:
            master_c[k] += c[k]

    for k in master_c:
        master_c[k] /= trials

    print_counter(master_c)


