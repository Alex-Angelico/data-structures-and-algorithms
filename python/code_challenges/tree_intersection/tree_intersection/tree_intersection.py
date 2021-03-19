# from tree import Node, QueueNode, Queue, BinaryTree, BinarySearchTree


def tree_intersection(tree1, tree2):
    list1 = tree1.inOrder()
    list2 = tree2.inOrder()

    common_list = []

    def commonality_checker(small_list, big_list):
        for i, value in enumerate(small_list):
            if small_list.count(value) > 1 and small_list.index(value) < i:
                pass
            elif big_list.count(value) > 0:
                common_list.append(value)

    if not len(list1) or not len(list2):
        return None
    elif list1 < list2:
        commonality_checker(list1, list2)
    else:
        commonality_checker(list2, list1)

    return common_list if common_list else None


if __name__ == '__main__':
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(4)
    tree1.add(2)
    tree1.add(5)

    tree2.add(2)
    tree2.add(1)
    tree2.add(4)

    print(tree_intersection(tree1, tree2))
