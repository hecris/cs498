"""
What's the minimum/maximum number of good swaps
in an array?
"""

import itertools

def good_swaps(A):
    swaps = list(itertools.combinations(range(len(A)), 2))
    good = []
    for i, j in swaps:
        if A[i] == j or A[j] == i:
            good.append((i, j))

    return len(good) / len(swaps)

N = 10
mymax = 0
mymin = 1
for perm in itertools.permutations(list(range(N))):
    if not any(i == perm[i] for i in range(N)):
        ratio = good_swaps(perm)
        mymax = max(mymax, ratio)
        mymin = min(mymin, ratio)

def nchoose2(N):
    return N * (N - 1) // 2

print(mymin, mymax)
print((N / 2) / nchoose2(N))
print(N / nchoose2(N))


# generate a permutation of 0..N-1 such that no element is in its correct position
# def solution(N):
#     if N == 2: return [1, 0]
#     ans = solution(N - 1) + [N - 1]
#     ans[0], ans[N - 1] = ans[N - 1], ans[0]
#     return ans


# for N in range(2, 20):
#     sol = solution(N)
#     print(sol)
#     assert not any(i == sol[i] for i in range(N))
