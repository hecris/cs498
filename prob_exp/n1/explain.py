from derangements import derangements, count_derangements
from exp import reduce
import itertools
import math
import collections

def nchoose2(N):
    return (N * (N - 1)) // 2

N = 6
print(count_derangements(N))

r = collections.defaultdict(set)
c = collections.Counter()
for d in derangements(N):
    for i in range(N):
        for j in range(i + 1, N):
            d[i], d[j] = d[j], d[i]
            cpy = tuple(d)
            reduced = reduce(d)
            if len(reduced) < N:
                c[tuple(reduced)] += 1
                r[tuple(reduced)].add(cpy)
            d[i], d[j] = d[j], d[i]


ss = collections.Counter()

for k in c:
    print(k, c[k])
    # ss[len(k)] += c[k]

# print(ss)
# print(N - 1, count_derangements(N-1) * N * (N - 1))
# print(N - 2, count_derangements(N-2) * nchoose2(N))

# for k in sorted(r, key=lambda t: len(t)):
#     # print(k, r[k])
#     continue
#     print(k, len(r[k]))


# def cycle_decomp(A):
#     ans = []
#     visited = set()
#     def dfs(i):
#         if i in visited:
#             return 0

#         visited.add(i)

#         return 1 + dfs(A[i])

#     for i in range(len(A)):
#         if i not in visited:
#             ans.append(dfs(i))

#     return sorted(ans)

# foo = collections.defaultdict(set)

# for k in c:
#     # print(k, cycle_decomp(k), c[k])
#     cd = tuple(cycle_decomp(k))
#     foo[cd].add(c[k])
#     # print(k, c[k])


# for k in graph:
#     print(k, graph[k])
