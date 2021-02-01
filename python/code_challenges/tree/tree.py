class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, input):
        if not str(input).isnumeric():
            raise Exception("Numeric value required for node value.")
        else:
            self.value = input


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
    def add(self, value):
        new_leaf = Node(value)
        current = self.root
        while current.left or current.right:
            if current.left and value < current.value:
                current = current.left
            if current.right and value > current.value:
                current = current.right
            if value == current.value:
                return 'Tree already contains this value.'

        if value < current.value:
            current.left = new_leaf
        if value > current.value:
            current.right = new_leaf

    def contains(self, value):
        current = self.root
        while current.left or current.right:
            if value < current.value:
                current = current.left
            if value > current.value:
                current = current.right
            if value == current.value:
                return True
        return False


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

    tree.add(155)
    print(tree.contains(155))

    print(tree.preOrder())
    print(tree.inOrder())
    print(tree.postOrder())
