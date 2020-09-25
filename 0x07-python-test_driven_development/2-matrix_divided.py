#!/usr/bin/python3
""" Divide matrix
"""


def matrix_divided(matrix, div):
    """ Divide elements in a matrix

    Args:
        matrix (list): list of lists
        div (integer): number which elements will be divided in a matrix

    Raises:
        ZeroDivisionError: division by zero
        TypeError: div must be a number
        TypeError: matrix must be a matrix (list of lists) of integers/float
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: matrix must be a matrix (list of lists) of integers/floats

    Returns:
        new_matrix: new list of lists
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    new_matrix = []
    new_list = []
    for row in matrix:
        if type(row) != list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(
                    'matrix must be a matrix (list of lists) '
                    'of integers/floats')
            result = item / div
            new_list.append(round(result, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
