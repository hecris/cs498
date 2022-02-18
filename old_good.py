"""
What's the minimum/maximum number of good swaps
in an array?
"""

import itertools
from collections import Counter

def good_swaps(A):
    swaps = list(itertools.combinations(range(len(A)), 2))
    good = []
    for i, j in swaps:
        if A[i] == j or A[j] == i:
            good.append((i, j))

    return len(good)

N = 9
total_good_swaps = 0
total_permutations = 0
mymax = 0
mymin = float('inf')
c = Counter()
for perm in itertools.permutations(list(range(N))):
    if not any(i == perm[i] for i in range(N)):
        swaps = good_swaps(perm)
        total_good_swaps += swaps
        total_permutations += 1
        mymax = max(mymax, swaps)
        mymin = min(mymin, swaps)
        c[swaps] += 1

print('mymin:', mymin)
print('mymax:', mymax)
ratio = total_good_swaps / total_permutations
print('total_good_swaps:', total_good_swaps)
print('total_permutations:', total_permutations)
print('ratio:', ratio)

for k,v in c.items():
    print('{}: {}'.format(k, v))

# N! / N

'''
1, 0

1, 0, 2

2, 0, 1
1, 2, 0

3, 1, 2
2, 3, 1

3, 1, 2, 4


0, 1, 2
0, 2, 1
1, 0, 2
2, 1, 0
1, 2, 0
2, 0, 1
'''


'''

how do we generate all permutations of length N where
no element is in the correct place

lets genreate all permutations of legnth N - 1 where
no element is in the correct place = R

for each arr in R

we can extend arr using N

but N is in the right correct place

so swap it with any of the first N - 1 elements

should i touch any of the first N - 1 elements

no, because N would be in its correct spot







'''



'''
# generate all permutations of length N where
# no element is in the correct place
def generate(N):
    if N < 2: return []
    if N == 2: return [[2, 1]]

    recurse = generate(N - 1)
    ans = []

    for arr in recurse:
        arr.append(N)
        for i in range(len(arr) - 1):
            arr[i], arr[-1] = arr[-1], arr[i]
            ans.append(arr.copy())
            arr[i], arr[-1] = arr[-1], arr[i]


    return ans

print(generate(2))
print(generate(3))
hi = (generate(4))
assert all(i+1 != A[i] for A in hi for i in range(len(A)))
'''



# def nchoose2(N):
#     return N * (N - 1) // 2

# print(mymin, mymax)
# print((N / 2) / nchoose2(N))
# print(N / nchoose2(N))


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

