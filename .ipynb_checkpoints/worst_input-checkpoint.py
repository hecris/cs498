import random
import threading
from math import factorial, ceil, e, floor

def count_derangements(N):
    return floor((factorial(N) + 1) / e)

def derangements(N):
    ans = []
    A = list(range(N))

    def go(i):
        if i == N:
            yield A.copy()
            # ans.append(A.copy())
        else:
            for j in range(i, N):
                if A[j] != i:
                    A[i], A[j] = A[j], A[i]
                    yield from go(i+1)
                    A[i], A[j] = A[j], A[i]
                    pass

    # go(0)
    # assert len(ans) == count_derangements(N)
    yield from go(0)

class DerangementsIterator:
    def __init__(self, N):
        self.lock = threading.Lock()
        self.N = N

    def __iter__(self):
        self.generator = derangements(self.N)
        return self

    def __next__(self):
        with self.lock:
            return next(self.generator)


def deterministic(A, log=False):
    swaps = 0
    if log:
        print(A, swaps)
    itrs = 0
    for i in range(len(A)):
        if A[i] == i:
            continue
        itrs += 1
        j = i + 1
        while not A[i] == i:
            if A[j] != j:
                A[i], A[j] = A[j], A[i]
                swaps += 1
                # if log:
                #     print(A, swaps)
            j += 1
        if log:
            print(A, swaps)

    # return itrs
    return swaps

def worst_input(itr, runs, idx, results):
    max_swaps, max_swaps_arr = 0, None
    for _ in range(runs):
        try:
            d = next(itr)
        except:
            break

        swaps = deterministic(d.copy())
        if swaps > max_swaps:
            max_swaps = swaps
            max_swaps_arr = d

    results[idx] = (max_swaps, max_swaps_arr)

def print_counter(c):
    for k, v in c.items():
        print(k, v)

