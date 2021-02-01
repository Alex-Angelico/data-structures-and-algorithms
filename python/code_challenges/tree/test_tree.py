import pytest
import tree


@pytest.fixture(scope='module')
def test_tree():
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

    return tree


def test_empty_tree():
    actual = BinarySearchTree()
    expected = None
    assert actual.root == expected
