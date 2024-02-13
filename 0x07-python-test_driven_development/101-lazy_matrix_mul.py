#!/usr/bin/python3
"""
    module to multiply matrix
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        Multiplies 2 matrix using numpy
        Returns:
            the product of two matrices
    """
    return np.matmul(m_a, m_b)
