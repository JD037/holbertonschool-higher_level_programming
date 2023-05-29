#!/usr/bin/python3
"""
Module that solves the Pascal's Triangle problem
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of n.

    Args:
        n (int): number of rows of Pascal’s triangle.

    Returns:
        list of lists: Each sub-list represents a row of Pascal’s triangle.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]

        # Generate the middle elements of the row by adding pairs of elements
        # from the last row.
        middle_elements = [sum(pair) for pair in zip(last_row, last_row[1:])]

        row.extend(middle_elements)
        row.append(1)

        triangle.append(row)

    return triangle
