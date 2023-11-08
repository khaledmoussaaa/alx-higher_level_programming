#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = list()
    newMatrix = []
    for i in matrix:
        result = list(map(lambda x: x**2, i))
        newMatrix.append(result)
    return newMatrix
