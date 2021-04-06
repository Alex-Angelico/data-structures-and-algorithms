# Whiteboard

## Problem Domain

Create a depth-first traversal method for the graph class that accepts a vertex as an argument and returns all vertices in the graph in the appropriate order relative to the starting vertex.

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
[A, B, D, C, E]

## Big O

Time: O(N log(N))
Space: O(N)

## Algorithm

1. Create the function depth_first which accepts a vertex value as an argument.
2. Instantiate a list for sorted vertices, and a second list for ranking known neighbors.
3. Check if the designated starting vertex value is in the graph.
   i. If it is, traverse it using a helper function
   ii. If not, raise an error.
4. define a helper traversal function that accepts a vertex as an argument.
   i. append the value of the vertex to the sorted vertices list
   ii. iterate through the neighbors of the vertex
      a) for every neighbor vertex that is not in the ranking of known neighbors, and whose value is not in the sorted list
          - append the neighbor vertex to known neighbors
          - traverse the neighbor vertex
          - pop the last item from the known neighbors list
5. Return the list of sorted vertices.

## Pseudocode

```
define depth_first (self, origin)
  sorted vertices []
  known neighbors []
  origin = vertex_converter(self, origin)

  define traverse (vertex)
    sorted_vertices append (vertext value)
    for neighbor in vertex adjaceny list
      if neighbor vertex not in known_neighbors and neighbor vertex value not in sorted_vertices
        known_neighbors append (neighbor vertex)
        traverse(neighbor vertex)
        known_neighbors pop last

  traverse(origin)
  return visited_vertices
```

## Code

```
def depth_first(self, origin_vertex):
    visited_vertices = []
    known_neighbors = []
    origin_vertex = Graph.vertex_converter(self, origin_vertex) <---- static method

    def traverse(vertex):
        visited_vertices.append(vertex.value)
        for neighbor in self._adjacency_list[vertex]:
            if neighbor.vertex not in known_neighbors and neighbor.vertex.value not in visited_vertices:
                known_neighbors.append(neighbor.vertex)
                traverse(neighbor.vertex)
                known_neighbors.pop(-1)

    traverse(origin_vertex)
    return visited_vertices
```
