from derangements import derangements, count_derangements
from exp import reduce
import itertools
import math
import collections

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

N = 7
print(count_derangements(N))


de = collections.Counter()
c = collections.Counter()
for d in derangements(N):

    tmp_c = collections.Counter()

    for i in range(N):
        for j in range(i + 1, N):
            d[i], d[j] = d[j], d[i]
            reduced = reduce(d)
            if len(reduced) == N - 1:
                tmp_c[tuple(reduced)] += 1
            d[i], d[j] = d[j], d[i]

    n1_swaps = sum(tmp_c.values())
    for k in tmp_c:
        c[k] += tmp_c[k] / n1_swaps

    de[tuple(cycle_decomp(d))] += 1

# for k in de:
#     print(k, de[k])

s = set()
for k in c:
    print(k, cycle_decomp(k), c[k])
    # print(k, c[k])
    # s.add((tuple(cycle_decomp(k)), c[k]))
    s.add((sum(x == 2 for x in tuple(cycle_decomp(k))), int(c[k])))

print(s)
