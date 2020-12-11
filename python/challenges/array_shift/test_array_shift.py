from challenges.array_shift.array_shift import insertShiftArray

def test_insertShiftArray_even():
  actual = insertShiftArray([1, 2, 4, 5], 3)
  expected = [1, 2, 3, 4, 5]
  assert actual == expected

def test_insertShiftArray_odd():
  actual = insertShiftArray([1, 2, 3, 5, 6], 4)
  expected = [1, 2, 3, 4, 5, 6]
  assert actual == expected