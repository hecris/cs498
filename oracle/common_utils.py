import random

BEFORE = lambda i, x, *args: x > i
AFTER = lambda i, x, *args: x < i


def random_permutation(n):
    """Generates a random permutation of [0, ..., n - 1]."""
    arr = list(range(n))
    random.shuffle(arr)
    return arr


def is_derangement(arr):
    """Returns true if `arr` is a derangement."""
    return all(x != i for i, x in enumerate(arr))


def random_derangement(n):
    """Generates a random derangement of [0, ..., n - 1]."""
    arr = list(range(n))
    while not is_derangement(arr):
        random.shuffle(arr)
    return arr


def derangements(n):
    """Generates all derangements length N."""
    ans = []
    A = list(range(n))

    def go(i):
        if i == n:
            yield A.copy()
        else:
            for j in range(i, n):
                if A[j] != i:
                    A[i], A[j] = A[j], A[i]
                    yield from go(i+1)
                    A[i], A[j] = A[j], A[i]
                    pass

    yield from go(0)


def count_inversions(arr, cond=lambda i, x, j, y: True):
    """Counts the number of inversions, optionally satisfying a certain condition."""
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j] and cond(i, arr[i], j, arr[j]):
                count += 1
    return count


def count_good_inversions(arr):
    """Counts the number of good inversions."""
    def cond(i, x, j, y): return y > j
    return count_inversions(arr, cond)


def get_abs_dist(arr, cond=lambda i, x: True):
    ans = 0
    for i, x in enumerate(arr):
        if cond(i, x):
            ans += abs(i - x)
    return ans


def num_swaps_eq1(arr):
    return count_inversions(arr) - 2 * count_good_inversions(arr)


def num_swaps_eq2(arr):
    return get_abs_dist(arr, BEFORE) + count_inversions(arr, AFTER) - count_good_inversions(arr)


if __name__ == '__main__':
    arr = [6, 7, 8, 9, 3, 4, 5, 2, 1, 0]
    print(count_inversions(arr))
    print(count_good_inversions(arr))
    print(get_abs_dist(arr))
    assert num_swaps_eq1(arr) == num_swaps_eq2(arr)
