def find_miss_num(arr):
  n = len(arr)
  xor1 = 0
  xor2 = 0
  
  for i in range (n - 1):
    xor2 = xor2 ^ arr[i]
    xor1 = xor1 ^ (i + 1)
  
  xor1 = xor1 ^ n
  
  return xor1 ^ xor2

arr1 = [1,2,4,5]
print(find_miss_num(arr1));