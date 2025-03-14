def rearrange_num(arr):
  positives = []
  negatives = []

  for i in range (len(arr)):
    if arr[i] > 0:
      positives.append(arr[i])
    else:
      negatives.append(arr[i])
    
  if len(positives) < len(negatives):
    for i in range(len(positives)):
      arr[2*i] = positives[i]
      arr[2*i+1] = negatives[i]
    
    index = len(positives) * 2
    for i in range(len(negatives) - len(positives)):
      arr[index] = negatives[len(positives) + i]
      index += 1
  else:
    for i in range(len(negatives)):
      arr[2*i] = positives[i]
      arr[2*i+1] = negatives[i]
    
    index = len(negatives) * 2
    for i in range(len(positives) - len(negatives)):
      arr[index] = positives[len(negatives) + i]
      index += 1

  return arr

arr1 = [1,2,-4,-5]
arr2 = [1,2,-3,-1,-2,-3]
print(rearrange_num(arr1))
print(rearrange_num(arr2))