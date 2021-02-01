class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preOrder(self):
        node_list = []

        def traverse(root):
            node_list.append(root.value)
            if root.left:
                traverse(root.left)

            if root.right:
                traverse(root.right)

        traverse(self.root)
        return node_list

    def inOrder(self):
        node_list = []

        def traverse(root):
            if root.left:
                traverse(root.left)
            node_list.append(root.value)

            if root.right:
                traverse(root.right)

        traverse(self.root)
        return node_list

    def postOrder(self):
        node_list = []

        def traverse(root):
            if root.left:
                traverse(root.left)

            if root.right:
                traverse(root.right)
            node_list.append(root.value)

        traverse(self.root)
        return node_list


class BinarySearchTree(BinaryTree):
    # def add(self, value):
    #     if value < self.root.value:

    def contains(self, value):
        presence = False

        def traverse(root):
            # presence = False
            print(value, root.value)
            if value == root.value:
                presence = True
                return presence
            if value < root.value and root.left:
                traverse(root.left)
            if value > root.value and root.right:
                traverse(root.right)

        traverse(self.root)
        # if value == self.root.value:
        #     return True
        # else:
        #     return False
        return presence
        # return False


if __name__ == '__main__':
    tree = BinarySearchTree()
    a = Node(28)
    b = Node(17)
    c = Node(34)
    d = Node(4)
    e = Node(21)
    f = Node(33)
    g = Node(67)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    tree.root = a

print(tree.preOrder())
print(tree.inOrder())
print(tree.postOrder())

# tree.add(1)
print(tree.contains(34))

# a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")
# e = Node("E")
# f = Node("F")
# g = Node("G")
