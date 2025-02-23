def sec_max_ele (arr):
  if len(arr) <= 1:
    return [-1, -1]
  
  _max = float('-inf')
  _sec_max = float('-inf')

  _min = float('inf')
  _sec_min = float('inf')

  for i in range (0, len(arr)):
    if arr[i] < _min:
      _sec_min = _min
      _min = arr[i]
    elif arr[i] > _min and arr[i] < _sec_min:
      _sec_min = arr[i]
    
    if arr[i] > _max:
      _sec_max = _max
      _max = arr[i]
    elif arr[i] < _max and arr[i] > _sec_max:
      _sec_max = arr[i]

    
  
  return [_sec_min, _sec_max]

print (sec_max_ele([1,2,4,7,7,5]))
print (sec_max_ele([1]))