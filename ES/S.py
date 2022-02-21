from functools import lru_cache
from math import comb, factorial, floor, e

'''
Let S(n, k, s) denote the number of ways to
split a graph of n vertices into s connected components,
each of size > 1 such that there are k good swaps.
'''

@lru_cache(None)
def S(n, k, s):
    if n == 0:
        return 1 if k == 0 and s == 0 else 0

    if n == 1:
        return 0

    if n == 2:
        return 1 if k == 1 and s == 1 else 0

    if not (0 < k <= n):
        return 0

    ans = 0
    for i in range(2, n + 1): 
        # pick i vertices
        choices = comb(n, i)

        # recurse on graph without these i elements
        recurse = None
        if i == 2:
            recurse = S(n - i, k - 1, s - 1)
        else:
            recurse = S(n - i, k - i, s - 1)

        # there are (i - 1)! cycles of i vertices
        cycles = factorial(i - 1)

        # number of graphs = number of ways to choose i vertices *
        #                    number of cycles of i vertices
        #                    number of ways to recurse

        ans += choices * cycles * recurse

    return ans

def T(n, k):
    ans = 0
    for s in range(1, n):
        x = S(n, k, s)
        ans += (x // factorial(s))

    return ans

def count_derangements(N):
    return floor((factorial(N) + 1) / e)

# Let S be number of good swaps.
# E(S) = sum(p_k * k for k = {1, ..., N})
# E(S) = sum((# of permutations with k good swaps) / # permutations for k = {1, ..., N})
def E(N):
    my_sum = 0
    for k in range(N//2, N+1):
        my_sum += T(N, k) * k

    return my_sum / count_derangements(N)

if __name__ == '__main__':
    N = int(input('Enter N: '))
    for k in range(0, N+1):
        t = T(N, k)
        print('There are {} permutations with {} good swaps'.format(t, k))

    print('Expected number of good swaps: {}'.format(E(N)))

