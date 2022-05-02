from derangements import derangements, count_derangements
from exp import reduce
import itertools
import math
import collections

N = 8
print(count_derangements(N))

graph = collections.defaultdict()

c = collections.Counter()
for d in derangements(N):
    for i in range(N):
        for j in range(i + 1, N):
            d[i], d[j] = d[j], d[i]
            cpy = tuple(d)
            reduced = reduce(d)
            if len(reduced) == N:
                c[tuple(reduced)] += 1
                graph[cpy].append(reduced)
            d[i], d[j] = d[j], d[i]

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

foo = collections.defaultdict(set)

for k in c:
    # print(k, cycle_decomp(k), c[k])
    cd = tuple(cycle_decomp(k))
    foo[cd].add(c[k])
    # print(k, c[k])


for k in graph:
    print(k, graph[k])
