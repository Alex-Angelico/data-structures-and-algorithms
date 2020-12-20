from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList


llist = LinkedList()


def test_empty_list():
    actual = llist.insert(Node())
    value = None
    assert actual == value


def test_insert_list():
    actual = llist.insert(Node(4))
    value = None
    assert actual == value


def test_head_link():
    actual = str(llist)
    value = '{4} -> {None} -> NULL'
    assert actual == value


llist_m = LinkedList()


def test_multiple_insert():
    llist_m.insert(Node(3))
    llist_m.insert(Node(6))
    llist_m.insert(Node(10))
    actual = str(llist_m)
    value = '{10} -> {6} -> {3} -> NULL'
    assert actual == value


def test_find_value():
    actual = llist_m.includes(3)
    value = True
    assert actual == value


def test_no_value():
    actual = llist_m.includes(99)
    value = False


def test_list_output():
    actual = str(llist_m)
    value = '{10} -> {6} -> {3} -> NULL'
    assert actual == value
