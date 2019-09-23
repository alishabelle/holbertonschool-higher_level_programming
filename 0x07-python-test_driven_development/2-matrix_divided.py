#!/usr/bin/python3
"""Function that divides elements of a matrix"""

def matrix_divided(matrix, div):
    hi = []
    hey = []

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if not isinstance(matrix[x][y], int) and not isinstance(matrix[x][y], float):
                raise TypeError("matrix must be a matrix(list of lists) of integers/floats") 
            ho = round(matrix[x][y] / div, 2)
            hi.append(ho)
        hey.append(hi)
        hi = []
    return(hey)
