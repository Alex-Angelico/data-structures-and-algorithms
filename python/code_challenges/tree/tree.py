class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # @property
    # def value(self):
    #     return self.value

    # @value.setter
    # def value(self, input):
    #     if not str(input).isnumeric():
    #         raise Exception("Numeric value required for node value.")
    #     else:
    #         self.value = input


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

    def find_maximum_value(self):
        max_value = 0
        tree_values = self.preOrder()
        for value in tree_values:
            if value > max_value:
                max_value = value
        return max_value


class BinarySearchTree(BinaryTree):
    def add(self, value):
        new_leaf = Node(value)
        current = self.root
        if current == None:
            self.root = new_leaf
            return

        while current:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    break
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    break
            if value == current.value:
                return 'Tree already contains this value.'

        if value < current.value:
            current.left = new_leaf
        if value > current.value:
            current.right = new_leaf

    def contains(self, value):
        current = self.root
        if value == current.value:
            return True

        while current:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    break
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    break
            if value == current.value:
                return True

        return False


if __name__ == '__main__':
    tree = BinarySearchTree()

    tree.add(28)
    tree.add(17)
    tree.add(34)
    tree.add(4)
    tree.add(21)
    tree.add(33)
    tree.add(67)
    tree.add(155)
    tree.add(16)
    tree.add(2)

    print(tree.contains(29))

    print(tree.preOrder())
    print(tree.inOrder())
    print(tree.postOrder())
    print(tree.breadthFirst())
