from functools import lru_cache

# @lru_cache(None)
# def T(N):
#     if N == 1: return 0
#     if N == 2: return 1
#     P1 = 2 / N
#     P2 = 1 / (N * (N - 1))
#     numer = 1 + P1 * T(N - 1) + P2 * T(N - 2)
#     return numer / (P1 + P2)

def T(N):
    prev2, prev1 = 0, 1
    for i in range(3, N + 1):
        P1 = 2 / i
        P2 = 1 / (i * (i - 1))
        numer = 1 + P1 * prev1 + P2 * prev2
        ans = numer / (P1 + P2)
        prev2, prev1 = prev1, ans
    return prev1


if __name__ == '__main__':
    N = int(input())
    print('actual: {}'.format(T(N)))
    print('expected: {}'.format((N * N) / 4))

