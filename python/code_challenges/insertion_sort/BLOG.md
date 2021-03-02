# Documenting and Explaining Insertion Sort

Insertion sort is a sorting algorithm that uses a nested for -> while loop to iterate through the elements in a list and check each one against preceding elements to compare which is larger. The traversal holds a given element until it is larger than the preceing element, gradually building an ascending sorted list from the front.

## Pseudocode
```
InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp
```

### Example Unsorted List

`[8,4,23,42,16,15]`

## Trace

### i = 1

i | j | temp
--|---|-----
1 | 0 | 4


 j i
[8,4,23,42,16,15]
   ^
  temp
   j i
[4,8,23,42,16,15]
     ^
    temp 

## Trace

### i = 2

i | j | temp
--|---|-----
1 | 0 | 4
2 | 1 | 23