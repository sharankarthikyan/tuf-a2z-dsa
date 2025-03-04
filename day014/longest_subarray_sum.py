def longest_subarray_sum(arr, k):
  left, right = 0, 0
  n = len(arr)
  maxLen = 0
  s = arr[0]

  while right < n:
    while left <= right and s > k:
      s -= arr[left]
      left += 1
    
    if s == k:
      maxLen = max (maxLen, right - left + 1)

    right += 1
    if right < n:
      s += arr[right]

  return maxLen

arr1 = [2,3,5]
arr2 = [2,3,5,1,9,2,0,0,5,3]
print(longest_subarray_sum(arr1, 5))
print(longest_subarray_sum(arr2, 10))
