import pytest
from .tree import Node, BinaryTree, BinarySearchTree


@pytest.fixture(scope='function')
def test_tree():
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

    return tree


def test_empty_tree():
    actual = BinarySearchTree()
    expected = None
    assert actual.root == expected


def test_single_Node():
    actual = BinarySearchTree(Node(1))
    expected = 1
    assert actual.root.value == expected


def test_children():
    actual = BinarySearchTree()
    actual.add(1)
    actual.add(0)
    actual.add(2)
    expected = [0, 2]
    assert [actual.root.left.value, actual.root.right.value] == expected


def test_preOrder(test_tree):
    assert test_tree.preOrder() == [28, 17, 4, 2, 16, 21, 34, 33, 67, 155]


def test_inOrder(test_tree):
    assert test_tree.inOrder() == [2, 4, 16, 17, 21, 28, 33, 34, 67, 155]


def test_postOrder(test_tree):
    assert test_tree.postOrder() == [2, 16, 4, 21, 17, 33, 155, 67, 34, 28]


def test_breadthFirst(test_tree):
    assert test_tree.breadthFirst() == [28, 17, 34, 4, 21, 2, 16, 33, 67, 155]


def test_find_maximum_value(test_tree):
    assert test_tree.find_maximum_value() == 155
