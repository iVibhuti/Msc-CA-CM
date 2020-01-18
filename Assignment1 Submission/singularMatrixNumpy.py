"""
Author : SahajKumar Lad
PRN : 19030142027
MSC CA 2019-21
Desc : Python program to show if a matrix is singular or non singular.
"""
import numpy as np


def check_singular(matrix):
    """
    Ensure that matrix is singular
        :param matrix: NxN matrix, which should be square matrix
        :return: determinant of matrix
    """
    det = np.linalg.det(matrix)
    return round(det)


if __name__ == "__main__":
    matrix = [[0, 1], [0, 1]]  # Define the matrix(should be square matrix)
    if check_singular(matrix) == 0:
        print("Matrix is Singular")
    else:
        print("Matrix is Non-Singular")
