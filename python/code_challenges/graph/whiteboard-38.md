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
2. Instantiate a list for sorted vertices, and a vertex queue.
3. Check if the designated starting vertex value is in the graph.
   i. If it is, enqueue it to the vertex queue
   ii. If not, raise an error.
4. Iterate through the graph's vertices, appending the neighbors of each vertex in order of each vertex to the sorted vertices list.
5. Return the list of sorted vertices.

## Pseudocode

```

```

## Code

```

```
