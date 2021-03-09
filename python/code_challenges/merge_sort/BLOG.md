# Documenting and Explaining Merge Sort

Merge sort is a sorting algorithm that uses recursion with a while loop in the helper function to first break a list into halves, and then iterate through the halves, rearranging their items in ascending order. The rearranged halves are then merged according to whichever half was completed first.

## Pseudocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

### Example Unsorted List

`[8,4,23,42,16,15]`

## Trace

left | right | new list
-----|-------|---------
[4] | [23] | [4, 23]
[8] | [4, 23] | [4, 8, 23]
[16] | [15] | [15, 16]
[42] | [15, 16] | [15, 16, 42]
[4, 8, 23] | [15, 16, 42] | [4, 8, 15, 16, 23, 42]

Sorted list: `[4, 8, 15, 16, 23, 42]`
