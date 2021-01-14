# README

## Queue with Stacks

### Author: Alex Angelico

### Problem Domain

Create a PseudoQueue class with standard queue interface (enqueue and dequeue) that internally uses two Stack() objects.

### Inputs and Expected Outputs

Input | Expected Output
----- | ---------------
enqueue(5) [10]->[15]->[20] | [5]->[10]->[15]->[20]
enqueue(5) --- | [5]
dequeue() [5]->[10]->[15]->[20] | 20
dequeue() [5]->[10]->[15] | 15

### Big O

Time: O(1)  
Space: O(1)

### Whiteboard

![Challenge 11 Whiteboard](../../assets/queue-with-stacks.jpg)

### Change Log

1.0: Functionality requirements complete - 13 Jan 2021
