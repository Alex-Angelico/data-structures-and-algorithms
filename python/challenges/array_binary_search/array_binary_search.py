list = [4,8,15,16,23,42]
integer = 15

list_alt = [11,22,33,44,55,66,77]
integer_alt = 90

# def BruteSearch(list, search_key):
#   i = 0
#   while i < len(list):
#     if list[i] == search_key:
#       return i
#     i = i + 1
 
#   return -1

def BinarySearch(sorted_list, integer_value):
  length = len(sorted_list)
  midpoint = length // 2
  midpoint_value = sorted_list[midpoint]
  list_1 = sorted_list[0:midpoint]
  list_2 = sorted_list[midpoint:length]

  print(list_1, list_2)

  if midpoint_value == integer_value:
      return midpoint
  elif length == 1 and sorted_list[0] != integer_value:
      return -1    
  elif midpoint_value > integer_value:
      return BinarySearch(list_1, integer_value), list_1 + list_2
  elif midpoint_value < integer_value:
      return BinarySearch(list_2, integer_value), list_1 + list_2

search_return, reconstituted_list = BinarySearch(list_alt, integer_alt)
print(search_return, reconstituted_list)

# output = BinarySearch(list, integer)