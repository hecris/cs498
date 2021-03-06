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
                    self._reverse_edge(element, j)

    def _reverse_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].add(u)

    def _is_in_matching(self, element, idx):
        return self.graph[idx] == {element}

    def _exist_path(self, u, v):
        seen = set()
        path = []

        def dfs(node):
            if node == v:
                return True

            if node not in seen:
                seen.add(node)
                for adj in self.graph[node]:
                    path.append((node, adj))
                    found = dfs(adj)
                    if found:
                        return True
                    path.pop()

            return False

        return dfs(u), path

    def _attempt_remove(self, idx, element):
        # if edge is not in matching, simply remove
        if not self._is_in_matching(element, idx):
            if idx in self.graph[element]:
                self.graph[element].remove(idx)
            return True

        # try to remove, and see if there is an alternating path
        self.graph[idx].remove(element)
        found, path = self._exist_path(element, idx)
        if found:
            for u, v in path:
                self._reverse_edge(u, v)

            return True

        # no alternating path found, edge cannot be removed.
        # add edge back into graph
        self.graph[idx].add(element)
        return False

    def swap(self, i, j):
        # perform swap
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]

        # initialize return value
        frozen = []

        # can we say elements[i] cannot be in position i
        removed = self._attempt_remove(i, self.elements[i])
        if not removed:
            # if can't remove, add it to frozen
            frozen.append(i)

        # repeat for j
        removed = self._attempt_remove(j, self.elements[j])
        if not removed:
            frozen.append(j)

        return frozen

    def original_array(self):
        n = len(self.elements)
        arr = [None] * n
        for i in range(n):
            element = next(iter(self.graph[i]))
            element_number = int(element.strip('element'))
            arr[element_number] = i

        return arr

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
