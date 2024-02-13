"""
Module matrix
"""


def matrix_divided(matrix, div):
    """
    Matrix divider
    """
    newlist = [item if not isinstance(item, list) else item[:] for item in matrix]
    t = 0

    # Testing if the matrix is a list of list and eache 
    #row have the same size
    for item in range(len(matrix)):
        if type(matrix[item]) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if t == 0:
            t = len(matrix[item])
        else:
            if t != len(matrix[item]):
                raise TypeError("Each row of the matrix must have the same size")

        
    #Over here we itereate to change values to divided ones
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newlist[i][j] = round(matrix[i][j] / div, 2)
            if type(matrix[i][j]) != (int or float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    #Checkin for dive now
    if type(div) == int:
        pass
    else:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return newlist
