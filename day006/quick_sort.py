def swap (arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def partition (arr, low, high):
  pivot = arr[low]
  i = low
  j = high

  while i < j:
    while arr[i] <= pivot and i <= high - 1:
      i += 1
    
    while arr[j] > pivot and j >= low + 1:
      j -= 1
    
    if i < j:
      swap (arr, i, j)


  swap (arr, low, j)
  return j

def quick_sort (arr, low, high):
  if low >= high:
    return
  
  pIndex = partition (arr, low, high)
  quick_sort (arr, low, pIndex - 1)
  quick_sort (arr, pIndex + 1, high)


arr1 = [4,1,7,9,3]
arr2 = [4,6,2,5,7,9,1,3]
quick_sort (arr1, 0, len(arr1) - 1)
quick_sort (arr2, 0, len(arr2) - 1)

print (arr1)
print (arr2)
