def buy_sell_stock(arr):
  maxProfit = 0
  minPrice = float('inf')
  
  for i in range (len(arr)):
    minPrice = min(minPrice, arr[i])
    maxProfit = max(maxProfit, arr[i] - minPrice)

  return maxProfit

arr1 = [7,1,5,3,6,4]
arr2 = [7,6,4,3,1]
print(buy_sell_stock(arr1))
print(buy_sell_stock(arr2))