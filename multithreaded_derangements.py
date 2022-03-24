from math import floor, factorial, e
import threading
from concurrent.futures import ThreadPoolExecutor

def count_derangements(N):
    return floor((factorial(N) + 1) / e)

def derangements(N, starting_with, idx, ans):
    print(0
            )
    A = list(range(N))

    i = A.index(starting_with)

    A[0], A[i] = A[i], A[0]

    def go(i):
        if i == N:
            # yield A.copy()
            ans[idx].append(A.copy())
        else:
            for j in range(i, N):
                if A[j] != i:
                    A[i], A[j] = A[j], A[i]
                    # yield from go(i+1)
                    go(i + 1)
                    A[i], A[j] = A[j], A[i]

    # go(0)
    # assert len(ans) == count_derangements(N)
    # yield from go(0)
    go(1)

def multithreaded_derangements(N):
    ans = [list() for i in range(1, N)]
    with ThreadPoolExecutor(4) as executor:
        for i in range(N - 1, 0, -1):
            future = executor.submit(derangements, N, i, i - 1, ans)
            # ans[i] = future.result()

    # print(ans)
    assert sum(len(arr) for arr in ans) == count_derangements(N)
    return ans
    

if __name__ == '__main__':
    N = int(input("Enter N: "))

    multithreaded_derangements(N)
    # print(multithreaded_derangements(N))


    # for x in derangements(5, 1):
    #     print(x)
