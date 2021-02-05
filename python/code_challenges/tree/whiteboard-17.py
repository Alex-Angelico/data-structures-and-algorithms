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
2. Create a node_list to hold node values.
3. Create a node_queue to hold nodes.
4. Make the roote node current.
5. If current is empty, return 'Empty tree'.
6. Enqueue current to node_queue.
7. While there is a current node, dequeue the current node and append its value to node_list.
8. Check for current.left and current.right nodes, and enqueue them in that order.
9. If node_queue is empty, break the loop and return node_list.


# Pseudocode


# define breadthFirst method
#   create a node_list variable that is an empty list
#   creat a node_queue variable that is an empty queue
#   current = self.root
#   if current is none: return 'Empty tree'
#   node_queue.enqueue(current)
#   while there is a current node:
#     if root.left and/or root.right exist, enqueue them in node_queue in that order
#     if node_queue.is_empty(): break
#   return node_list

# Code


def breadthFirst(self):
    node_list = []
    node_queue = Queue()
    current = self.root
    if current == None:
        return 'Empty tree'

    node_queue.enqueue(current)

    while current:
        current = node_queue.dequeue()
        node_list.append(current.value)
        if current.left:
            node_queue.enqueue(current.left)
        if current.right:
            node_queue.enqueue(current.right)
        if node_queue.is_empty():
            break

    return node_list
