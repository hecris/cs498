from n1exp import random_derangement
import itertools
import random

def probabilistic(A):
    swaps = 0
    while True:
        candidates = filter(lambda idx: A[idx] != idx, range(len(A)))
        pairs = list(itertools.combinations(candidates, 2))
        if not pairs:
            break
        i, j = random.choice(pairs)
        swaps += 1
        A[i], A[j] = A[j], A[i]

    return swaps

def trial(n):
    A = random_derangement(n)
    return probabilistic(A)

def exp(n, trials):
    count = 0
    for _ in range(trials):
        count += trial(n)

    return count / trials

n = 40
trials = 1000
print(exp(n, trials))
print((n * (n - 1)) / 4)

