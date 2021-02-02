# Problem Domain
Create a binary tree class with traversal methods, and a binary search tree subclass with methods to add and search for nodes with designated values. Additionally create an associated node class.

# Edge Cases
Tree has no nodes
BST receives non-numerical search input

# Visualization
Root: {1} Left: {2} Right: {3}

#           / -> {1} < -\
# {2} < -- /             \- -> {3}

# Big O
Binary Tree
Time: O(N)
Space: O(1)
BST
Time: O(log(N))
Space: O(1)

# Algorithm
1.Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
2. Create a BinaryTree class with methods for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
3. For each method an appropriate configuration of loops and conditional should be used to traverse nodes in the tree reflecting the principles of preOrder, inOrder, and postOrder.
4.Create a BinarySearchTree class with two methods.
5.The first method is named add. It accepts a value, and adds a new node with that value in the correct location in the binary search tree.
6. If the value provided is not numeric, return a custom error message.
7. The second method is named contains. It accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
8. If no node containing the provided value exists, return a custom error message.

# Pseudocode


class Node


define constructor with value, left, and right properties(all defaulting to None)


class BinaryTree


define construtor with root property defaulting to None

# define preOrder method
#   create a node_list variable that is an empty list
#   define traverse helper function that accepts a root node
#     append the root value to node_list
#       check if root.left is not None
#         traverse(root.left)

#       check if root.right is not None
#         traverse(root.right)

#   traverse(self.root)
#   return node_list

# define inOrder method
#   create a node_list variable that is an empty list
#   define traverse helper function that accepts a root node

#        check if root.left is not None
#           traverse(root.left)
#         append the root value to node_list

#         check if root.right is not None
#           traverse(root.right)

#   traverse(self.root)
#   return node_list

# define postOrder method
#   create a node_list variable that is an empty list
#   define traverse helper function that accepts a root node

#        check if root.left is not None
#           traverse(root.left)

#         check if root.right is not None
#           traverse(root.right)
#         append the root value to node_list

#   traverse(self.root)
#   return node_list


# class BinarySearchTree (subclass of BinaryTree)

#    define add method with value property
#       try
#         assert that an numerical input was passed as an argument to value
#       except
#         return ValueError
#       create a new Node with the value property
#
#    define add method with value property
#       try
#         assert that an numerical input was passed as an argument to value
#       except
#         return ValueError
#
