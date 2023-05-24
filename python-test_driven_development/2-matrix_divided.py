#!/usr/bin/python3
"""
This module contains the matrix_divided function
"""


def matrix_divided(matrix=[[1]], div=1):
    """
    Function that divides all elements of a matrix

    Parameters:
    matrix (list of lists): matrix of integers/floats
    div (int, float): the number to divide the matrix by

    Returns:
    list of lists: new matrix with all elements divided by div,
                   rounded to 2 decimal places
    """
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
