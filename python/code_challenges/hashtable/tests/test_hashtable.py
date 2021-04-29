from hashtable.hashtable import Hashtable
from hashtable.linked_list import LinkedList
import pytest

def test_create():
    hashtable = Hashtable()
    assert hashtable


def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('spam')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable._size


def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary


def test_null_key():
    hashtable = Hashtable()
    actual = hashtable.get('alpha')
    expected = None
    assert actual == expected


def test_key_retrieve_value():
    hashtable = Hashtable()
    hashtable.add('alpha', 'test_value')
    actual = hashtable.get('alpha')
    expected = 'test_value'
    assert actual == expected


def test_key_retrieve_value_collision():
    hashtable = Hashtable()
    hashtable.add('listen', 'test_value')
    hashtable.add('silent', 'other_value')
    actual = hashtable.get('silent')
    expected = 'other_value'
    assert actual == expected
