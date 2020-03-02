"""author: shriaas2898
   description: Python library contains functions related to matrix operations
"""


# for calculating determinant of a matrix
def determinant(matrix):
    if 1 == len(matrix):
        return matrix[0][0]

    if 2 == len(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix)):
        minor = matrix[1:]
        minor = list(map(lambda lst: lst[:i] + lst[i + 1:], minor))
        det += (-1) ** i * matrix[0][i] * determinant(minor)
    else:
        return det


# Function to calculate transpose of matrix
def transpose(matrix):
    trans = list(map(lambda row: list(row),list(zip(*matrix))))
    return trans
