def two_sum(arr, target):
  hashMap = {}

  for i in range(len(arr)):
    s = target - arr[i]
    if s in hashMap:
      return [hashMap[s], i]
    hashMap[arr[i]] = i
  
  return []


arr = [2,6,5,8,11]
print (two_sum(arr, 14))
print (two_sum(arr, 15))