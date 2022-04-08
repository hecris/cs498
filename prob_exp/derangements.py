from math import factorial, ceil, e, floor

def count_derangements(N):
    return floor((factorial(N) + 1) / e)

def derangements(N):
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

    yield from go(0)
