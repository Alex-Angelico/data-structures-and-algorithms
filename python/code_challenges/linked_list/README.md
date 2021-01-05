# README

## Linked List Implementation

### Author: Alex Angelico

### Contributors: Anothy Beaver, Logan Jones, Mason Fryberger, Sean Hawkins

### Problem Domain

Create a node calss that has properties for the value stored in the node and a pointer to the next node.

Create additional methods that allow for adding nodes to a linked list at selected locations.

Create an additional method that allows for selecting a node in a linked list by its index value.

### Inputs and Expected Outputs

#### Challenge 05

Input | Expected Output
----- | ---------------
[3, 6, 10], 3 | '{10} -> {6} -> {3} -> NULL', True
[None, 4], 99 | '{4} -> {None} -> NULL', False

#### Challenge 06

Input | Expected Output
----- | ---------------
head -> [1] -> [3] -> [2] -> NULL, 5 | head -> [1] -> [3] -> [2] -> [5] -> NULL
head -> [1] -> [3] -> [2] -> NULL, 3, 5 | head -> [1] -> [5] -> [3] -> [2] -> NULL
head -> [1] -> [2] -> [2] -> NULL, 2, 5 | head -> [1] -> [2] -> [5] -> [2] -> NULL

#### Challenge 07

Input | Expected Output
----- | ---------------
head -> [1] -> [3] -> [8] -> [2] -> NULL, 2 | 3

### Big O

#### Challenge 05

Time: O(1)  
Space: O(N)

#### Challenge 06

Time: O(1)  
Space: O(N)

#### Challenge 07

Time: O(N)  
Space: O(1)

### Whiteboards

#### Challenge 05

![Challenge 05 Whiteboard](../assets/linked-list.jpg)

#### Challenge 06

![Challenge 06 Whiteboard](../assets/linked-list-c06.jpg)

#### Challenge 07

![Challenge 07 Whiteboard](../assets/linked-list-c07.jpg)

### Change Log

1.2.1: Completed Challenge 07 Functionality - 23 Dec 2020
1.2: Completed Challenge 06 Functionality - 23 Dec 2020
1.1: Partly implemented append, insertBefore, insertAfter, and kthFromEnd functions - 22 Dec 2020
1.0: Completed Functionality - 19 Dec 2020
