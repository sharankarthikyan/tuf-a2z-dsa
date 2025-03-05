def longest_array_sum(arr, k):
  n = len(arr)

  preSumMap = {}
  _sum = 0
  maxLen = 0

  for i in range(n):
    _sum += arr[i]

    if _sum == k:
      maxLen = max(maxLen, i+1)
    
    rem = _sum - k

    if rem in preSumMap:
      length = i - preSumMap[rem]
      maxLen = max(maxLen, length)

    if _sum not in preSumMap:
      preSumMap[_sum] = i

  return maxLen


arr1 = [2,3,5]
arr2 = [-1, 1, 1]
print(longest_array_sum(arr1, 5))
print(longest_array_sum(arr2, 1))