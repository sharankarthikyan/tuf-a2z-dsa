def recursive_bubble_sort(arr, n):
  if n == 0:
    return
  
  for j in range (0, n):
    if arr[j] > arr[j + 1]:
      temp = arr[j]
      arr[j] = arr[j + 1]
      arr[j + 1] = temp

  recursive_bubble_sort(arr, n - 1)


arr1 = [13,46,24,52,20,9]
arr2 = [5,4,3,2,1]
recursive_bubble_sort(arr1, len(arr1) - 1)
recursive_bubble_sort(arr2, len(arr2) - 1)

print (arr1)
print (arr2)