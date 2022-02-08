"""
Algorithm to blind sort if all elements are either 0 or 1.
"""

from BlindArray import BlindArray

def sort(A):
    i, j = 0, len(A) - 1
    while True:
        while i < len(A) and A.is_frozen(i):
            i += 1

        while j >= 0 and A.is_frozen(j):
            j -= 1

        if i < j:
            A.swap(i, j)
            i += 1
            j -= 1
        else:
            break

    assert A.is_sorted()

def simulate(N=20, runs=100):
    for _ in range(runs):
        A = BlindArray(N, 2)
        sort(A)

simulate()
