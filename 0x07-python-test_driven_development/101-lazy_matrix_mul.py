#!/usr/bin/python3

import numpy as np

"""
Multiplies 2 matrices
"""


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices
    :param m_a: the first matrix
    :param m_b: second matrix
    :return: The resulting of m_a * m_b
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")
    elif any(type(x) != list for x in m_a):
        raise TypeError("m_a must be a list of lists")
    elif any(type(x) != list for x in m_b):
        raise TypeError("m_b must be a list of lists")
    elif not m_a or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif not m_b or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    elif any(any(type(x) not in (int, float) for x in rec)
             for rec in m_a):
        raise TypeError("m_a should contain only integers or floats")
    elif any(any(type(x) not in (int, float) for x in rec)
             for rec in m_b):
        raise TypeError("m_b should contain only integers or floats")
    lengths = set([len(rec) for rec in m_a])
    if len(lengths) > 1:
        raise TypeError("each row of m_a must be of the same size")
    lengths = set([len(rec) for rec in m_b])
    if len(lengths) > 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.dot(m_a, m_b)
