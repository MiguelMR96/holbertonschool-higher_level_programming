#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    new_matrix = []
    new_list = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        if type(row) != list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            result = item / div
            new_list.append(round(result, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
