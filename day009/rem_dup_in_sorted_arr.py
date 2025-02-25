def remove_duplicates(arr):
  i = 0
  j = 1

  while j <= len(arr) - 1:
    if arr[i] != arr[j]:
      i += 1
      arr[i] = arr[j]
    
    j += 1

  return arr[:i+1]

arr1 = [1,1,2,2,2,3,3]
arr2 = [1,1,1,2,2,3,3,3,3,4,4]
print(remove_duplicates(arr1))
print(remove_duplicates(arr2))
