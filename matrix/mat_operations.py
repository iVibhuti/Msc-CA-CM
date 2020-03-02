"""author: shriaas2898
   description: Python library contains functions related to matrix operations
"""


# for calculating minor of a matrix
def minor_mat(matrix, i, j):
    minor = matrix[:j] + matrix[j+1:]
    print("LOG: minor after j =",minor)
    minor = list(map(lambda lst: lst[:i] + lst[i + 1:], minor))
    print("LOG: minor after i =", minor)
    return minor


# for calculating determinant of a matrix
def determinant(matrix):
    if 1 == len(matrix):
        return matrix[0][0]

    if 2 == len(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix)):
        minor = minor_mat(i,0)
        det += (-1) ** i * matrix[0][i] * determinant(minor)

    else:
        return det


# Function to calculate transpose of matrix
def transpose(matrix):
    trans = list(map(lambda row: list(row),list(zip(*matrix))))
    return trans


