# README

## Graph Implementaiton

### Author: Alex Angelico

### Problem Domain

#### Challenge 35

Create Graph, Vertex, and Edge classes which together allow for the construction and representation of various graphs.

#### Challenge 36

Create a breadth-first traversal method for the graph class that accepts a vertex as an argument and returns all vertices in the graph in the appropriate order relative to the starting vertex.

#### Challenge 37

Write a function which takes in a graph of city names with edges weighed as plane ticket prices, and a list of city names. Return whether the trip between the cities is possible with direct flights, and how much it would cost.

#### Challenge 38

Create a depth-first traversal method for the graph class that accepts a vertex as an argument and returns all vertices in the graph in the appropriate order relative to the starting vertex.

### Inputs and Expected Outputs

#### Challenge 35

Input | Expected Output
----- | ---------------
A, B, C, D | A ----(2)---> C
A -> B (1) | |             |
A -> C (2) | | (1)     (4) |
B -> D (3) | \/           \/
C -> D (4) | B ----(3)---> D

#### Challenge 36

Input | Expected Output
----- | ---------------
A, B, C, D, E |
A -> B (1)    |
A -> C (2)    |
B -> D (3)    |
C -> D (4)    |
A -> E (5)    | [A, B, C, E, D]

#### Challenge 37

Input | Expected Output
----- | ---------------
A, B, C, D, E |
A -> B (1)    |
A -> C (2)    |
B -> D (3)    |
C -> D (4)    |
A -> E (5)    |
['C', 'D']    | True, 4

#### Challenge 38

Input | Expected Output
----- | ---------------
A, B, C, D, E |
A -> B (1)    |
A -> C (2)    |
B -> D (3)    |
C -> D (4)    |
A -> E (5)    | [A, B, D, C, E]

### Big O

#### Challenge 35

Time: O(N)  
Space: O(N)

#### Challenge 36

Time: O(N^2)
Space: O(N)

#### Challenge 37

Time: O(N^2)
Space: O(N)

#### Challenge 38

Time: O(N log(N))
Space: O(N)

### Change Log

1.2.5: *depth_first preliminary documentation mostly complete* - 05 Apr 2021
1.2: *get_edges challenge complete* - 01 Apr 2021
1.1.5: *get_edges whiteboard complete, working on code* - 31 Mar 2021
1.1: *Added breadth sort method* - 31 Mar 2021
1.0: *Challenge complee* - 30 Mar 2021
