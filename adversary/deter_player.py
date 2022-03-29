from adversary import Adversary

def deterministic(n):
    A = Adversary(n)
    frozen = set()
    swaps = 0

    for i in range(n):
        j = i + 1
        while i not in frozen:
            if j not in frozen:
                frozen.update(A.swap(i, j))
                swaps += 1
            j += 1

    print(A.original_array())
    return swaps

if __name__ == '__main__':
    n = int(input('n: '))
    print(deterministic(n))

