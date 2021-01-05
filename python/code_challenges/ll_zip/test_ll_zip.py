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
    actual = zipLists(llist_a, llist_b)
    expected = 213
    assert actual.data == expected
