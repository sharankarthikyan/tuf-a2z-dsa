def bubble_sort(arr):
  for i in range (len(arr) - 1, 0, -1):
    for j in range (0, i):
        if arr[j] > arr[j+1]:
          temp = arr[j]
          arr[j] = arr[j+1]
          arr[j+1] = temp
  return arr

print(bubble_sort([13,46,24,52,20,9]))
print(bubble_sort([5,4,3,2,1]))