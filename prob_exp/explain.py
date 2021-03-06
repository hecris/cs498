from derangements import derangements, count_derangements
from exp import reduce
import itertools
import math
import collections

N = 8
print(count_derangements(N))

graph = collections.defaultdict(set)

c = collections.Counter()
for d in derangements(N):
    for i in range(N):
        for j in range(i + 1, N):
            cpy = tuple(d)
            d[i], d[j] = d[j], d[i]
            reduced = reduce(d)
            if len(reduced) == N:
                c[tuple(reduced)] += 1
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

def nchoose2(n):
    return (n * (n - 1)) // 2

def degree(C):
    n = sum(C)
    return nchoose2(n) - n + sum(x == 2 for x in C)

foo = collections.defaultdict(set)

for k in c:
    # print(k, cycle_decomp(k), c[k])
    cd = tuple(cycle_decomp(k))
    foo[cd].add(c[k])
    # print(k, c[k])


# for k in graph:
#     print(k, graph[k])

probs = collections.defaultdict(set)
s = 0

for node, neighbors in graph.items():
    num_d = count_derangements(N)
    prob = 0
    for neighbor in neighbors:
        d = degree(cycle_decomp(neighbor))
        prob += 1 / d

    prob *= 1/num_d
    s += prob

    prob_s = float('%s' % float('%.5g' % prob))

    tc = tuple(cycle_decomp(node))
    probs[tc].add(prob_s)

for k in probs:
    print(k, probs[k])

print(s)
