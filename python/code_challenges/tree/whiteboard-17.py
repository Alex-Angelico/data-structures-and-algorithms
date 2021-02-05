# Problem Domain
Extend the binary tree class with a funciton that traverses a tree object using the breadth-first approach.
# Edge Cases
Tree has no nodes

# Visualization

#           / -> {1} < -\
# {2} < -- /      |      \- -> {3}
#  |______________|_____________|
#  |
[1, 2, 3]

# Big O
Time: O(N)
Space: O(1)

# Algorithm
1. Create a method within BinaryTree called breadthFirst() that takes no arguments.
2. Us an appropriate configuration of loops and conditionals that cycles through each node in the tree breadth-first.
3. Append node values to a list.
4. Return the list.

# Pseudocode
# define breadthFirst method
#   create a node_list variable that is an empty list
#   append the root vaue of the tree to node_list
#   define traverse helper function that accepts a root node
#     if root.left and/or root.right exist, and add their values in order
#     if root.left and/or root.right exist, traverse them in order
#   traverse(self.root)
#   return node_list

# Code


def breadthFirst(self):
    node_list = []

    node_list.append(self.root.value)

    def traverse(root):

        if root.left:
            node_list.append(root.left.value)

        if root.right:
            node_list.append(root.right.value)

        if root.left:
            traverse(root.left)

        if root.right:
            traverse(root.right)

    traverse(self.root)
    return node_list
