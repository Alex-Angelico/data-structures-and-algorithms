import pytest
from .fifo_animal_shelter import Node, AnimalShelter


def test_enqueue():
    q = AnimalShelter()
    q.enqueue("cat")
    actual = q.front.value
    expected = "cat"
    assert actual == expected


def test_dequeue():
    q = AnimalShelter()
    q.enqueue("cat")
    actual = q.dequeue("cat")
    expected = "cat"
    assert actual == expected


def test_enqueue_two():
    q = AnimalShelter()
    q.enqueue("dog")
    q.enqueue("cat")
    actual = q.front.value
    expected = "dog"
    assert actual == expected


def test_dequeue_preferred_animal():
    q = AnimalShelter()
    q.enqueue("dog")
    q.enqueue("cat")
    actual = q.dequeue("cat")
    expected = "cat"
    assert actual == expected


def test_animal_longest_dequeue():
    q = AnimalShelter()
    q.enqueue("dog")
    q.enqueue("cat")
    actual = q.dequeue()
    expected = "dog"
    assert actual == expected


def test_dequeue_none_animal():
    q = AnimalShelter()
    q.enqueue("dog")
    q.enqueue("cat")
    actual = q.dequeue("monkey")
    expected = None
    assert actual == expected
