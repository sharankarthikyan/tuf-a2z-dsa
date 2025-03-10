def max_subarr_sum(arr):
  Sum = 0
  Max = 0
  i = 0

  while i < len(arr):
    Sum += arr[i]

    if Sum > Max:
      Max = Sum
    elif Sum < 0:
      Sum = 0
    
    i += 1

  return Max

arr1 = [-2,1,-3,4,-1,2,1,-5,4]
arr2 = [1]
print (max_subarr_sum(arr1))
print (max_subarr_sum(arr2))