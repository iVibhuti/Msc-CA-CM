"""author: shriaas2898
   description: Python library contains functions related to matrix operations
"""


# for calculating minor of a matrix
def minor_mat(matrix, i, j):
    minor = matrix[:j] + matrix[j + 1:]
    minor = list(map(lambda lst: lst[:i] + lst[i + 1:], minor))
    return minor


# for calculating determinant of a matrix
def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        NonSquareMatrixExecption = Exception("Supplied matrix is not a square matrix")
        raise NonSquareMatrixExecption

    if 1 == len(matrix):
        return matrix[0][0]

    if 2 == len(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix)):
        minor = minor_mat(matrix,i, 0)
        det += (-1) ** i * matrix[0][i] * determinant(minor)

    else:
        return det


# Function to calculate transpose of matrix
def transpose(matrix):
    trans = list(map(lambda row: list(row), list(zip(*matrix))))
    return trans


# Function to calculate inverse of a matrix
def inverse_mat(matrix):

    if(determinant(matrix)==0):
        NoInverseException = Exception("Inverse of  matrix: ",matrix," does not exists since the determinant is 0.")
        raise NoInverseException

    # calculating co-factor
    inverse = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            # inserting cofactor of element in place of the element
            row.append((-1)**(i+j+2)*determinant(minor_mat(matrix, i, j)))
        inverse.append(row)

    # calculating adjoint of matrix
    #inverse = transpose(inverse)

    det = determinant(matrix)
    # calculating inverse
    matrix_element_operation(inverse, det, "div")

    return inverse


# function to perform mathematical operation on each element of a matrix
def matrix_element_operation(matrix, operand, operation):
    if(operation == "mul"):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i][j]*operand

    elif (operation == "div"):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i][j] / operand


def read_csv(file_name):
    file = open(file_name,"r")
    row,column = file.readline().strip().split(",")
    matrix = []
    for index in range(0,int(row)):
        matrix.append(list(map(int,file.readline().split(","))))
    return matrix