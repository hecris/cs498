from derangements import derangements, count_derangements
from exp import reduce
import itertools
import math
import collections

N = 5
print(count_derangements(N))

c = collections.Counter()
for d in derangements(N):
    for i in range(N):
        for j in range(i + 1, N):
            d[i], d[j] = d[j], d[i]
            reduced = reduce(d)
            if len(reduced) < N:
                c[tuple(reduced)] += 1
            d[i], d[j] = d[j], d[i]

for k in c:
    print(k, c[k])
