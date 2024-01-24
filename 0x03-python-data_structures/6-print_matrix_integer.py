#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    else:
        ln_x = len(matrix)
        ln_y = len(matrix[0])
        # Displying the matrix on [i] [j] element

        for i in range(ln_x):
            for j in range(ln_y):
                if (j != ln_y - 1):
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j], end=""))
