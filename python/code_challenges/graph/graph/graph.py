from graph.stacks_and_queues import Node, Queue
# from stacks_and_queues import Node, Queue


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

    def breadth_first(self, origin_vertex):
        visited_vertices = []
        vertex_queue = Queue()
        i = 0
        for vertex in self._adjacency_list:
            if origin_vertex == vertex.value:
                vertex_queue.enqueue(vertex)
                break
            i += 1
            if i == self.size():
                raise KeyError('Vertex not in graph')

        j = 0
        while j < self.size() + 1:
            vertex = vertex_queue.dequeue()
            if vertex.value not in visited_vertices:
                visited_vertices.append(vertex.value)
                for neighbor in self._adjacency_list[vertex]:
                    vertex_queue.enqueue(neighbor.vertex)
            j += 1

        return visited_vertices


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
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(a, e)
    graph.add_edge(e, f)
    graph.add_edge(e, g)
    graph.add_edge(f, h)
    print(graph.get_neighbors(a))
    print(a, b)
    print(graph.breadth_first('a'))
