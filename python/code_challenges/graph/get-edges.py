from graph.graph import Graph, Vertex, Edge

define get_edges(route_graph, city_list):
    for index, city in enumerate(city_list):
        if city not in graph:
            raise KeyError('Vertex not in graph')
        else:
            list[index] = {city: city vertex object}
    price = 0

    i = 0
    while list[i+1]:
        route_check = graph.get_neighbors(list[i].value)
        if list[i+1].key in route_check.keys:
            add weight to price
        else return False

    return True, f'${price}'

if __name__ == '__main__':
    metroville = graph.add_node('Metroville')
    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    new_monstropolis = graph.add_node('New Monstropolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')
    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(metroville, new_monstropolis, 105)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(new_monstropolis, arendelle, 42)
    graph.add_edge(new_monstropolis, naboo, 73)
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(narnia, naboo, 250)
