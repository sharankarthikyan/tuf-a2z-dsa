def recursive_insertion_sort(arr, i):
  if i == len(arr):
    return
  
  j = i
  while j > 0 and arr[j - 1] > arr[j]:
    temp = arr[j - 1]
    arr[j - 1] = arr[j]
    arr[j] = temp
    j -= 1

  recursive_insertion_sort(arr, i + 1)


arr1 = [13,46,24,52,20,9]
arr2 = [5,4,3,2,1]
recursive_insertion_sort(arr1, 1)
recursive_insertion_sort(arr2, 1)

print(arr1)
print(arr2)