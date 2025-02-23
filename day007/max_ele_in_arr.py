def max_ele (arr):
  if len(arr) == 0:
    return -1
  
  _max = arr[0]

  for i in range (1, len(arr)):
    if arr[i] > _max:
      _max = arr[i]
  
  return _max

print(max_ele([2,5,1,3,0]))
print(max_ele([8,10,5,7,9]))