# Whiteboard

## Problem Domain

Create a function that LEFT JOINs two hashmaps into a single data structure.

## Edge Cases

One or both hashmaps is empty.

## Visualization

INPUT
Synonyms { 'fond':'enamored', 'wrath':'anger', 'diligent':'employed', 'outfit':'garb', 'guide':'usher' }  
Antonyms { 'fond':'averse', 'wrath':'delight', 'diligent':'idle', 'guide':'follow', 'flow':'jam' }  

OUTPUT
[ ['fond','enamored','averse'], ['wrath','anger','delight',], ['diligent','employed','idle'], ['outfit','garb',NULL], ['guide','usher','follow'] ]

## Big O

Time: O(N)  
Space: O(N)

## Algorithm

1. Define a function called left_joiner with two hashmap parameters (left and right).
2. Initialize an empty list called joined_data.
3. Iterate through all the key/value pairs in the left hashmap.
4. Create a list for each key/value pair, appending both the key and the value.
5. get() each key from the left hashmap in the right hashmap.
6. Append whatever is returned by the get() function to the key/value list, whether it is a value or None.
7. Append the key/value list to joined_data.
8. When iteration is complete, return joined_data.

## Pseudocode

left_joiner(left, right)
  joined_data = []
  for bucket in left._buckets:
    if bucket:
      current = bucket.head
      while current:
        left_column = [ current.data[0], current.data[1] ]
        right_value = right.get(current.data[0])
        left_column.append(right_value)
        current = current.next
      joined_data.append(left_column)
  return joined_data

## Code

```
def left_joiner(left, right):
  joined_data = []
  for bucket in left._buckets:
    if bucket:
      current = bucket.head
      while current:
        left_column = [ current.data[0], current.data[1] ]
        right_value = right.get(current.data[0])
        left_column.append(right_value)
        current = current.next
      joined_data.append(left_column)
  return joined_data
```

## Verification

Index | Hashmap1 | Hashmap2
------|----------|----------------
8     | NULL | ('flow', 'jam')
...   | ... | ...
45    | ('outfit', 'garb') | NULL
...   | ... | ...
48    | ('diligent', 'employed') | ('diligent', 'idle')
...   | ... | ...
65    | ('fond', 'enamored) | ('fond', 'averse')
66    | ('guide', 'usher') | ('guide', 'follow')
...   | ... | ...
106   | ('wrath', 'anger') | ('wrath', 'delight')

Hashmap1._buckets = [45, ... 48, ... 65, 66, ... 106]
joined_data = []

if 45:
  current = 45.head
  while head:
    left_column =[ head.key ('outfit'), head.value ('garb')]
    right_value = right.get(head.key ('outfit')) = 'NULL'
    left_column.append('NULL')
  joined_data.append(['outfit', 'garb', 'NULL'])

joined_data = [ ['outfit', 'garb', 'NULL'] ]

if 48:
  current = 48.head
  while head:
    left_column =[ head.key ('diligent'), head.value ('employed')]
    right_value = right.get(head.key ('diligent')) = 'idle'
    left_column.append('idle')
  joined_data.append(['diligent', 'garb', 'employed'])

joined_data = [ ['outfit', 'garb', 'NULL'], ['diligent', 'garb', 'employed'] ]

if 65:
  current = 65.head
  while head:
    left_column =[ head.key ('fond'), head.value ('enamored')]
    right_value = right.get(head.key ('fond')) = 'averse'
    left_column.append('averse')
  joined_data.append(['fond', 'enamored', 'averse'])

joined_data = [ ['outfit', 'garb', 'NULL'], ['diligent', 'garb', 'employed'], ['fond', 'enamored', 'averse'] ]

if 66:
  current = 66.head
  while head:
    left_column =[ head.key ('guide'), head.value ('usher')]
    right_value = right.get(head.key ('guide')) = 'follow'
    left_column.append('follow')
  joined_data.append(['guide', 'usher', 'follow'])

joined_data = [ ['outfit', 'garb', 'NULL'], ['diligent', 'garb', 'employed'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'] ]

if 106:
  current = 106.head
  while head:
    left_column =[ head.key ('wrath'), head.value ('anger')]
    right_value = right.get(head.key ('wrath')) = 'delight'
    left_column.append('delight')
  joined_data.append(['wrath', 'anger', 'delight'])

joined_data = [ ['outfit', 'garb', 'NULL'], ['diligent', 'garb', 'employed'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'] ]