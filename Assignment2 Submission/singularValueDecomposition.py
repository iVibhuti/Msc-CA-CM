"""
Author : SahajKumar Lad
PRN : 19030142027
MSC CA 2019-21 
Desc : Python program to compute the factor of a given array by Singular Value Decomposition.
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


def matrix_subtraction(A, B):
    """
    Subtracts matrix B from matrix A and returns difference
        :param A: The first matrix
        :param B: The second matrix
        :return: Matrix difference
    """
    # Section 1: Ensure dimensions are valid for matrix subtraction
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')

    # Section 2: Create a new matrix for the matrix difference
    C = zeros_matrix(rowsA, colsB)

    # Section 3: Perform element by element subtraction
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]

    return C


def transpose(M):
    """
    Returns a transpose of a matrix.
        :param M: The matrix to be transposed
        :return: The transpose of the given matrix
    """
    # Section 1: if a 1D array, convert to a 2D array = matrix
    if not isinstance(M[0], list):
        M = [M]

    # Section 2: Get dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 3: MT is zeros matrix with transposed dimensions
    MT = zeros_matrix(cols, rows)

    # Section 4: Copy values from M to it's transpose MT
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT


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


def matrix_multiply(A, B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix
        :return: The product of the two matrices
    """
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C


def copy_matrix(mat_cpy):
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


def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
        :return: a square identity matrix
    """
    IdM = zeros_matrix(n, n)
    for i in range(n):
        IdM[i][i] = 1.0

    return IdM


def check_matrix_equality(A, B, tol=None):
    """
    Checks the equality of two matrices.
        :param A: The first matrix
        :param B: The second matrix
        :param tol: The decimal place tolerance of the check
        :return: The boolean result of the equality check
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol == None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j], tol) != round(B[i][j], tol):
                    return False

    return True


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
        As = copy_matrix(A)  # make a copy, and ...
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


def check_squareness(A):
    """
    Makes sure that a matrix is square
        :param A: The matrix to be checked.
    """
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square to inverse.")


