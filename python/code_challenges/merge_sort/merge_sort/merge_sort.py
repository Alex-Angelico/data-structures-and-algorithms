def merge_sort(arr):
    n = len(arr)

    def Merge(left, right, arr):
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        if i == len(left):
            for item in right[j:]:
                arr[k] = item
                k += 1
        else:
            for item in left[i:]:
                arr[k] = item
                k += 1

    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        merge_sort(left)
        merge_sort(right)
        Merge(left, right, arr)

    return arr


if __name__ == '__main__':
    ulist = [8, 4, 23, 42, 16, 15]
    print(merge_sort(ulist))
