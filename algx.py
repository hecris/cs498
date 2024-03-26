import random

def is_derangement(arr):
    return all(arr[i] != i for i in range(len(arr)))

def random_derangement(n):
    arr = list(range(n))
    while not is_derangement(arr):
        random.shuffle(arr)
    return list(arr)

def deter1(arr):
    steps = []
    i = 0
    while i != len(arr):
        if arr[i] != i:
            j = i + 1
            swaps = 0
            while arr[i] != i:
                if arr[j] != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
                j += 1
            steps.append(swaps)

        i += 1
    assert arr == sorted(arr)
    return steps

def deter1p(arr):
    steps = []
    i = len(arr) - 1
    while i != -1:
        if arr[i] != i:
            j = i - 1
            swaps = 0
            while arr[i] != i:
                if arr[j] != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
                    print(arr)
                j -= 1
            steps.append(swaps)

        i -= 1
    assert arr == sorted(arr)
    return steps

def deter2(arr):
    i = 0
    steps = []
    while i < len(arr):
        if arr[i] == i:
            i += 1
        else:
            swaps = 0
            j, k = i, i + 1
            while arr[j] != j:
                while arr[k] == k:
                    k += 1
                arr[j], arr[k] = arr[k], arr[j]
                j = k
                k = k + 1
                swaps += 1
            steps.append(swaps)
    assert arr == sorted(arr)
    return steps

def deter2p(arr):
    i = len(arr) - 1
    steps = []
    while i >= 0:
        if arr[i] == i:
            i -= 1
        else:
            swaps = 0
            j, k = i, i - 1
            while arr[j] != j:
                while arr[k] == k:
                    k -= 1
                arr[j], arr[k] = arr[k], arr[j]
                j = k
                k = k - 1
                swaps += 1
            steps.append(swaps)
    assert arr == sorted(arr)
    return steps

def transform(arr):
    cpy = list(reversed(arr))
    for i in range(len(cpy)):
        cpy[i] = len(cpy) - cpy[i] - 1
    return cpy


N = 10
arr = random_derangement(10)
print('orig: ', arr)
res = (deter1(list(arr)))
print('deter1: ', res, sum(res))
res = (deter1p(list(arr)))
print('deter1p: ', res, sum(res))
res = (deter2(transform(arr)))
print('deter2 transformed: ', res, sum(res))
res = (deter2p(transform(arr)))
print('deter2p transformed: ', res, sum(res))
res = (deter2(list(arr)))
print('deter2: ', res, sum(res))
res = (deter2p(list(arr)))
print('deter2p: ', res, sum(res))

print('dist: ', sum(abs(arr[i] - i) for i in range(len(arr))))

def predict_1p(arr):
    a = sum(i - arr[i] for i in range(len(arr)) if i > arr[i])
    b = sum(arr[i] < i and arr[i] > arr[j] for i in range(len(arr)) for j in range(i + 1, len(arr)))
    c = sum(arr[i] > arr[j] and arr[j] > j for i in range(len(arr)) for j in range(i + 1, len(arr)))
    print(-2 * b + 2 * c)
    return a - b + c

print('predict_1p: ', predict_1p(arr))


