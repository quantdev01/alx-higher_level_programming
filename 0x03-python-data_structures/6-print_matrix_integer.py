#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    else:
        ln = len(matrix[0])

        for i in range(len(matrix)):
            for j in range(ln):
                if (j != len(matrix) - 1):
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j], end=""))
