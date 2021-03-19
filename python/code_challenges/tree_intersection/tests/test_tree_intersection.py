import pytest
from tree_intersection.tree_intersection import tree_intersection
from tree_intersection.tree import Node, QueueNode, Queue, BinaryTree, BinarySearchTree


def test_normal_trees():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(4)
    tree1.add(2)
    tree1.add(5)

    tree2.add(2)
    tree2.add(1)
    tree2.add(4)

    actual = tree_intersection(tree1, tree2)
    expected = [2, 4]
    assert actual == expected


def test_uncommon_trees():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(4)
    tree1.add(2)
    tree1.add(5)

    tree2.add(3)
    tree2.add(1)
    tree2.add(7)

    actual = tree_intersection(tree1, tree2)
    expected = None
    assert actual == expected


def test_one_tree_empty():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(4)
    tree1.add(2)
    tree1.add(5)

    actual = tree_intersection(tree1, tree2)
    expected = None
    assert actual == expected


def test_both_trees_empty():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    actual = tree_intersection(tree1, tree2)
    expected = None
    assert actual == expected


def test_huge_trees():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(28)
    tree1.add(17)
    tree1.add(34)
    tree1.add(4)
    tree1.add(21)
    tree1.add(33)
    tree1.add(67)
    tree1.add(155)
    tree1.add(16)
    tree1.add(2)

    tree2.add(17)
    tree2.add(16)
    tree2.add(2)
    tree2.add(67)
    tree2.add(39)
    tree2.add(8)
    tree2.add(3)
    tree2.add(94)

    actual = tree_intersection(tree1, tree2)
    expected = [2, 16, 17, 67]
    assert actual == expected
