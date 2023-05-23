#!/usr/bin/python3
"""
2-matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(rows) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for elements in rows:
            if not isinstance(elements, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        length_of_rows = len(matrix[0])
        for rows in matrix:
            if len(rows) != length_of_rows:
                raise TypeError("Each row of the matrix must have the same size")
        return [[round(elements / div, 2) for elements in rows] for rows in matrix]
