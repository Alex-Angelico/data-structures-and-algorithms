def insertion_sort(nlist):
    for i in range(1, len(nlist)):
        j = i - 1
        temp = nlist[i]

        while j >= 0 and temp < nlist[j]:
            nlist[j + 1], nlist[j] = nlist[j], nlist[i]
            j = j - 1

        nlist[j + 1] = temp

    return nlist


if __name__ == '__main__':
    ulist = [8, 4, 23, 42, 16, 15]
    print(insertion_sort(ulist))
