def is_sorted(arr):
  if len(arr) == 0:
    return
  
  for i in range(0, len(arr) - 1):
    if arr[i] > arr[i + 1]:
      return False
    
  return True

print(is_sorted([1,2,3,4,5]))
print(is_sorted([5,4,6,7,8]))
print(is_sorted([]))