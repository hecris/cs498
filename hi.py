import itertools
from math import factorial


def hey(n, k):
    a = list(range(n))
    total = 0
    for c in itertools.combinations(a, k):
        total += sum(c[i] + 1 == c[i+1] for i in range(len(c) - 1))
        
        # print(c)



    pickpair = n - 1
    pickpair *= factorial(n - 2) / factorial(n - k)

    # for i in range(k - 2):
    #     pickpair *= (n - 2 - i)

    expected = pickpair // (factorial(k - 2))

    # print(total)
    # print(expected)
    assert total == expected

for n in range(2, 15):
    for k in range(2, n+1):
        hey(n, k)
