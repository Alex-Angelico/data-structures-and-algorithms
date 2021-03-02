class K_node:
    def __init__(self, value):
        self.value = value
        self.children = []


class K_AryTree:
    def __init__(self, root=None):
        self.root = root

    def fizz_buzz_tree(self):
        # print('Function initialization:', self)
        fb_node_values = []
        if self.root:
            # root_clone = K_AryTree.fizz_buzz_eval(self.root)
            # fizz_buzz_tree = K_AryTree(K_AryTree.fizz_buzz_eval(self.root))
            # fizz_buzz_tree = K_AryTree(K_node(root_clone.value))
            fb_root = K_AryTree.fizz_buzz_eval(K_node(self.root.value))
            fizz_buzz_tree = K_AryTree(fb_root)
            # print('ORIGINAL ROOT:', self.root, self.root.value)
            # print('FB ROOT:', fizz_buzz_tree.root, fizz_buzz_tree.root.value)
        else:
            return 'Empty tree'
        # print('New tree creation:', self)
        # print(fizz_buzz_tree.root.children[1].value)

        # def traverse(node):
        #     fb_node_values.append(node.value)
        #     child_values = []
        #     new_node = K_node(node.value)

        #     for child in node.children:
        #         child = K_AryTree.fizz_buzz_eval(child)
        #         child_values.append(child.value)
        #         traverse(child)

        #     for i in range(len(child_values)):
        # print('z')
        #         new_node.children.append(K_node(child_values[i]))
        # print(new_node.children)

        def traverse(node):
            fb_node_values.append(node.value)
            # child_values = []
            # new_node = K_node(node.value)
            new_node = K_node(node.value)

            for child in node.children:
                # new_child_node = K_node(child.value)
                # new_child_node = K_AryTree.fizz_buzz_eval(new_child_node)
                new_child_node = K_AryTree.fizz_buzz_eval(K_node(child.value))
                new_node.children.append(new_child_node)
                # print(new_child_node.value)
                # child_values.append(new_child_node.value)
                # for i in range(len(child_values)):
                #     new_node.children.append(K_node(child_values[i]))
                traverse(child)

            if node == self.root:
                print('THRESHOLD 0')
                for new_child in new_node.children:
                    print('THRESHOLD 1')
                    fizz_buzz_tree.root.children.append(new_child)
                    # print(new_child.value, new_child.children[0].value)

            # print(f"""
            # {fizz_buzz_tree.root.value}
            # {fizz_buzz_tree.root.children[0].value} {fizz_buzz_tree.root.children[1].value} {fizz_buzz_tree.root.children[2].value}
            # {fizz_buzz_tree.root.children[0].children[0].value} {fizz_buzz_tree.root.children[0].children[1].value} {fizz_buzz_tree.root.children[0].children[2].value}
            # {fizz_buzz_tree.root.children[1].children[0].value} {fizz_buzz_tree.root.children[1].children[1].value} {fizz_buzz_tree.root.children[1].children[2].value}
            # {fizz_buzz_tree.root.children[2].children[0].value} {fizz_buzz_tree.root.children[2].children[1].value} {fizz_buzz_tree.root.children[2].children[2].value}
            # """)

        traverse(self.root)
        # print('Traversal execution:', self)
        return fizz_buzz_tree, fb_node_values

    @staticmethod
    def fizz_buzz_eval(item):
        if not item.value % 15:
            item.value = 'FizzBuzz'
        elif not item.value % 3:
            item.value = 'Fizz'
        elif not item.value % 5:
            item.value = 'Buzz'
        else:
            item.value = str(item.value)

        return item


if __name__ == '__main__':
    node_alpha = K_node(3)
    node_bravo = K_node(4)
    node_charlie = K_node(5)
    node_delta = K_node(6)
    node_echo = K_node(7)
    node_foxtrot = K_node(8)
    node_golf = K_node(9)
    node_hotel = K_node(10)
    node_india = K_node(11)
    node_juliet = K_node(12)
    node_kilo = K_node(13)
    node_lima = K_node(14)
    node_mike = K_node(15)

    node_alpha.children.append(node_bravo)
    node_alpha.children.append(node_charlie)
    node_alpha.children.append(node_delta)

    node_bravo.children.append(node_echo)
    node_bravo.children.append(node_foxtrot)
    node_bravo.children.append(node_golf)

    node_charlie.children.append(node_hotel)
    node_charlie.children.append(node_india)
    node_charlie.children.append(node_juliet)

    node_delta.children.append(node_kilo)
    node_delta.children.append(node_lima)
    node_delta.children.append(node_mike)

    test_K_tree = K_AryTree(node_alpha)
    # print(test_K_tree)
    # print(f"""
    # {test_K_tree.root.value}
    # {test_K_tree.root.children[0].value} {test_K_tree.root.children[1].value} {test_K_tree.root.children[2].value}
    # {test_K_tree.root.children[0].children[0].value} {test_K_tree.root.children[0].children[1].value} {test_K_tree.root.children[0].children[2].value}
    # {test_K_tree.root.children[1].children[0].value} {test_K_tree.root.children[1].children[1].value} {test_K_tree.root.children[1].children[2].value}
    # {test_K_tree.root.children[2].children[0].value} {test_K_tree.root.children[2].children[1].value} {test_K_tree.root.children[2].children[2].value}
    # """)

    fb_tree, fb_node_values = test_K_tree.fizz_buzz_tree()

    print(test_K_tree)
    print(f"""
    {test_K_tree.root.value}
    {test_K_tree.root.children[0].value} {test_K_tree.root.children[1].value} {test_K_tree.root.children[2].value}
    {test_K_tree.root.children[0].children[0].value} {test_K_tree.root.children[0].children[1].value} {test_K_tree.root.children[0].children[2].value}
    {test_K_tree.root.children[1].children[0].value} {test_K_tree.root.children[1].children[1].value} {test_K_tree.root.children[1].children[2].value}
    {test_K_tree.root.children[2].children[0].value} {test_K_tree.root.children[2].children[1].value} {test_K_tree.root.children[2].children[2].value}
    """)

    print(fb_tree)
    print(f"""
    {fb_tree.root.value}
    {fb_tree.root.children[0].value} {fb_tree.root.children[1].value} {fb_tree.root.children[2].value}
    {fb_tree.root.children[0].children[0].value} {fb_tree.root.children[0].children[1].value} {fb_tree.root.children[0].children[2].value}
    {fb_tree.root.children[1].children[0].value} {fb_tree.root.children[1].children[1].value} {fb_tree.root.children[1].children[2].value}
    {fb_tree.root.children[2].children[0].value} {fb_tree.root.children[2].children[1].value} {fb_tree.root.children[2].children[2].value}
    """)

    print(fb_node_values)
