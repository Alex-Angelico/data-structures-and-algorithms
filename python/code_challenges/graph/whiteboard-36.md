# Whiteboard

## Problem Domain

Create a breadth-first traversal method for the graph class that accepts a vertex as an argument and returns all vertices in the graph in the appropriate order relative to the starting vertex.

## Edge Cases

Graph is empty.

## Visualization

INPUT
A, B, C, D, E
A -> B (1)
A -> C (2)
B -> D (3)
C -> D (4)
A -> E (5)

Starting vertex: A

OUTPUT
[A, B, C, E, D]

## Big O

Time: O(N^2)
Space: O(N)

## Algorithm

1. Create the function breadth_first which accepts a vertex value as an argument.
2. Instantiate a list for sorted vertices, and a vertex queue.
3. Check if the designated starting vertex value is in the graph.
   i. If it is, enqueue it to the vertex queue
   ii. If not, raise an error.
4. Iterate through the graph's vertices, appending the neighbors of each vertex in order of each vertex to the sorted vertices list.
5. Return the list of sorted vertices.

## Pseudocode

```
define breadth_first(starting vertex)
  visited vertices []
  vertex queue
  for vertex in graph adjacency list
    if starting vertex is vertex's value
      enqueue vertex
    if cycled whole adjacency list
      raise KeyError

  while less than graph size
    dequeue vertex
    if dequeued vertex value not in sorted vertices
      append vertex value to sorted
      enqueue all neighbors of the appended vertex

  return sorted vertices
```

## Code

```
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
```
