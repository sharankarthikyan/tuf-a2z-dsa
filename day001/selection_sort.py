import sys

def selection_sort(arr):
  for i in range(0, len(arr) - 1):
    minIndx = i
    for j in range (i, len(arr)):
      if arr[j] < arr[minIndx]:
        minIndx = j
    temp = arr[i]
    arr[i] = arr[minIndx]
    arr[minIndx] = temp
  return arr

print(selection_sort([13,46,24,52,20,9]))
print(selection_sort([5,4,3,2,1]))