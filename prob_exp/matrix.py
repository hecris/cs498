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
    dn1 = count_derangements(n - 1)
    dn2 = count_derangements(n - 2)

    m = dn + dn1 + dn2

    derange_n = list(derangements(n))
    derange_n1 = list(derangements(n - 1))
    derange_n2 = list(derangements(n - 2))

    full_derange = list(derange_n)
    full_derange.extend(derange_n1)
    full_derange.extend(derange_n2)

    map_n = inv_map(derange_n)
    map_n1 = inv_map(derange_n1, dn)
    map_n2 = inv_map(derange_n2, dn + dn1)

    full_map = map_n
    full_map.update(map_n1)
    full_map.update(map_n2)

    mat = [[0 for _ in range(m)] for _ in range(m)]

    for idx, d in enumerate(derange_n):
        for i, j in itertools.combinations(range(n), 2):
            d[i], d[j] = d[j], d[i]

            reduced = reduce(d)
            search = full_map[reduced]

            # if len(reduced) < n:
            mat[idx][search] += 1

            d[i], d[j] = d[j], d[i]


    for i in range(dn1 + dn2):
        for j in range(dn):
            # mat[~i][j] += 1
            mat[~i][j] += 1

    for ro in mat:
        s = sum(ro)
        for i in range(len(ro)):
            ro[i] /= s

    # for ro in mat:
    #     print(ro)


    # print(np.sum(mat, axis=0))

    # for i in range(m):
    #     for j in range(m):
    #         if i < dn:
    #             mat[i][j] = str(mat[i][j]) + '/' + str(nchoose2(n))
    #         else:
    #             mat[i][j] = str(mat[i][j]) + '/' + str(dn)

    # print_matrix(mat)

    # change last column to 1
    for ro in mat:
        ro[-1] = 1

    # multiply by modified identity
    for i in range(m - 1):
        mat[i][i] -= 1

    mat = np.array(mat)
    inv_mat = np.linalg.inv(mat)

    # print(mat)
    # print(inv_mat)

    vector = [0 for _ in range(m)]
    vector[-1] = 1

    vector = np.array(vector)

    probs = np.dot(vector, inv_mat)

    # print(probs)

    sorted_probs = sorted(((x, i) for i, x in enumerate(probs)), reverse=True)

    for x, i in sorted_probs:
        d = full_derange[i]
        if len(d) < n:
            print('{}: {}'.format(d, x))

    classes = {}
    for x, i in sorted_probs:
        d = full_derange[i]
        if len(d) != n:
            continue
        classes.setdefault(x, [])
        classes[x].append(d)

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

        return tuple(sorted(ans))

    for k in classes:
        classes[k] = set(map(cycle_decomp, classes[k]))

    for k in classes:
        print(k, classes[k])

    print('----------')


    probs = collections.defaultdict(set)
    for k in classes:
        t = tuple(classes[k])
        rounded = float('%s' % float('%.5g' % k))
        probs[t].add(rounded)

    for k in probs:
        print(k, probs[k])

    # target_probs = [t for t in sorted_probs if len(full_derange[t[1]]) == n - 1]
    # target_sum = sum(t[0] for t in target_probs)

    # scaled_target_probs = [
    #         (prob / target_sum, idx) for prob, idx in target_probs
    #         ]
    # print(target_probs)
    # print(scaled_target_probs)
    # print('scaled')

    # min_prob = min(t[0] for t in scaled_target_probs)
    # max_prob = max(t[0] for t in scaled_target_probs)
    # print(set(t[0] for t in scaled_target_probs))


    # for x, i in scaled_target_probs:
    #     d = full_derange[i]
    #     if len(d) < n:
    #         print('{}: {}'.format(d, x))

    # print(min_prob / max_prob)
    return probs

    # print_matrix(mat_exp(mat, 1000))


def mat_exp(mat, exp):
    ans = np.array(mat)
    copy_mat = np.array(mat)

    for i in range(exp - 1):
        ans = np.dot(ans, copy_mat)

    return ans

if __name__ == '__main__':
    # print(matrix(5))
    N = 8
    matrix(N)
    # print(matrix(N))
