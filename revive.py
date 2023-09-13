import random
import threading
from math import factorial, ceil, e, floor

def cycle_decomp(A):
    ans = []
    visited = set()
    def dfs(i):
        if i in visited:
            return 0

        visited.add(i)

        return 1 + dfs(A[i])

    for i in range(len(A)):
        if i not in visited:
            ans.append(dfs(i))

    return sorted(ans)


def count_derangements(N):
    return floor((factorial(N) + 1) / e)

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

def deterministic(A, log=False):
    swaps = 0
    if log:
        print(A, cycle_decomp(A), swaps)
    itrs = 0
    for i in range(len(A)):
        if A[i] == i:
            continue
        itrs += 1
        j = i + 1
        while not A[i] == i:
            if A[j] != j:
                A[i], A[j] = A[j], A[i]
                swaps += 1
                # if log:
                #     print(A, swaps)
            j += 1
        if log:
            print(A, cycle_decomp(A), swaps)

    # return itrs
    return swaps

def rdeterministic(A, log=False):
    swaps = 0
    if log:
        print(A, cycle_decomp(A), swaps)
    itrs = 0
    for i in reversed(range(len(A))):
        if A[i] == i:
            continue
        itrs += 1
        j = i - 1
        while not A[i] == i:
            if A[j] != j:
                A[i], A[j] = A[j], A[i]
                swaps += 1
                # if log:
                #     print(A, swaps)
            j -= 1
        if log:
            print(A, cycle_decomp(A), swaps)

    # return itrs
    return swaps


def worst_input(itr, runs, idx, results):
    max_swaps, max_swaps_arr = 0, None
    for _ in range(runs):
        try:
            d = next(itr)
        except:
            break

        swaps = deterministic(d.copy())
        if swaps > max_swaps:
            max_swaps = swaps
            max_swaps_arr = d

    results[idx] = (max_swaps, max_swaps_arr)

def print_counter(c):
    for k, v in c.items():
        print(k, v)

if __name__ == '__main__':
    from collections import Counter, defaultdict

    N = int(input("Enter N: "))
    # worst_input = max(
    #     derangements(N), key=lambda A: deterministic(A.copy()))

    # rworst_input = max(
    #     derangements(N), key=lambda A: rdeterministic(A.copy()))
    worst_input = [6, 7, 8, 9, 3, 4, 5, 2, 1, 0]
    rworst_input = [6, 7, 8, 9, 5, 4, 3, 2, 1, 0]

    print(worst_input)
    print(deterministic(worst_input, log=True))
    print(deterministic(rworst_input, log=True))

    # print('reverse')
    # print(rworst_input)
    # print(rdeterministic(rworst_input, log=True))
