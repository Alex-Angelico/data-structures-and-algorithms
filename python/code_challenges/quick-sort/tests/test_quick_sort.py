import pytest
from quick_sort.quick_sort import quick_sort


@pytest.mark.parametrize(
    "test_lists, left, right, expected",
    [
        ([8, 4, 23, 42, 16, 15], 0, 5, [4, 8, 15, 16, 23, 42]),
        ([20, 18, 12, 8, 5, -2], 0, 5, [-2, 5, 8, 12, 18, 20]),
        ([5, 12, 7, 5, 5, 7], 0, 5, [5, 5, 5, 7, 7, 12]),
        ([2, 3, 5, 7, 13, 11], 0, 5, [2, 3, 5, 7, 11, 13])
    ]
)
def test_quick_sorting(test_lists, left, right, expected):
    actual = quick_sort(test_lists, left, right)
    assert actual == expected
