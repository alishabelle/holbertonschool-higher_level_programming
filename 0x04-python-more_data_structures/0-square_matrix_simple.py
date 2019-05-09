#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_list = []
    new_matrix = []
    for eachList in matrix:
        for i in eachList:
            a = i ** 2
            new_list.append(a)
        new_matrix.append(new_list)
        new_list = []
    return(new_matrix)
    return(matrix)
