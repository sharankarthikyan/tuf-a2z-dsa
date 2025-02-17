def insertion_sort(arr):
  for i in range (0, len(arr)):
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
      temp = arr[j - 1]
      arr[j - 1] = arr[j]
      arr[j] = temp
      j -= 1
  return arr

print(insertion_sort([13,46,24,52,20,9]))
print(insertion_sort([5,4,3,2,1]))