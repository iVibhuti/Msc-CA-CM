from math import sqrt
def eigen_values(arr):
    
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
def check_non_singular(A):
    det = determinant_recursive(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Singular Matrix!")
def zeros_matrix(rows, cols):
     
    mat = []
    while len(mat) < rows:
        mat.append([])
        while len(mat[-1]) < cols:
            mat[-1].append(0.0)

    return mat
def qrFactorization(arr):
    """
    Factorization of a given matrix.
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
def transpose(M):
       
    # Section 1: if a 1D array, convert to a 2D array = matrix
    if not isinstance(M[0], list):
        M = [M]

    rows = len(M)
    cols = len(M[0])


    MT = zeros_matrix(cols, rows)

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT
def matrix_multiply(A, B):
       
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
def calEigenVectors(matrixdata, r1, r2):
    temp = []

    x1 = matrixdata[0][0] - r1

    for i in range(0, 2):
        x2 = -(matrixdata[0][1])
        x2 = x1 / x2
        x1 = 1

        temp.append(x1)
        temp.append(x2)

        x1 = matrixdata[0][0] - r2

    return temp

def norm(x):
       
    return square_root(sum([x_i ** 2 for x_i in x]))
def inverseMatrix(vectorMat):
    cofactor = []
    temp = []
    r = 1
    c = 1
    sign = 1

    
    deter = (vectorMat[0][0] * vectorMat[1][1]) - (vectorMat[0][1] * vectorMat[1][0])

    #  Cofactors calculation of a given matrix
    for i in range(0, 2):
        for j in range(0, 2):
            data = (vectorMat[r][c])
            if (i + j) % 2 != 0:
                temp.append(data * (-sign))
            else:
                temp.append(data)
            c = c - 1
        r = 0
        c = 1
        cofactor.append(temp)
        temp = []

    # Matrix Tranpose calculation of a given matrix
    tempVar = cofactor[0][1]
    cofactor[0][1] = cofactor[1][0]
    cofactor[1][0] = tempVar

    # Inverse calculation of a given matrix
    for i in range(0, 2):
        for j in range(0, 2):
            cofactor[i][j] = float(cofactor[i][j]) / deter
    print("Inverse Of Vector : ", cofactor)

    return cofactor

# Function to calculate the SVD
def calculateSVD(base):
    temporMat = []
    vectorMatrix = []
    valueMatrix = []

    p = 1
    q = -(base[0][0]) - (base[1][1])
    c = (base[0][0] * base[1][1]) - (base[1][0] * base[0][1])

    #  discriminant
    discrim = (q ** 2) - 4 * p * c

    if discrim > 0:
        r1 = int((-q + sqrt(discrim)) / (2))
        r2 = int((-q - sqrt(discrim)) / (2))
        print(" Eigen Values for Data  : ", r1, r2)

    else:
        print("Provide Valid Matrix!")

    if r1 > r2:
        list = [r1, r2]
    else:
        list = [r2, r1]

    for i in range(0, 2):
        for j in range(0, 2):
            if i == j:
                temporMat.append(list[j])
            else:
                temporMat.append(0)
        valueMatrix.append(temporMat)
        temporMat = []
    temporMat = []

    vectorMat = calEigenVectors(base, r1, r2)

    if (r1 > r2):
        m = 0
        for i in range(0, 2):
            for j in range(0, 2):
                temporMat.append(vectorMat[m])
                m = m + 2
            vectorMatrix.append(temporMat)
            temporMat = []
            m = 1
    else:
        m = 2
        for i in range(0, 2):
            for j in range(0, 2):
                temporMat.append(vectorMat[m])
                m = m - 2
            vectorMatrix.append(temporMat)
            temporMat = []
            m = 3
    print("Eigen Vector for Data : ", vectorMatrix)

    inverseMat = inverseMatrix(vectorMatrix)

    print("SVD for matrix given is ",'\n' "Value Matix : " ,valueMatrix ,'\n' ,"Vector Matrix :" , vectorMatrix, '\n', "InverseMatrix : ", inverseMat)


if __name__ == '__main__':
    
    data = []
    f = open(input("Enter the file name : "), "r")
    for i in range(0, 2):
        line = f.readline()
        datalist = line.split(" ")

        temp = []
        for j in datalist:
            temp.append(int(j))
        data.append(temp)
        temp = []

    calcluteSVD(data)