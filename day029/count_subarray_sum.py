from collections import defaultdict

def count_subarray_sum(arr, k):
  Map = defaultdict(int)
  preSum = 0
  count = 0

  Map[0] = 1
  for i in range (len(arr)):
    preSum += arr[i]
    remove = preSum - k
    count += Map[remove]
    Map[preSum] += 1

  return count

arr1 = [3,1,2,4]
arr2 = [1,2,3]
print(count_subarray_sum(arr1, 6))
print(count_subarray_sum(arr2, 3))