def rotate_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(i):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  for i in range (len(matrix)):
    matrix[i].reverse()
  return matrix

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate_matrix(matrix1))
print(rotate_matrix(matrix2))