def check_non_singular(A):
    """
    Check if matrix is non-singular.
        :param A: The matrix to be checked
        :return: determinant of the matrix if its non-singular
    """
    det = determinant_recursive(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Singular Matrix!")


def invert_matrix(A, tol=None):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed
        :return: The inverse of the matrix A
    """
    # Section 1: Make sure A can be inverted.
    check_squareness(A)
    check_non_singular(A)

    # Section 2: Make copies of A & I, AM & IM, to use for row operations
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    # Section 3: Perform row operations
    indices = list(range(n))  # to allow flexible row referencing ***
    for fd in range(n):  # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse.
        for j in range(n):  # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd + 1:]:  # *** skip row with fd in it.
            crScaler = AM[i][fd]  # cr stands for "current row".
            for j in range(n):  # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    # Section 4: Make sure that IM is an inverse of A within the specified tolerance
    if check_matrix_equality(I, matrix_multiply(A, IM), tol):
        return IM
    else:
        raise ArithmeticError("Matrix inverse out of tolerance.")


def norm(x):
    """
    Return the Euclidean norm of the vector x.
    """
    return square_root(sum([x_i ** 2 for x_i in x]))


def Q_i(Q_min, i, j, k):
    """
    Construct the Q_t matrix by left-top padding the matrix Q
    with elements from the identity matrix.
    """
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i - k][j - k]


def cmp(a, b):
    """
    Compare two given objects.
        :param a: object 1 
        :param b: object 2
        :return: compared object
    """
    return (a > b) - (a < b)


def householder(A):
    """
    Performs a Householder Reflections based QR Decomposition of the
    matrix A. The function returns Q, an orthogonal matrix and R, an
    upper triangular matrix such that A = QR.
    """
    n = len(A)

    # Set R equal to A, and create Q as a zero matrix of the same size
    R = A
    Q = [[0.0] * n for i in range(n)]

    # The Householder procedure
    for k in range(n - 1):  # We don't perform the procedure on a 1x1 matrix, so we reduce the index by 1
        # Create identity matrix of same size as A
        I = [[float(i == j) for i in range(n)] for j in range(n)]

        # Create the vectors x, e and the scalar alpha
        # Python does not have a sgn function, so we use cmp instead
        x = [row[k] for row in R[k:]]
        e = [row[k] for row in I[k:]]
        alpha = -cmp(x[0], 0) * norm(x)

        # Using anonymous functions, we create u and v
        u = list(map(lambda p, q: p + alpha * q, x, e))
        norm_u = norm(u)
        v = list(map(lambda p: p / norm_u, u))

        # Create the Q minor matrix
        Q_min = [[float(i == j) - 2.0 * v[i] * v[j] for i in range(n - k)] for j in range(n - k)]

        # "Pad out" the Q minor matrix with elements from the identity
        Q_t = [[Q_i(Q_min, i, j, k) for i in range(n)] for j in range(n)]

        # If this is the first run through, right multiply by A,
        # else right multiply by Q

        if k == 0:
            Q = Q_t
            R = matrix_multiply(Q_t, A)
        else:
            Q = matrix_multiply(Q_t, Q)
            R = matrix_multiply(Q_t, R)

    # Since Q is defined as the product of transposes of Q_t,
    # we need to take the transpose upon returning it
    return transpose(Q), R


def checkDiagonal(arr):
    """
    Check the matrix diagonally.
    :param arr: The matrix to check
    :return: True / False
    """
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                continue
            else:
                if abs(arr[i][j]) > 0.001:
                    return False
    return True


def qrFactorization(arr):
    """
    Factorization of a given matrix.
    :param arr: The matrix to factorize
    :return: Factorized matrix
    """
    temp = arr
    i = 0
    while True:
        Q, R = householder(temp)
        temp = matrix_multiply(R, Q)
        if checkDiagonal(temp):
            # print("Number of Factorizations: " + str(i + 1))
            break
        else:
            i += 1

    return temp


def eigen_values(arr):
    """
    Calculate the eigen values of a Matrix
    :param arr: The matrix to find eigen values
    :return: List of eigen values
    """
    count = 1
    values = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                temp = arr[i][j]
                if abs(temp) < 0.000000000001:
                    temp = 0
                # print("Lamda" + str(count) + ": " + str(round(temp, 4)))
                values.append(round(temp, 4))
                count += 1

    return values


def reduced_row_echelon_form(M):
    """
    Create a reduced row echelon form of a matrix.
    :param M: The matrix to be row reduced
    :return: Reduced row echelon form of a given matrix
    """
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r

                lead += 1
                if columnCount == lead:
                    return
        M[i], M[r] = M[r], M[i]
        lv = M[r][lead]
        M[r] = [mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [iv - lv * rv for rv, iv in zip(M[r], M[i])]
        lead += 1


def eigen_vectors(mat, values):
    """
    Finding the eigen vaectors from eigen values.
    :param mat: Original Matrix
    :param values: List of eigen values
    :return: Matrix of eigen vectors
    """
    lambda_matrix = identity_matrix(2)
    eigen_matrix = []

    for v in values:
        lmd = v
        for i in range(len(lambda_matrix)):
            for j in range(len(lambda_matrix)):
                if i == j:
                    lambda_matrix[i][j] = lmd * lambda_matrix[i][j]

        temp = matrix_subtraction(mat, lambda_matrix)
        reduced_row_echelon_form(temp)
        temp_vector = temp[0]
        temp_vector.reverse()

        if temp_vector[0] is not 0.0:
            a = temp_vector[0]
            if a < 0:
                temp_vector[0] = a * -1
            else:
                temp_vector[0] = a * -1

        eigen_matrix.append(temp_vector)

    return eigen_matrix


def square_root(n):
    """
    Calculate the square root of a given number
        :param n: Number to find square root of
        :return: Square root of a number
    """
    const = 0.5
    sqrt = round((n ** const), 4)
    return sqrt


def print_matrix(M):
    """
    docstring here
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x, 3) + 0 for x in row])


def main():
    file_input = input("Enter the file name with path : ")
    # file_input = "F:\matrix.txt"
    matrix = read_matrix(file_input)

    e_values = eigen_values(qrFactorization(matrix))
    print("Eigen Values :", e_values)

    U = eigen_vectors(matrix, e_values)
    print("U : ")
    print_matrix(U)

    e_values.sort(reverse=True)
    caret = identity_matrix(len(e_values))
    caret[0][0] = caret[0][0] * e_values[0]
    caret[1][1] = caret[1][1] * e_values[1]
    print("Caret(^) : ")
    print_matrix(caret)

    U_inverse = invert_matrix(U)
    print("Inverse of U : ")
    print_matrix(U_inverse)


if __name__ == "__main__":
    main()