def multithreaded_search(N, thread_count):
    d = DerangementsIterator(N)
    itr = iter(d)

    total = (factorial(N) + 1) / e
    x = ceil(total / thread_count)
    results = [None for _ in range(thread_count)]
    threads = [
            threading.Thread(target=worst_input, args=(itr, x, i, results))
            for i in range(thread_count)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return results


if __name__ == '__main__':
    from collections import Counter, defaultdict

    N = int(input("Enter N: "))
    # for x in derangements(N):
    #     pass
    # x = factorial(N)

    # results = multithreaded_search(N, 5)


    # for x in itr:
    #     print(x)


    worst_input =  max(
        derangements(N), key=lambda A: deterministic(A.copy()))

    print(worst_input)
    print(deterministic(worst_input, log=True))

    # counts = {
    #         deterministic(A.copy()): A for A in derangements(N)
    #         }

    # counts = defaultdict(list)
    # for A in derangements(N):
    #     swaps = deterministic(A.copy())
    #     counts[swaps].append(A)

    # print_counter(counts)
    # x = random.randint(0, count_derangements(N))
    # itr = derangements(N)
    # for _ in range(x):
    #     print(next(itr))

    # print(deterministic([5, 6, 7, 8, 9, 10, 4, 3, 2, 1, 0], log=True))
    # print(deterministic([5, 6, 7, 8, 9, 4, 3, 2, 1, 0], log=True))
    # print(deterministic([0, 1, 2, 3, 5, 4, 9, 6, 7, 8], log=True))
    # print(deterministic([6, 7, 8, 9, 5, 4, 3, 2, 1, 0], log=True))
    # print(deterministic([3, 4, 1, 2, 0], log=True))
    # print(deterministic([3, 4, 2, 1, 0], log=True))
    # print(deterministic([2, 3, 4, 1, 0], log=True))
    # print(deterministic([4, 3, 2, 1, 0], log=True))


    # c = Counter(
    #         deterministic(A) for A in derangements(N))

#     exp = {
#             34: [[5, 6, 7, 8, 9, 3, 4, 2, 1, 0], [5, 6, 7, 8, 9, 4, 2, 3, 1, 0], [5, 6, 7, 8, 9, 4, 3, 2, 0, 1], [5, 6, 7, 8, 9, 4, 3, 1, 2, 0], [5, 6, 7, 9, 8, 4, 3, 2, 1, 0], [5, 6, 8, 7, 9, 4, 3, 2, 1, 0], [5, 7, 6, 8, 9, 4, 3, 2, 1, 0], [5, 7, 8, 9, 3, 4, 2, 6, 1, 0], [6, 5, 7, 8, 9, 4, 3, 2, 1, 0], [6, 7, 8, 2, 9, 4, 5, 3, 1, 0], [6, 7, 8, 9, 1, 4, 5, 3, 2, 0], [6, 7, 8, 9, 2, 4, 5, 1, 3, 0], [6, 7, 8, 9, 2, 4, 5, 3, 0, 1], [6, 7, 8, 9, 2, 4, 3, 5, 1, 0], [6, 7, 8, 9, 2, 3, 5, 4, 1, 0], [6, 7, 8, 9, 3, 1, 5, 4, 2, 0], [6, 7, 8, 9, 3, 2, 5, 1, 4, 0], [6, 7, 8, 9, 3, 2, 5, 4, 0, 1], [6, 7, 8, 9, 3, 2, 4, 5, 1, 0], [6, 7, 8, 9, 3, 4, 1, 5, 2, 0], [6, 7, 8, 9, 3, 4, 2, 1, 5, 0], [6, 7, 8, 9, 3, 4, 2, 5, 0, 1], [6, 7, 8, 9, 3, 4, 5, 1, 0, 2], [6, 7, 8, 9, 3, 4, 5, 0, 2, 1], [6, 7, 9, 8, 3, 4, 5, 1, 2, 0], [6, 7, 9, 8, 3, 4, 5, 2, 0, 1], [6, 7, 9, 8, 3, 4, 2, 5, 1, 0], [6, 7, 9, 8, 3, 2, 5, 4, 1, 0], [6, 7, 9, 8, 2, 4, 5, 3, 1, 0], [6, 8, 7, 9, 2, 4, 5, 3, 1, 0], [6, 8, 7, 9, 3, 2, 5, 4, 1, 0], [6, 8, 7, 9, 3, 4, 2, 5, 1, 0], [6, 8, 7, 9, 3, 4, 5, 2, 0, 1], [6, 8, 7, 9, 3, 4, 5, 1, 2, 0], [6, 8, 9, 7, 3, 4, 5, 2, 1, 0], [6, 9, 7, 8, 3, 4, 5, 2, 1, 0], [7, 6, 8, 9, 2, 4, 5, 3, 1, 0], [7, 6, 8, 9, 3, 2, 5, 4, 1, 0], [7, 6, 8, 9, 3, 4, 2, 5, 1, 0], [7, 6, 8, 9, 3, 4, 5, 2, 0, 1], [7, 6, 8, 9, 3, 4, 5, 1, 2, 0], [7, 6, 9, 8, 3, 4, 5, 2, 1, 0], [7, 8, 6, 9, 3, 4, 5, 2, 1, 0], [8, 6, 7, 9, 3, 4, 5, 2, 1, 0]],
#             35: [[5, 6, 7, 8, 9, 4, 3, 2, 1, 0], [6, 7, 8, 9, 2, 4, 5, 3, 1, 0], [6, 7, 8, 9, 3, 2, 5, 4, 1, 0], [6, 7, 8, 9, 3, 4, 2, 5, 1, 0], [6, 7, 8, 9, 3, 4, 5, 1, 2, 0], [6, 7, 8, 9, 3, 4, 5, 2, 0, 1], [6, 7, 9, 8, 3, 4, 5, 2, 1, 0], [6, 8, 7, 9, 3, 4, 5, 2, 1, 0], [7, 6, 8, 9, 3, 4, 5, 2, 1, 0]],
#             36: [[6, 7, 8, 9, 3, 4, 5, 2, 1, 0]]
#             }


#     for swaps, larr in exp.items():
#         print(swaps)
#         for arr in larr:
#             print('\t{}'.format(deterministic(arr)))

