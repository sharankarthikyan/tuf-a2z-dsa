def linear_search(arr, num):
  for i in range(0, len(arr)):
    if arr[i] == num:
      return i
    
  return -1


arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
print(linear_search(arr1, 3))
print(linear_search(arr2, 5))
