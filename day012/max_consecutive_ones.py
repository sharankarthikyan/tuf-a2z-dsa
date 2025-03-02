def max_consecutive_ones(arr):
  _max = 0
  counter = 0

  for i in range (len(arr)):
    if arr[i] == 1:
      counter += 1
    else:
      counter = 0
    _max = max (_max, counter)
  
  return _max

arr1 = [1, 1, 0, 1, 1, 1]
arr2 = [1, 0, 1, 1, 0, 1]
print (max_consecutive_ones(arr1))
print (max_consecutive_ones(arr2))