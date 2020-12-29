from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList


llist = LinkedList()


def test_empty_list():
    actual = llist.head
    expected = None
    assert actual == expected


def test_insert_list():
    llist.insert(4)
    actual = str(llist)
    expected = '{4} -> NULL'
    assert actual == expected


def test_head_link():
    actual = llist.head.data
    expected = 4
    assert actual == expected


llist_m = LinkedList()


def test_multiple_insert():
    llist_m.insert(3)
    llist_m.insert(6)
    llist_m.insert(10)
    actual = str(llist_m)
    expected = '{10} -> {6} -> {3} -> NULL'
    assert actual == expected


def test_find_value():
    actual = llist_m.includes(3)
    expected = True
    assert actual == expected


def test_no_value():
    actual = llist_m.includes(99)
    expected = False
    assert actual == expected


def test_list_output():
    actual = str(llist_m)
    expected = '{10} -> {6} -> {3} -> NULL'
    assert actual == expected


def test_append():
    llist_m.append(74)
    actual = str(llist_m)
    expected = '{10} -> {6} -> {3} -> {74} -> NULL'
    assert actual == expected


def test_multiple_append():
    llist_m.append(75)
    llist_m.append(76)
    actual = str(llist_m)
    expected = '{10} -> {6} -> {3} -> {74} -> {75} -> {76} -> NULL'
    assert actual == expected


def test_insert_before_middle():
    llist_m.insertBefore(3, 7)
    actual = str(llist_m)
    expected = '{10} -> {6} -> {7} -> {3} -> {74} -> {75} -> {76} -> NULL'
    assert actual == expected


def test_insert_before_first():
    llist_m.insertBefore(10, 128)
    actual = str(llist_m)
    expected = '{128} -> {10} -> {6} -> {7} -> {3} -> {74} -> {75} -> {76} -> NULL'
    assert actual == expected


def test_insert_after_middle():
    llist_m.insertAfter(74, 315)
    actual = str(llist_m)
    expected = '{128} -> {10} -> {6} -> {7} -> {3} -> {74} -> {315} -> {75} -> {76} -> NULL'
    assert actual == expected


def test_insert_after_last():
    llist_m.insertAfter(76, 22)
    actual = str(llist_m)
    expected = '{128} -> {10} -> {6} -> {7} -> {3} -> {74} -> {315} -> {75} -> {76} -> {22} -> NULL'
    assert actual == expected


def test_delete():
    llist_m.delete(75)
    actual = str(llist_m)
    expected = '{128} -> {10} -> {6} -> {7} -> {3} -> {74} -> {315} -> {76} -> {22} -> NULL'
    assert actual == expected


llist_b = LinkedList()
llist_b.insert(23)
llist_b.insert(98)
llist_b.insert(415)
llist_b.insert(123)
llist_b.insert(981)
llist_b.insert(454)
llist_b.insert(213)
llist_b.insert(198)
llist_b.insert(455)
llist_b.insert(253)
llist_b.insert(978)
llist_b.insert(45)
llist_b.insert(203)
llist_b.insert(918)
llist_b.insert(45)


def test_kth_overindex():
    actual = llist_b.kthFromEnd(25)
    expected = 'Target index value greater than list length.'
    assert actual == expected


def test_kth_equal():
    actual = llist_b.kthFromEnd(14)
    expected = 45
    assert actual == expected


def test_kth_negative():
    actual = llist_b.kthFromEnd(-5)
    # expected = 253
    expected = 'Target index value greater than list length.'
    assert actual == expected


def test_kth_happy():
    actual = llist_b.kthFromEnd(8)
    expected = 455
    assert actual == expected


llist_single = LinkedList()
llist_single.insert(13)


def test_kth_single():
    actual = llist_single.kthFromEnd(0)
    expected = 13
    assert actual == expected
