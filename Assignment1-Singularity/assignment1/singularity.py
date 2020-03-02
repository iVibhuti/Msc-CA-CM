'''author: shriaas2898
   description: Python file contains function to calculate determinant of matrix
   and a  function to check if the matrix is singular'''
# for calculating determinant of a matrix


def determinant(matrix):

        if 1 == len(matrix):
            return matrix[0][0]

        if 2 == len(matrix):
            return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])

        det = 0
        for i in range(len(matrix)):
            minor = matrix[1:]
            minor = list(map(lambda lst :lst[:i] + lst[i+1:],minor ))
            det+= (-1)**i*matrix[0][i]*determinant(minor)
        else:
            return det


def singularity_check(matrix):

    # for checking if matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        NonSquareMatrixExecption = Exception("Supplied matrix is not a square matrix")
        raise NonSquareMatrixExecption

        return False

    if 0 == determinant(matrix):
        return True
    else:
        return False


def build_matrix(file_name):
    file = open(file_name,"r")
    row,column = file.readline().split(",")
    if row != column:
        NonSquareMatrixExecption = Exception("Supplied matrix is not a square matrix")
        raise NonSquareMatrixExecption
    else:
        matrix = []
        for index in range(0,int(row)):
            matrix.append(file.readline().split(","))

        return matrix
if __name__ == '__main__':
    