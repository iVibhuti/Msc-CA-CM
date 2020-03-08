import matrix.mat_operations as matop
'''author: shriaas2898
   description: Python file contains function to calculate determinant of matrix
   and a  function to check if the matrix is singular'''
# for calculating determinant of a matrix

def singularity_check(matrix):

    # for checking if matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        NonSquareMatrixExecption = Exception("Supplied matrix is not a square matrix")
        raise NonSquareMatrixExecption

        return False

    if 0 == matop.determinant(matrix):
        return True
    else:
        return False




if __name__ == '__main__':
    mat = matop.read_csv("input_matrix.csv")
    print(singularity_check(mat))

