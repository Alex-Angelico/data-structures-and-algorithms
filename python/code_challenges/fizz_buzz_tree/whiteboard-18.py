# Problem Domain
Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree. Set the values of each of the new nodes depending on the corresponding node value in the source tree.
# Edge Cases
Original tree has no nodes

# Visualization

#           / -> {1} < -\
# {2} < -- /      |      \- -> {3}
#                 |
#                {5}
#
#           / -> {1} < -\
# {2} < -- /      |      \- -> {Fizz}
#                 |
#               {Buzz}

# Big O
Time: O(N)
Space: O(N)

# Algorithm
1. Create a K_Node class with a constructor method.
2. Give the K_Node constructor an attribute that holds K number of nodes.
3. Create a K_AryTree class with a constructor
4. Add a fizz_buzz_tree method to the K_AryTree class.
5. In the fizz_buzz_tree method, check if the tree has a root.
6. If the tree has a root, determine its FizzBuzz value.
7. Else, return that the tree is empty.
8. Recursively traverse ever child of ever node to determine its FizzBuzz value.
9. Build a new tree with nodes with the FizzBuzz values of every node from the original tree, in the same order.
10. Return the new tree.


# Code


def fizz_buzz_tree(self):

    if self.root:
        if not self.root.value % 3 and not self.root.value % 5:
            self.root.value = 'FizzBuzz'
        elif not self.root.value % 3:
            self.root.value = 'Fizz'
        elif not self.root.value % 5:
            self.root.value = 'Buzz'
        else:
            self.root.value = str(self.root.value)
        fizz_buzz_tree = K_AryTree(self.root)
    else:
        return 'Empty tree'

    def traverse(node):
        child_values = []
        new_node = K_node(node.value)

        for number, child in enumerate(node.children):
            if not child.value % 3 and not child.value % 5:
                node.children[number].value = 'FizzBuzz'
            elif not child.value % 3:
                node.children[number].value = 'Fizz'
            elif not child.value % 5:
                node.children[number].value = 'Buzz'
            else:
                node.children[number].value = str(child.value)

            child_values.append(node.children[number].value)
            traverse(child)

        for i in range(len(child_values)):
            new_node.children.append(K_node(child_values[i]))

    traverse(self.root)
    return fizz_buzz_tree
