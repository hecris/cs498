import random

class BlindArray:
    def __init__(self, N, K=None, all_distinct=True):
        if K is None:
            K = N

        assert N != 0 and 0 < K <= N
        assert not (all_distinct and K < N)

        self.N = N
        self.K = K

        # unique integers
        if all_distinct:
            self.arr = list(range(N))
            random.shuffle(self.arr)
        else:
            # not necessarily unique
            choices = list(range(K))
            self.arr = [random.choice(choices) for _ in range(N)]

        self.sorted_arr = sorted(self.arr)

    def is_frozen(self, i):
        return self.arr[i] == self.sorted_arr[i]

    def swap(self, i, j):
        # assert not (self.is_frozen(i) or self.is_frozen(j))
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def is_sorted(self):
        return self.arr == self.sorted_arr

    def __repr__(self):
        return str(self.arr)

    def __len__(self):
        return self.N
