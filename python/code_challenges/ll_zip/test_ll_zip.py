from ll_zip import zipLists
from linked_list import Node, LinkedList

llist_a, llist_b = LinkedList(), LinkedList()

llist_a.insert(23)
llist_a.insert(98)
llist_a.insert(415)
llist_a.insert(123)
llist_a.insert(981)
llist_a.insert(454)
llist_a.insert(213)

llist_b.insert(198)
llist_b.insert(455)
llist_b.insert(253)
llist_b.insert(978)
llist_b.insert(203)
llist_b.insert(918)
llist_b.insert(45)


def test_zip_lists_normal():
    zipped_list = zipLists(llist_a, llist_b)
    actual = str(zipped_list)
    expected = '{213} -> {45} -> {454} -> {918} -> {981} -> {203} -> {123} -> {978} -> {415} -> {253} -> {98} -> {455} -> {23} -> {198} -> NULL'
    assert actual == expected
