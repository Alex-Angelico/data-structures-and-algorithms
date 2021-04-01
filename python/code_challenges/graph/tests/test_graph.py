import pytest
from graph.graph import Graph, Vertex, Edge


@pytest.fixture(scope='function')
def test_graph():
    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(a, e)
    graph.add_edge(e, f)
    graph.add_edge(e, g)
    graph.add_edge(f, h)

    return graph


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
    expected = [{'Value': 'b', 'Weight': 1}, {'Value': 'c', 'Weight': 2}]
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
    expected = [{'Value': 'a', 'Weight': 1}]
    assert actual == expected


def test_breadth_first(test_graph):
    assert test_graph.breadth_first(
        'a') == ['a', 'b', 'c', 'e', 'd', 'f', 'g', 'h']


def test_breadth_first_fail(test_graph):
    try:
        test_graph.breadth_first('i')
        assert False
    except KeyError:
        assert True
