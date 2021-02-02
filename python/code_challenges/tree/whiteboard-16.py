# Problem Domain
Extend the binary tree class with a funciton that returns the highest value in a tree.
# Edge Cases
Tree has no nodes

# Visualization

#           / -> {1} < -\
# {2} < -- /      |      \- -> {3}
#  |______________|_____________|
#  |
[1, 2, 3] - ---- -> 3 is max_value value

# Big O
Time: O(N)
Space: O(1)

# Algorithm
1. Create a method within BinaryTree called find_maximum_value() that takes no arguments.
2. Within the method, use one of BinaryTree's traversal methods to return a list of values from the tree.
3. Iterate through the list, comparing each value to the one before to determine which is larger.
4. Retain the largest value.
5. Return the value.

# Pseudocode
# define find_maximum_value
#   create a variable that is assigned an instance of a traversal method for the tree
#   create a variable assigned an integer value of 0.
#   for ever element in the list variable
#     check if it is larger than the integer variable
#     if it's larger, it is assigned to the integer variable
#   return the integer variable

# Code


def find_maximum_value(self):
    max_value = 0
    tree_values = self.preOrder()
    for value in tree_values:
        if value > max_value:
            max_value = value
    return max_value
