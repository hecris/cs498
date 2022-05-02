from derangements import derangements, count_derangements
from exp import reduce
import itertools
import math
import collections

N = 5
print(count_derangements(N))

# graph = collections.defaultdict(set)
graph = collections.defaultdict(list)

c = collections.Counter()
for d in derangements(N):
    for i in range(N):
        for j in range(i + 1, N):
            cpy = tuple(d)
            d[i], d[j] = d[j], d[i]
            reduced = reduce(d)
            if len(reduced) == N:
                c[tuple(reduced)] += 1
                # graph[cpy].append(reduced)
                graph[cpy].add(tuple(reduced))
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
