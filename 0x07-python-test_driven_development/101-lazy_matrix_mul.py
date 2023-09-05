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

    return np.dot(m_a, m_b)
