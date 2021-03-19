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
