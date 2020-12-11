def insertShiftArray(arr, val):
  try:
    list(arr)
  except Exception:
    raise Exception('Function requires list input.')

  arr_len = len(arr)
  
  if arr_len % 2:
    arr_mid = round(arr_len // 2) + 1
  else:
    arr_mid = arr_len // 2

  arr.insert(arr_mid, val)

  return arr
