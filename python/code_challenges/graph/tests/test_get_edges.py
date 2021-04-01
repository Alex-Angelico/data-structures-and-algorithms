import pytest
from graph.get_edges import get_edges
from graph.graph import Graph, Vertex, Edge


@pytest.mark.parametrize(
    "city_list, expected",
    [
        (['Arendelle', 'New Monstropolis', 'Naboo'], (True, '$115')),
        (['Metroville', 'Pandora'], (True, '$82')),
        (['Naboo', 'Pandora'], (False, '$0')),
        (['Narnia', 'Arendelle', 'Naboo'], (False, '$0')),
        (['Pandora', 'Metroville', 'Narnia', 'Naboo'], (True, '$369'))
    ]
)
def test_get_edges(test_cities_graph, city_list, expected):
    cities = Graph()
    metroville = cities.add_node('Metroville')
    pandora = cities.add_node('Pandora')
    arendelle = cities.add_node('Arendelle')
    new_monstropolis = cities.add_node('New Monstropolis')
    narnia = cities.add_node('Narnia')
    naboo = cities.add_node('Naboo')
    cities.add_edge(metroville, pandora, 82)
    cities.add_edge(pandora, metroville, 82)
    cities.add_edge(metroville, arendelle, 99)
    cities.add_edge(arendelle, metroville, 99)
    cities.add_edge(metroville, new_monstropolis, 105)
    cities.add_edge(new_monstropolis, metroville, 105)
    cities.add_edge(metroville, narnia, 37)
    cities.add_edge(narnia, metroville, 37)
    cities.add_edge(metroville, naboo, 26)
    cities.add_edge(naboo, metroville, 26)
    cities.add_edge(new_monstropolis, arendelle, 42)
    cities.add_edge(arendelle, new_monstropolis, 42)
    cities.add_edge(new_monstropolis, naboo, 73)
    cities.add_edge(naboo, new_monstropolis, 73)
    cities.add_edge(pandora, arendelle, 150)
    cities.add_edge(arendelle, pandora, 150)
    cities.add_edge(narnia, naboo, 250)
    cities.add_edge(naboo, narnia, 250)

    actual = get_edges(cities, city_list)
    assert actual == expected
