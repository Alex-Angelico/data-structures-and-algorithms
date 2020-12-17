# BRUTE FORCE


def brute_search(list, search_key):
    i = 0
    while i < len(list):
        if list[i] == search_key:
            return i
        i = i + 1

    return -1

# ITERATIVE


def binary_search(sorted_list, integer_value):
    start = 0
    end = len(sorted_list) - 1

    while start < end:
        midpoint = start + (end - start) // 2

        if sorted_list[midpoint] == integer_value:
            return midpoint
        elif sorted_list[midpoint] > integer_value:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return -1

# RECURSIVE


def rec_binary_search(sorted_list: list, search_int: int) -> int:
    def helper(start_idx: int, end_idx: int) -> int:
        if start_idx >= end_idx:
            return -1
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if sorted_list[mid_idx] == search_int:
            return mid_idx
        elif sorted_list[mid_idx] > search_int:
            return helper(start_idx, mid_idx - 1)
        else:
            return helper(mid_idx + 1, end_idx)
    return helper(0, len(sorted_list) - 1)

# DRAFTS


# def BinarySearch(sorted_list, integer_value):
#     length = len(sorted_list)
#     midpoint = length // 2
#     midpoint_value = sorted_list[midpoint]
#     list_1 = sorted_list[:midpoint]
#     list_2 = sorted_list[midpoint:]

#     print(list_1, list_2)

#     if midpoint_value == integer_value:
#         original_list = list_1 + list_2
#         index = original_list.index(midpoint_value)
#         return index, sorted_list
#         #   return midpoint
#     elif length <= 1 and sorted_list[0] != integer_value:
#         return -1
#     elif midpoint_value > integer_value:
#         return BinarySearch(list_1, integer_value)
#     elif midpoint_value < integer_value:
#         return BinarySearch(list_2, integer_value)


# search_return, reconstituted_list = BinarySearch(list, integer)
# search_return, reconstituted_list = BinarySearch(list_alt, integer_alt)
# print('SEARCH RETURN:', type(search_return), search_return, 'RECONSTITUTED LIST:', reconstituted_list)

# search_return = BinarySearch(list, integer)
# search_return = BinarySearch(list_alt, integer_alt)
# print('SEARCH RETURN:', type(search_return), search_return)

# output = BruteSearch(list, integer)
# print(output)

# , f'tracking: {list_1 + list_2}'
# , f'tracking: {list_1 + list_2}'

# def BinarySearch(sorted_list, integer_value):
#     original_length = len(sorted_list) - 1
#     length = len(sorted_list)
#     midpoint = length // 2
#     midpoint_value = sorted_list[midpoint]
#     while length > 1:
#         if midpoint_value == integer_value:
#             return midpoint + (midpoint - original_length)
#         elif midpoint_value > integer_value:
#             sorted_list = sorted_list[:midpoint]
#             length = len(sorted_list)
#             midpoint = length // 2
#             midpoint_value = sorted_list[midpoint]
#         elif midpoint_value < integer_value:
#             sorted_list = sorted_list[midpoint:]
#             length = len(sorted_list)
#             midpoint = length // 2
#             midpoint_value = sorted_list[midpoint]
#     return -1
