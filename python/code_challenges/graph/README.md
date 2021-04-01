# README

## Graph Implementaiton

### Author: Alex Angelico

### Problem Domain

#### Challenge 35

Create Graph, Vertex, and Edge classes which together allow for the construction and representation of various graphs.

#### Challenge 36

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
A, B, C, D |
A -> B (1) |
A -> C (2) |
B -> D (3) |
C -> D (4) |
A -> E (5) | [A, B, C, E, D]

### Big O

#### Challenge 35

Time: O(N)  
Space: O(N)

#### Challenge 36

Time: O(N^2)
Space: O(N)

### Change Log

1.1: *Added breadth sort method* - 31 Mar 2021
1.0: *Challenge complee* - 30 Mar 2021
