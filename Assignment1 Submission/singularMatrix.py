"""
Author : SahajKumar Lad
PRN : 19030142027
MSC CA 2019-21
Desc : Python program to show if a matrix is singular or non singular.
"""


def read_matrix(file_path):
    """
    Read the integer from the file and store it in a 2D array.
        :param file_path: full path of the file
        :return: 2D array
    """
    try:
        with open(file_path) as file:
            array = []
            for line in file:
                array.append([int(x) for x in line.split()])  #
        return array

    except Exception:
        raise Exception("File Error")


def check_squareness(A):
    """
    Makes sure that a matrix is square
        :param A: The matrix to be checked.
    """
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square.")
    else:
        return True


def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
        :return: list of lists that form the matrix
    """
    mat = []
    while len(mat) < rows:
        mat.append([])
        while len(mat[-1]) < cols:
            mat[-1].append(0.0)

    return mat


def copy_of_matrix(mat_cpy):
    """
    Creates and returns a copy of a matrix.
        :param mat_cpy: The matrix to be copied
        :return: A copy of the given matrix
    """
    # Get matrix dimensions
    rows = len(mat_cpy)
    cols = len(mat_cpy[0])

    # Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)

    # Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = mat_cpy[i][j]

    return MC


def determinant_recursive(A, total=0):
    """
        Find determinant of a square matrix using full recursion
            :param A: the matrix to find the determinant for
            :param total=0: safely establish a total at each recursion level
            :returns: the running total for the levels of recursion
    """
    # store indices in list for row referencing
    indices = list(range(len(A)))

    # when at 2x2 sub-matrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    # define sub-matrix for focus column and call this function
    for fc in indices:  # for each focus column, ...
        # find the sub-matrix ...
        As = copy_of_matrix(A)  # make a copy, and ...
        As = As[1:]  # remove the first row
        height = len(As)

        for i in range(height):
            # for each remaining row of sub-matrix remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        # pass sub-matrix recursively
        sub_det = determinant_recursive(As)
        # total all returns from recursion
        total += sign * A[0][fc] * sub_det

    return round(total)


if __name__ == "__main__":
    file_input = input("Enter the file name with path : ")
    matrix = read_matrix(file_input)
    if check_squareness(matrix) is True:
        if determinant_recursive(matrix) == 0:
            print("Matrix is Singular")
        else:
            print("Matrix is Non-Singular")
