import random

def is_derangement(arr):
    return all(i != x for i, x in enumerate(arr))


def generate_swap(arr):
    bag = [i for i, x in enumerate(arr) if x == i]
    i = random.choice(bag)
    j = random.choice(bag)

    while (i == j):
        i = random.choice(bag)
        j = random.choice(bag)

    return i, j

def trial(n):
    arr = list(range(n))
    swaps = 0
    while not is_derangement(arr):
        i, j = generate_swap(arr)
        arr[i], arr[j] = arr[j], arr[i]
        swaps += 1
    return swaps

def experiment(n, k=1000):
    total_swaps = 0
    for _ in range(k):
        total_swaps += trial(n)

    return total_swaps / k

N = int(input('N: '))
print(experiment(N))

