import pytest
from ..array_binary_search import brute_search, binary_search, rec_binary_search


def test_brute_search_in():
    actual = brute_search([4, 8, 15, 16, 23, 42, 64], 42)
    expected = 5
    assert actual == expected


def test_binary_search_in():
    actual = binary_search([4, 8, 15, 16, 23, 42, 64], 42)
    expected = 5
    assert actual == expected


def test_rec_binary_search_in():
    actual = rec_binary_search([4, 8, 15, 16, 23, 42, 64], 42)
    expected = 5
    assert actual == expected


def test_brute_search_out():
    actual = brute_search([11, 22, 33, 44, 55, 66, 77], 90)
    expected = -1
    assert actual == expected


def test_binary_search_out():
    actual = binary_search([11, 22, 33, 44, 55, 66, 77], 90)
    expected = -1
    assert actual == expected


def test_rec_binary_search_out():
    actual = rec_binary_search([11, 22, 33, 44, 55, 66, 77], 90)
    expected = -1
    assert actual == expected


def test_rec_binary_search_in_even():
    actual = rec_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
    expected = 8
    assert actual == expected
