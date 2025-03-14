def next_permutation(arr):
  i = len (arr) - 1
  index = -1
  while i > 0:
    if arr[i - 1] < arr[i]:
      index = i - 1
      break
    i -= 1
  
  if index == -1:
    arr.reverse()
  
  j = len(arr) - 1
  while j > index:
    if arr[j] > arr[index]:
      arr[j], arr[index] = arr[index], arr[j]
      break
    j -= 1
  
  arr[index+1:] = reversed(arr[index+1:])

  return arr

arr1 = [1,3,2]
arr2 = [3,2,1]
arr3 = [2, 4, 1, 7, 5, 0]
arr4 = [1, 3, 5, 4, 2]
print (next_permutation(arr1))
print (next_permutation(arr2))
print (next_permutation(arr3))
print (next_permutation(arr4))