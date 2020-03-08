#Name- Apurva Kumar Singh
#Prn- 19030142007

from math import sqrt

def calcluteEigenValue(data):
    tempMatrix = []
    vectorMatrix = []
    valueMatrix = []
    a = 1
    b = -(data[0][0]) -(data[1][1])
    c = (data[0][0] * data[1][1]) - (data[1][0] * data[0][1])

    d = (b ** 2) - 4 * a * c

        root1 = int((-b + sqrt(d))/(2 * a))
        root2 = int((-b - sqrt(d)) / (2 * a))

  
    vector = calculateEigenVector(data,root1,root2)

  
    if(root1 > root2):
        k = 0
        for i in range(2):
            for j in range(2):
                tempMatrix.append(vector[k])
                k = k + 2
            vectorMatrix.append(tempMatrix)
            tempMatrix = []
            k = 1
    else:
        k = 2
        for i in range(2):
            for j in range(2):
                tempMatrix.append(vector[k])
                k = k - 2
            vectorMatrix.append(tempMatrix)
            tempMatrix = []
            k = 3
    print("The Eigen Vector Matrix is : ")
    print(vectorMatrix)
    
    inverse = calculateInverse(vectorMatrix)

    print("The singular value decomposition (SVD) is ")
    print(vectorMatrix)
    print(inverse)

def calculateEigenVector(data,root1,root2):

    vector = []

    x1 = data[0][0] - root1

    for i in range(2):
        x2 = -(data[0][1])
        x2 = x1 / x2
        x1 = 1

        vector.append(x1)
        vector.append(x2)

        x1 = data[0][0] - root2

    return vector

def calculateInverse(vectorMatrix):

    cofactorMatrix = []
    temp = []
    r = 1
    c = 1

    determinant = 2

    for i in range(2):
        for j in range(2):
            data = (vectorMatrix[c][r])
            if (i + j) % 2 != 0:
                temp.append(data * (-1))
            else:
                temp.append(data)
            r = r - 1
        c = 0
        r = 1
        cofactorMatrix.append(temp)
        temp = []

    
    temp = cofactorMatrix[0][1]
    cofactorMatrix[0][1] = cofactorMatrix[1][0]
    cofactorMatrix[1][0] = temp

    
    for i in range(2):
        for j in range(2):
            cofactorMatrix[i][j] = float(cofactorMatrix[i][j]) / determinant
    
    return cofactorMatrix



    matrix =[ [0,1],[2,3]]

    calcluteEigenValue(matrix)