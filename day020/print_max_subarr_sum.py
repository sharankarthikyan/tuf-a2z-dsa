import sys

def max_subarr_sum(arr):
  Max = -sys.maxsize - 1
  Sum = 0
  start = end = s = 0
  i = 0

  while i < len(arr):
    Sum += arr[i]

    if Sum > Max:
      Max = Sum
      start = s
      end = i
    elif Sum < 0:
      Sum = 0
      s = i + 1
    
    i += 1

  return arr[start:end+1]

arr1 = [-2,1,-3,4,-1,2,1,-5,4]
arr2 = [1]
print(max_subarr_sum(arr1))
print(max_subarr_sum(arr2))