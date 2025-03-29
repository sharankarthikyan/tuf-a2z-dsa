def three_sum(arr):
  result = set()

  for i in range (len(arr)):
    Sum = set()
    for j in range (i + 1, len(arr)):
      third = -(arr[i] + arr[j])

      if third in Sum:
        temp = [arr[i], arr[j], third]
        temp.sort()
        result.add(tuple(temp))
      Sum.add(arr[j])

  result = list(result)
  return result

arr1 = [-1,0,1,2,-1,-4]
arr2 = [-1,0,1,0]
print(three_sum(arr1))
print(three_sum(arr2))
