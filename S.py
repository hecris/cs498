from math import comb, factorial

'''
Let S(n, k, s) denote the number of ways to 
split a graph of n vertices into s connected components
each of size > 1 such that there are k good swaps.

Assume
n > 0
0 < k <= n
0 < s < n
s > 0

base cases
n == 1: return 0
k == 0: return 0
s == 1: 
'''

def S(n, k, s):
    if n == 1:
        return 0

    if n == 2:
        return 1 if k == 1 and s == 1 else 0

    if k == -1:
        return 1 if n == 2 and s == 1 else 0

    if not (0 < k <= n):
        return 0

    if s == 1:
        return factorial(n - 1) if k == n else 0

    # n = 6
    # k = 3
    # s = 2
    ans = 0
    for i in range(2, n): # {2, 3, 4, 5}
        # i = 4
        # pick i vertices
        choices = comb(n, i)

        # recurse on graph without these i elements
        recurse = None
        if i == 2:
            recurse = S(n - i, k - 1, s - 1) # S(6 - 2, 3 - 1, 2 - 1) = S(4, 2, 1)
        else:
            recurse = S(n - i, k - i, s - 1) # S(6 - 4, 3 - 4, 2 - 1) = S(2, -1, 1)

        # there are (i - 1)! cycles of i vertices
        cycles = factorial(i - 1)

        # number of graphs = number of ways to choose i vertices *
        #                    number of cycles of i vertices
        #                    number of ways to recurse

        ans += choices * cycles * recurse

    # overcount
    # ans = ans // factorial(s)

    # print('S({}, {}, {}) = {}'.format(n, k, s, ans))
    return ans

def T(n, k):
    ans = 0
    for s in range(1, n):
        x = S(n, k, s)
        # print(x)
        ans += (x // factorial(s))

    return ans

# print(S(4, 3, 2))

# print(T(4, 2))
# print(S(6, 3, 2))
# print(T(5, 3))
# print(T(9, 4))
print(T(9, 5))
print(T(9, 6))
print(T(9, 7))
print(T(9, 8))
print(T(9, 9))

# print(T(5, 5))
# print(T(6, 6))
