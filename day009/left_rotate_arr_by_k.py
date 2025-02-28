def left_rotate(arr, k, direction):
  if len(arr) <= k:
    return arr

  if direction == "right":
    k_elements = arr[len(arr) - k:len(arr)]
    arr = k_elements + arr[:len(arr) - k]
  elif direction == "left":
    k_elements = arr[:k]
    arr = arr[k:len(arr)] + k_elements
  return arr

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,8,9,10,11]
print(left_rotate(arr1, 2, "right"))
print(left_rotate(arr2, 3, "left"))
