def leaders_in_array(arr):
  i = len(arr) - 1
  result = [arr[i]]
  max_from_right = arr[i]
  i -= 1

  while i >= 0:
    if arr[i] > max_from_right:
      max_from_right = arr[i]
      result.append(arr[i])
    i -= 1

  result.reverse()
  
  return result

arr1 = [4, 7, 1, 0]
arr2 = [10, 22, 12, 3, 0, 6]
print (leaders_in_array(arr1))
print (leaders_in_array(arr2))