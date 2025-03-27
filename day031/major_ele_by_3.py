from collections import defaultdict

def major_ele(arr):
  Map = defaultdict(int)
  for i in range (len(arr)):
    Map[arr[i]] += 1

  result = []

  for ele in Map:
    if Map[ele]//3 == 1:
      result.append(ele)

  return result

arr1 = [1,2,2,3,2]
arr2 = [11,33,33,11,33,11]
print(major_ele(arr1))
print(major_ele(arr2))