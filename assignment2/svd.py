import matrix.mat_operations as matop
'''author: shriaas2898
   description: Python file contains function to derive 3 matrices from a single matrix by the method of singular value 
   decomposition '''
# Singular value decompostion of 2x2 matrix


def svd(matrix):
    if len(matrix) != 2:
        WrongOrderMatrix = Exception("Matrix: ", matrix, " is not of 2x2 order")
        raise WrongOrderMatrix
    # extracting elements from matrix
    m1, m2 = matrix[0]
    m3, m4 = matrix[1]

    # finding roots of quadratic equation: e**2 -(m1+m2)*e -m2*m3
    e1 = ((m1 + m4) + ((m1 - m4) ** 2 + 4 * m2 * m3) ** 0.5) / 2
    e2 = ((m1 + m4) - ((m1 - m4) ** 2 + 4 * m2 * m3) ** 0.5) / 2

    # building eigen matrix from eigen values
    evalue_matrix = [[e1, 0], [0, e2]]

    # calculating eigen vectors
    evector_matrix = []
    e = e1
    x = m2
    y = e - m1
    r = (x * x + y * y) ** 0.5
    if r > 0:
        x /= r
        y /= r
    else:
        x = e - m4
        y = m3
        r = (x * x + y * y) ** 0.5
        if r > 0:
            x /= r
            y /= r
        else:
            x = 1
            y = 0
    evector_matrix.append([x, y])

    e = e2
    x = m2
    y = e - m1
    r = (x * x + y * y) ** 0.5
    if r > 0:
        x /= r
        y /= r
    else:
        x = e - m4
        y = m3
        r = (x * x + y * y) ** 0.5
        if r > 0:
            x /= r
            y /= r
        else:
            x = 1
            y = 0
    evector_matrix.append([x, y])
    return (evector_matrix, evalue_matrix, matop.inverse_mat(evector_matrix))