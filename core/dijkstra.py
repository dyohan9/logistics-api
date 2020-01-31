# Referencia (original): https://gist.github.com/econchick/4666413
# Referencia (original): https://github.com/vglinden/Dijkstra

import collections


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.costs = {}

    def add_node(self, node):
        for name in node:
            self.nodes.add(name)

    def add_edge(self, node_a, node_b, cost):
        self.edges[node_a].append(node_b)
        self.edges[node_b].append(node_a)
        self.costs[(node_a, node_b)] = cost
        self.costs[(node_b, node_a)] = cost

    def dijsktra(self, initial):
        visited = {initial: 0}
        nodes = set(self.nodes)
        path = {}

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)

            for edge in self.edges[min_node]:
                cost = visited[min_node] + self.costs[(min_node, edge)]
                if edge not in visited or cost < visited[edge]:
                    visited[edge] = cost
                    path[edge] = min_node

        return visited, path

    def caminho(self, inicial, final):
        visited, path = self.dijsktra(inicial)
        trajeto = []
        atual = final
        while atual is not inicial:
            trajeto.append(atual)
            atual = path[atual]

        trajeto.append(atual)
        trajeto.reverse()

        return visited[final], trajeto
