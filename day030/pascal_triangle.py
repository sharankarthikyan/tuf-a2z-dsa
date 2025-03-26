def nCr(n, r):
  result = 1

  for i in range (r):
    result = result * (n - i)
    result = result // (i + 1)

  return result

def pascal_triangle(n):
    for i in range (n):
      for j in range (0, i + 1):
        print(nCr(i, j), end=" ")
      print()

n = int(input("n: "))
pascal_triangle(n)