import random


def random_permutation(n):
    arr = list(range(n))
    random.shuffle(arr)
    return arr


def is_derangement(arr):
    return all(x != i for i, x in enumerate(arr))


def random_derangement(n):
    arr = list(range(n))
    while not is_derangement(arr):
        random.shuffle(arr)
    return arr


def derangements(N):
    """Generates all derangements length N."""
    ans = []
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
                    pass

    yield from go(0)
