# import the package
from math import sqrt


# function to calculate the SVD
def calcluteSVD(matrixdata):
    temporMat = []
    vectorMatrix = []
    valueMatrix = []

    p = 1
    q = -(matrixdata[0][0]) - (matrixdata[1][1])
    c = (matrixdata[0][0] * matrixdata[1][1]) - (matrixdata[1][0] * matrixdata[0][1])

    # calculating the discriminant
    discrim = (q ** 2) - 4 * p * c

    if discrim > 0:
        r1 = int((-q + sqrt(discrim)) / (2))
        r2 = int((-q - sqrt(discrim)) / (2))
        print("The Eigen Values are : ", r1, r2)

    else:
        print("Sorry,SVD cannot be calculated")

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

    vectorMat = calculateEigenVectors(matrixdata, r1, r2)

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
    print("The Eigen Vector Matrix is : ", vectorMatrix)

    inverseMat = calculateInverseMatrix(vectorMatrix)

    print(" SVD is ")
    print("Value Matix : " ,valueMatrix ,'\n' ,"Vector Matrix :" , vectorMatrix, '\n', "InverseMatrix : ", inverseMat)


def calculateEigenVectors(matrixdata, r1, r2):
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


def calculateInverseMatrix(vectorMatrix):
    cofactor = []
    temp = []
    r = 1
    c = 1
    sign = 1

    # calculate the determinant
    deter = (vectorMatrix[0][0] * vectorMatrix[1][1]) - (vectorMatrix[0][1] * vectorMatrix[1][0])

    # calculate the cofactor matrix
    for i in range(0, 2):
        for j in range(0, 2):
            data = (vectorMatrix[r][c])
            if (i + j) % 2 != 0:
                temp.append(data * (-sign))
            else:
                temp.append(data)
            c = c - 1
        r = 0
        c = 1
        cofactor.append(temp)
        temp = []

    # calculate the transpose of cofactor matrix
    tempVar = cofactor[0][1]
    cofactor[0][1] = cofactor[1][0]
    cofactor[1][0] = tempVar

    # calculating the inverse of the matrix
    for i in range(0, 2):
        for j in range(0, 2):
            cofactor[i][j] = float(cofactor[i][j]) / deter
    print("The inverse of the vector matrix is : ", cofactor)

    return cofactor


if __name__ == '__main__':

    matrix = []
    f = open(input("Name : "), "r")
    for i in range(0, 2):
        line = f.readline()
        datalist = line.split(" ")

        temp = []
        for j in datalist:
            temp.append(int(j))
        matrix.append(temp)
        temp = []

    calcluteSVD(matrix)