from math import comb, factorial

# how many permutations of [1,2,..n] are there such
# that there are k good swaps
memo = {}
def swaps(n, k):
    print(n, k)
    ans = 0
    if n == 0:
        ans = 0
    elif n == 1:
        ans = 1 if k == 0 else 0
    elif n == 2:
        ans = 1 if k == 1 else 0
    elif k > n:
        ans = 0
    else:
        if n == k:
            ans += factorial(n - 1)
        for i in range(2, k+1):
            itr = 0
            if i == 2:
                itr = (comb(n, i) * swaps(n - i, k - 1)) // 2
                ans += itr
            else:
                itr = (comb(n, i) * factorial(i - 1) * swaps(n - i, k - i)) // 2
                ans += itr

            if n == 5:
                print(i, itr)

    memo[n, k] = ans
    return ans

# print(swaps(5, 5)) # 24
print(swaps(5, 4)) # 160

# 2, 3, 4

for k in sorted(memo):
    print('{}: {}'.format(k, memo[k]))
