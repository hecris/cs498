from BlindArray import BlindArray


def sort(A):
    N = len(A)
    K = A.K

    def partition(front):
        back = N - 1
        while True:
            while front < len(A) and A.is_frozen(front):
                front += 1

            while back >= 0 and A.is_frozen(back):
                back -= 1

            if front < back:
                A.swap(front, back)
                if A.is_frozen(front):
                    front += 1
                    back -= 1
                else:
                    A.swap(front, back)
                    back -= 1
            else:
                break

        return front


    front = 0
    for _ in range(K):
        front = partition(front)

    assert A.is_sorted()

def simulate(N=20, K=5, runs=100):
    for _ in range(runs):
        A = BlindArray(N, K)
        sort(A)

simulate(N=20, K=20, runs=1000)
