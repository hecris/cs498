from collections import defaultdict

class Adversary:
    def __init__(self, n):
        # no derangements for n < 2
        assert not n < 2

        # build graph
        self.elements = ['element{}'.format(i) for i in range(n)]
        self.graph = defaultdict(set)

        for i, element in enumerate(self.elements):
            for j in range(n):
                if i != j:
                    self.graph[element].add(j)

                if (i + 1) % n == j:
                    self.__reverse_edge__(element, j)

    def __reverse_edge__(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].add(u)

    def __is_in_matching__(self, element, idx):
        return self.graph[idx] == {element}

    def __attempt_remove__(self, idx, element):
        # try to remove
        self.graph[idx].remove(element)
        found, path = self.__exist_path__(element, idx)
        if found:
            for u, v in path:
                self.__reverse_edge__(u, v)

            return True

        # no alternating path found, edge cannot be removed
        self.graph[idx].add(element)
        return False

    def __exist_path__(self, u, v):
        seen = set()
        def dfs(node):
            if node == v:
                return True, []

            if node not in seen:
                seen.add(node)
                for adj in self.graph[node]:
                    found, path = dfs(adj)
                    if found:
                        return True, [(node, adj)] + path

            return False, []

        return dfs(u)

    def swap(self, i, j):
        # perform swap
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]

        # initialize return array
        frozen = []
        # can we say elements[i] is not in i

        # is (i, elements[i]) in matching?
        if self.__is_in_matching__(self.elements[i], i):
            # attempt to remove (i, elements[i])
            # if can remove, remove it and find alternating path
            removed = self.__attempt_remove__(i, self.elements[i])
            # if can't remove, add it to frozen
            if not removed:
                frozen.append(i)
        else:
            # if no, simply remove (elements[i], i)
            if i in self.graph[self.elements[i]]:
                self.graph[self.elements[i]].remove(i)

        # can we say elements[j] is not in j
        # is (j, elements[j]) in matching?
        if self.__is_in_matching__(self.elements[j], j):
            # attempt to remove (j, elements[j])
            # if can remove, remove it and find alternating path
            removed = self.__attempt_remove__(j, self.elements[j])
            # if can't remove, add it to frozen
            if not removed:
                frozen.append(j)
        else:
            # if no, simply remove (elements[i], i)
            if j in self.graph[self.elements[j]]:
                self.graph[self.elements[j]].remove(j)

        return frozen

    def as_array(self):
        n = len(self.elements)
        return str([next(iter(self.graph[i])).strip('element') for i in range(n)])

    def __repr__(self):
        return '\n'.join(
                '{}: {}'.format(k, v)
                for k, v in self.graph.items()
                )

    def edges(self):
        return '\n'.join(
                '{},  {}'.format(k, x)
                for k, v in self.graph.items()
                for x in v
                )



if __name__ == '__main__':
    a = Adversary(5)
    print(a)
    print(a.swap(0, 1))
    print(a)
