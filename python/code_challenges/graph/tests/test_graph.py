import pytest
from graph.graph import Graph, Vertex, Edge


def test_create_vertex():
    actual = Vertex('a').value
    expected = 'a'
    assert actual == expected


def test_add_node():
    graph = Graph()
    actual = graph.add_node('a').value
    expected = 'a'
    assert actual == expected


def test_add_edge():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True


def test_get_nodes():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    actual = graph.get_nodes()
    expected = ['a', 'b']
    assert actual == expected


def test_get_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    expected = None
    assert actual == expected


def test_get_neighbors():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(a, c, 2)
    actual = graph.get_neighbors(a)
    expected = [{'b': 1}, {'c': 2}]
    assert actual == expected


def test_graph_size():
    graph = Graph()
    actual = graph.size()
    expected = 0
    assert actual == expected


def test_single_node_edge():
    graph = Graph()
    a = graph.add_node('a')
    graph.add_edge(a, a)
    actual = graph.get_neighbors(a)
    expected = [{'a': 1}]
    assert actual == expected
