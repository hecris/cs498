import pprint
import numpy as np
import itertools
from derangements import derangements, count_derangements
import collections

pp = pprint.PrettyPrinter(indent=4)

def reduce(derangement):
    ans = [x for i, x in enumerate(derangement) if x != i]
    s = sorted(ans)
    ranks = {x: i for i, x in enumerate(s)}
    return tuple(ranks[x] for x in ans)

def print_matrix(mat):
    for row in mat:
        print(row)

def inv_map(l, offset=0):
    return {tuple(x): i + offset for i, x in enumerate(l)}

def nchoose2(n):
    return (n * (n - 1)) // 2

def matrix(n):
    dn = count_derangements(n)
    m = dn

    derange_n = list(derangements(n))

    map_n = inv_map(derange_n)


    mat = [[0 for _ in range(m)] for _ in range(m)]

    for idx, d in enumerate(derange_n):
        for i, j in itertools.combinations(range(n), 2):
            d[i], d[j] = d[j], d[i]

            reduced = reduce(d)

            if len(reduced) == n:
                search = map_n[reduced]
                mat[idx][search] += 1

            d[i], d[j] = d[j], d[i]


    init_prob = []
    for ro in mat:
        s = sum(ro)
        for i in range(len(ro)):
            ro[i] /= s
            if ro[i]:
                init_prob.append(ro[i])


    # subtract by identity
    for i in range(m):
        mat[i][i] -= 1

    # change last column to 1
    for ro in mat:
        ro[-1] = 1

    mat = np.array(mat)
    inv_mat = np.linalg.inv(mat)

    vector = [0 for _ in range(m)]
    vector[-1] = 1

    vector = np.array(vector)

    probs = np.dot(vector, inv_mat)

    print(sorted(normalize(sigfig_set(init_prob))))
    print(sorted(normalize(sigfig_set(probs))))
    return probs


def sigfig_set(l):
    return set(float('%s' % float('%.5g' % x)) for x in l)

def normalize(l):
    s = sum(l)
    return [x/s for x in l]

if __name__ == '__main__':
    N = 5
    matrix(N)
