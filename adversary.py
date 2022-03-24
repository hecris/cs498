from collections import defaultdict

class Adversary:
    def __init__(self, n):
        # no derangements for n < 2
        assert not n < 2

        # build graph 
        self.elements = ['element{}'.format(i) for i in range(n)]
        self.indices = ['index{}'.format(i) for i in range(n)]
        self.graph = defaultdict(set)

        for i, index in enumerate(self.indices):
            for j, element in enumerate(self.elements):
                if i != j:
                    self.graph[index].add(element)

                if (i + 1) % n == j:
                    self.__reverse_edge__(index, element)

    def __reverse_edge__(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].add(u)

    def __repr__(self):
        pass

    def swap(self, i, j):
        pas

    def is_frozen(self, i):
        pass


a = Adversary(10)
