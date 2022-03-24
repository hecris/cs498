from functools import lru_cache

def T(n):
    n2, n1 = 1, 2
    for i in range(4, n+1):


        p1 = 2 / i
        p2 = 1 / (i * (i - 1))

        numer = 1 + p1 * n1 + p2 * n2
        denom = p1 + p2

        n2, n1 = n1, numer / denom

    return n1

if __name__ == '__main__':
    n = int(input('n: '))
    print(T(n))
