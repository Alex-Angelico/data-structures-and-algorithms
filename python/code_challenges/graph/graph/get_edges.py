from graph.graph import Graph, Vertex, Edge


def get_edges(route_graph, city_list):
    for index, city in enumerate(city_list):
        i = 0
        for vertex in route_graph._adjacency_list:
            if city == vertex.value:
                city_list[index] = {'city': city, 'vertex': vertex}
                break
            i += 1
            if i == route_graph.size():
                raise KeyError(f'{city} has no flights connecting to it.')

    price = 0

    i = 0
    while i < len(city_list) - 1:
        route_check = route_graph.get_neighbors(city_list[i]['vertex'])
        j = 0
        for destination in route_check:
            if destination.get('Value') == city_list[i+1]['city']:
                price += destination['Weight']
                break
            # elif destination.get('Value') == city_list[-1]['city']:
            #     price += destination['Weight']
            #     i = len(city_list) - 1
            #     break
            j += 1
            if j == len(route_check):
                return False, '$0'
        i += 1

    return True, f'${price}'


if __name__ == '__main__':
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

    print(get_edges(cities, ['Arendelle', 'New Monstropolis', 'Naboo']))
    print(get_edges(cities, ['Metroville', 'Pandora']))
    print(get_edges(cities, ['Naboo', 'Pandora']))
    print(get_edges(cities, ['Narnia', 'Arendelle', 'Naboo']))
    print(get_edges(cities, ['Pandora', 'Metroville', 'Narnia', 'Naboo']))
