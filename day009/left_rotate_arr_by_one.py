def left_rotate(arr):
  if len(arr) <= 1:
    return arr
  
  ele = arr[0]
  arr = arr[1:len(arr)]
  arr.append(ele)
  return arr

arr1 = [1,2,3,4,5]
arr2 = [3]
print(left_rotate(arr1))
print(left_rotate(arr2))