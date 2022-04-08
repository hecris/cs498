import pprint
import numpy as np
import itertools
from derangements import derangements, count_derangements

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
    dn1 = count_derangements(n - 1)
    dn2 = count_derangements(n - 2)

    m = dn + dn1 + dn2

    derange_n = list(derangements(n))
    derange_n1 = list(derangements(n - 1))
    derange_n2 = list(derangements(n - 2))

    map_n = inv_map(derange_n)
    map_n1 = inv_map(derange_n1, dn)
    map_n2 = inv_map(derange_n2, dn + dn1)

    full_map = map_n
    full_map.update(map_n1)
    full_map.update(map_n2)

    for k in sorted(full_map, key=lambda k: full_map[k]):
        print('{}: {}'.format(k, full_map[k]))

    mat = [[0 for _ in range(m)] for _ in range(m)]

    for idx, d in enumerate(derange_n):
        for i, j in itertools.combinations(range(n), 2):
            d[i], d[j] = d[j], d[i]

            reduced = reduce(d)
            search = full_map[reduced]

            mat[idx][search] += 1
            # mat[idx][search] += 1/nchoose2(n)
            d[i], d[j] = d[j], d[i]



    for i in range(dn1 + dn2):
        for j in range(dn):
            mat[~i][j] += 1
            # mat[~i][j] += 1/dn

    # mat = np.array(mat)
    # print(mat)
    # print(np.sum(mat, axis=0))


    for i in range(m):
        for j in range(m):
            if i < dn:
                mat[i][j] = str(mat[i][j]) + '/' + str(nchoose2(n))
            else:
                mat[i][j] = str(mat[i][j]) + '/' + str(dn)

    # print_matrix(mat)

    # for i in range(m - 1):
    #     mat[i][i] -= 1

    # print(mat)
    # inv_mat = np.linalg.inv(mat)
    # print(inv_mat)

    # vector = [0 for _ in range(m)]
    # vector[-1] = 1

    # vector = np.array(vector)

    # print(np.dot(vector, inv_mat))
    # print(map_n)
    # print(map_n1)
    # print(map_n2)

    # print_matrix(mat)
    # print_matrix(mat_exp(mat, 1000))


def mat_exp(mat, exp):
    ans = np.array(mat)
    copy_mat = np.array(mat)

    for i in range(exp - 1):
        ans = np.dot(ans, copy_mat)

    return ans

if __name__ == '__main__':
    print(matrix(4))
