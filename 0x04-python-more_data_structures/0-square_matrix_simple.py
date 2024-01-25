#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    temp = [item if not isinstance(item, list) else item[:] for item in matrix]

    def square(n):
        return n * n

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp[i][j] = square(matrix[i][j])

    return temp
