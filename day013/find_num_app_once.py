def find_num_appear_once(arr):
  xor = 0
  for i in range (len(arr)):
    xor ^= arr[i]
  return xor

arr1 = [2,2,1]
arr2 = [4,1,2,1,2]
print(find_num_appear_once(arr1))
print(find_num_appear_once(arr2))