import random

N = 20
def generate_arr(N):
    arr = list(range(N))
    random.shuffle(arr)
    return arr

def is_sorted(A):
    return all(A[i] == i for i in range(len(A)))

def randpair(N):
    candidates = [(i, j) for i in range(N) for j in range(N) if i != j]
    return random.choice(candidates)

def blindsort(A):
    def check(i, j):
        return A[i] == i or A[j] == j

    def swap(i, j):
        A[i], A[j] = A[j], A[i]

    swaps = 0
    while not is_sorted(A):
        i, j = randpair(len(A))
        if not check(i, j):
            swaps += 1
            swap(i, j)

    return swaps

total = 0
runs = 100
for _ in range(runs):
    arr = generate_arr(N)
    total += blindsort(arr)

avg = total / runs

print('total: {}\nruns: {}\navg: {}'.format(total, runs, avg))
