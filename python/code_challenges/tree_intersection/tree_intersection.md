# Whiteboard

## Problem Domain

Create a function that will generate a list of common values in two binary trees.

## Edge Cases

No common values.

One or both trees are empty.

## Visualization

INPUT
tree1: {2} <---> {4} <---> {5}
tree2: {1} <---> {2} <---> {4}

values from searching tree1: [2, 4, 5]
values from searching tree2: [1, 2, 4]

OUTPUT
common values after comparing both tree lists: [2, 4]

## Big O

Time: O(log(n))  
Space: O(n)

## Algorithm

1. Create a function called tree_intersection that accepts two binary trees as arguments.
2. If one or both trees is empty, return None.
3. Traverse each tree, creating a list of the value in each.
4. Iterate through the smaller list.
    i. For each value, check if it is a duplicate that has already been checked.
   ii. Check if the value is also present in the larger list.
5. Return a list of common values.

## Pseudocode

def tree_intersection(tree1, tree2):
  list1 = tree1.inOrder()
  list2 = tree2.inOrder()

  for whichever list is smaller:
    check smaller_list[i] against other smaller_list values for duplication
    check smaller_list[i] against larger_list values for commonality
      if common value is detected, append  value to common_list

  return common_list

## Code

```
def tree_intersection(tree1, tree2):
  list1 = tree1.inOrder()
  list2 = tree2.inOrder()

  common_list =[]

  def commonality_checker(small_list, big_list):
    for i, value in enumerate(small_list):
      if small_list.count(value) > 1 and small_list.index(value) < i: pass
      elif big_list.count(value) > 0: common_list.append(value)

  if list1 < list2: commonality_checker(list1, list2)
  else: commonality_checker(list2, list1)

  return common_list
```

## Verification

