import pytest
# from .queue_with_stacks import PseudoQueue
from .stacks_and_queues import PseudoQueue, Node, Stack, InvalidOperationError


def test_enqueue():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.read_stack.top.value
    expected = "apple"
    assert actual == expected


def test_dequeue():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


def test_enqueue_two():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.read_stack.top.next.value
    expected = "apples"
    assert actual == expected


def test_dequeue_when_full():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


def test_peek_post_dequeue():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.read_stack.peek()
    expected = "bananas"
    assert actual == expected
