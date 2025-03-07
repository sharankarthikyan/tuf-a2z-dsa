def sort_items(arr):
  low = 0
  mid = 0
  high = len(arr) - 1

  while mid <= high:
    if arr[mid] == 0:
      arr[mid], arr[low] = arr[low], arr[mid]
      low += 1
      mid += 1
    elif arr[mid] == 1:
      mid += 1
    else:
      arr[mid], arr[high] = arr[high], arr[mid]
      high -= 1

  return arr


arr1 = [2,0,2,1,1,0]
arr2 = [1, 0, 2, 1, 2, 0]
arr3 = [2,0,1]
arr4 = [0]
print (sort_items(arr1))
print (sort_items(arr2))
print (sort_items(arr3))
print (sort_items(arr4))