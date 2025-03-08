def majority_ele(arr):
  n = len(arr)
  half = n//2

  Map = {}

  for e in arr:
    if e in Map:
      Map[e] += 1

      if Map[e] > half:
        return e
    else:
      Map[e] = 1

  return -1

arr1 = [3,2,3]
arr2 = [2,2,1,1,1,2,2]
arr3 = [4,4,2,4,3,4,4,3,2,4]
print(majority_ele(arr1))
print(majority_ele(arr2))
print(majority_ele(arr3))