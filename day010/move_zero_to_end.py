def move_zero (arr):
  if len(arr) <= 1:
    return arr
  
  i = 0
  j = 1
  
  while i <= len(arr) - 1:
    if arr[i] == 0:
      while j <= len(arr) - 1:
        if arr[j] != 0:
          arr[i], arr[j] = arr[j], arr[i]
          break
        j += 1
    i += 1
    j += 1

  return arr

arr1 = [1,0,2,3,0,4,0,1]
arr2 = [1,2,0,1,0,4,0]
print(move_zero(arr1))
print(move_zero(arr2))