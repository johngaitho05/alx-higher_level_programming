#!/usr/bin/python3
"""
Divides a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a 2D matrix
    :param matrix: a 2D array
    :param div: the number to divide with
    :return: a new matrix with the division result
    """
    if type(matrix) != list or \
            not all(all(type(x) in (int, float) for x in rec)
                    for rec in matrix):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    lengths = set([len(rec) for rec in matrix])
    if len(lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda rec: list(map(lambda x: round(x / div, 2), rec)),
                    matrix))
