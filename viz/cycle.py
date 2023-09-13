from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

arr = [6, 7, 8, 9, 3, 4, 5, 2, 1, 0]
arr = [6, 7, 8, 9, 5, 4, 3, 2, 1, 0]

def build_graph(arr):
    graph = defaultdict(list)
    for i, x in enumerate(arr):
        graph[x].append(i)
    return graph

G = nx.DiGraph(build_graph(arr))
pos = nx.spring_layout(G, scale=3)

nx.draw(G, pos, with_labels = True)
# plt.show()
plt.savefig('img.png')

