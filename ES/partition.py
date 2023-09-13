from functools import lru_cache
from S import T

def p(n):
    @lru_cache(None)
    def go(n, coin):
        if n == 0: return 1
        if n >= coin:
            return go(n - coin, coin) + go(n, coin + 1)
        return 0
    return go(n, 1)

def t(n, k):
    c2 = n - k
    n2 = n - 2 * c2
    return p(n2) - p(n2 - 1)

# print(T(10, 5))
# print(t(10, 5))

@lru_cache(None)
def go(n, coin):
    if n == 0: return 1
    if n >= coin:
        return go(n - coin, coin) + go(n, coin + 1)
    return 0

print(go(10, 1))
