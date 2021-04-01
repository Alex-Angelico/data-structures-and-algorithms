# Whiteboard

## Problem Domain

Write a function which takes in a graph of city names with edges weighed as plane ticket prices, and a list of city names. Return whether the trip between the cities is possible with direct flights, and how much it would cost.

## Edge Cases

Some set of the selected cities is not in the graph.

## Visualization

INPUT
Graph
A, B, C, D, E
A -> B (1)
A -> C (2)
B -> D (3)
C -> D (4)
A -> E (5)

City List
['C', 'D']

OUTPUT
True, 4

## Big O

Time: O(N^2)
Space: O(N)

## Algorithm

1. Create the function get_edges which accepts two arguments, a city graph and a city list.
2. Confirm that all cities in the list are in the graph. If not, raise an error.
3. Initialize a price variable.
4. Starting at the first city in the list, check if the following city is a neighbor in the graph of the preceding.
   i. If they are neighbors, add the edge weight between the two to the price variable.
   ii. If they are not neighbors, return False, $0.
5. Return True, $price.

## Pseudocode

```
define get_edges(graph, list):
  for index, city in enumerate(list):
    if city not in graph:
      raise KeyError
    else:
      list[index] = { city: city vertex object }
  price = 0

  i = 0
  while list[i+1]:
    route_check = graph.get_neighbors(list[i].value)
    if list[i+1].key in route_check.keys:
      add weight to price
    else return False

  return True, f'${price}'
```

## Code

```
define get_edges(route_graph, city_list):
  for index, city in enumerate(city_list):
    if city not in graph:
      raise KeyError('Vertex not in graph')
    else:
      list[index] = { city: city vertex object }
  price = 0

  i = 0
  while list[i+1]:
    route_check = graph.get_neighbors(list[i].value)
    if list[i+1].key in route_check.keys:
      add weight to price
    else return False

  return True, f'${price}'
```
