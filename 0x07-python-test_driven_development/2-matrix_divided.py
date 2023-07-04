#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module contains two functions:
   - matrix_divided: Divide all elements of a matrix by a divisor
   - deep_copy: Create a deep copy of a list with no ties to the original
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by the divisor.

    Args:
        matrix (list): A flat or nested list of integers.
        div (int | float): The divisor to use for each integer or float.

    Raises:
        TypeError: If the divisor is not a float or integer.
        ZeroDivisionError: If the divisor is zero (cannot divide by zero).
        TypeError: If all rows do not have the same size.
        TypeError: If any element in the final nested list is not an int or float.

    Returns:
        list: The result of dividing each integer and float in the matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a valid list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Perform division and rounding
    result_matrix = []
    for row in matrix:
        result_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result_row.append(round(element / div, 2))
        result_matrix.append(result_row)

    return result_matrix
