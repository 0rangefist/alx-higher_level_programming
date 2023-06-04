#!/usr/bin/python3
"""
This module defines matrix_divided
"""


def is_a_matrix(data):
    """
    Returns true if an object is a matrix of ints or floats
    and returns false otherwise
    """
    if not isinstance(data, list):
        return False

    if not data:  # Check if the matrix is an empty list
        return False

    for row in data:
        if not isinstance(row, list):
            return False
        if not row:  # Check if a row is an empty list
            return False
        for elem in row:
            if not isinstance(elem, (int, float)):
                return False
    return True


def are_rows_same_length(matrix):
    """
    Returns true if a matrix has the same length for
    all it's rows and returns false if otherwise
    """
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            return False
        row_length = len(row)
    return True


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix
    and rounds the result to two decimal places
    """
    if not is_a_matrix(matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not are_rows_same_length(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Make a deep copy of the matrix for manipulation
    result_matrix = [[elem for elem in row] for row in matrix]

    # divide all elements of result_matrix by div
    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[i])):
            result_matrix[i][j] = round(result_matrix[i][j]/div, 2)
    return result_matrix
