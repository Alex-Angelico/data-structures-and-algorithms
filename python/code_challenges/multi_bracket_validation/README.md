# README

## Multi-bracket Validation

### Author: Alex Angelico

### Problem Domain

Create a function that accepts a string argument and returns a boolean representing whether or not the brackets in the string are balanced.

### Inputs and Expected Outputs

Input | Expected Output
----- | ---------------
{} | TRUE
{}(){} | TRUE
()[[Extra Characters]] | TRUE
(){}[[]] | TRUE
{}{Code}[Fellows](()) | TRUE
[({}] | FALSE
(]( | FALSE
{(}) | FALSE

### Big O

Time: O(N)  
Space: O(1)

### Whiteboard

![Challenge 13 Whiteboard](../../assets/multi-bracket-validation.jpg)

### Change Log

1.0: Created readme and whiteboard - 18 Jan 2021
