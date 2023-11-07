#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  if not matrix:
    return None
  if len(matrix)-1 == 0:
    print()
    return None
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      print("{:d}".format(matrix[i][j]), end='')
      if j < 2:
        print(" ", end='')
    print("")
