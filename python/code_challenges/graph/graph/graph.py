class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        new_vertex = Vertex(value)
        self._adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, start_vertex, end_vertex, weight=1):
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in graph')
        new_edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(new_edge)

    def get_nodes(self):
        return None if not self._adjacency_list else [node.value for node in self._adjacency_list]

    def get_neighbors(self, vertex):
        if vertex not in self._adjacency_list:
            raise KeyError('Vertex not in graph')
        return [{neighbor.vertex.value: neighbor.weight} for neighbor in self._adjacency_list[vertex]]

    def size(self):
        return len(self._adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(a, c, 2)
    print(graph.get_neighbors(a))
    print(a, b)
