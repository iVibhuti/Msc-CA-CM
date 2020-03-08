#importing the packages
from math import sqrt

#function to calculate the eigen values
def calculateEigenValue(data):
    #declaring variables
    tempMatrix = []
    vectorMatrix = []
    valueMatrix = []

    #assigning the coefficients
    a = 1
    b = -(data[0][0]) -(data[1][1])
    c = (data[0][0] * data[1][1]) - (data[1][0] * data[0][1])

    #calculating the discriminant
    d = (b ** 2) - 4 * a * c

    #calculating the eigen values
    if d > 0:
        root1 = int((-b + sqrt(d))/(2 * a))
        root2 = int((-b - sqrt(d)) / (2 * a))
        print("The Eigen Values are : ", root1 , root2)
        print("")

    else:
        print("SVD cannot be computed :(")

    #calculating the eigen value matrix
    if root1 > root2:
        sol = [root1, root2]
    else:
        sol = [root2, root1]

    for i in range(0,2):
        for j in range(0,2):
            if i == j:
                tempMatrix.append(sol[j])
            else:
                tempMatrix.append(0)
        valueMatrix.append(tempMatrix)
        tempMatrix = []
    tempMatrix = []

    #calling the function to calculate eigen vector
    vector = calculateEigenVector(data,root1,root2)
    print("cbc",vector)

    #finding the greater root
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
    print("")

    #calling the function to calculate the inverse of eigen vector
    inverse = calculateInverse(vectorMatrix)

    print("The singular value decomposition (SVD) is ")
    print("Eigen Value Matrix : ^" ,valueMatrix)
    print("Eigen Vector Matrix : U",vectorMatrix)
    print("Inverse of Eigen Vector Matrix : U-1",inverse)

#function to calculate the eigen vector
def calculateEigenVector(data,root1,root2):

    #declaring variables
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

#function to calculate inverse of the eigen vector
def calculateInverse(vectorMatrix):

    #declaring variables
    cofactorMatrix = []
    temp = []
    r = 1
    c = 1

    # calculating the determinant
    determinant = (vectorMatrix[0][0] * vectorMatrix[1][1]) - (vectorMatrix[0][1] * vectorMatrix[1][0])

    #finding the cofactor matrix
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

    #finding the transpose of cofactor matrix
    temp = cofactorMatrix[0][1]
    cofactorMatrix[0][1] = cofactorMatrix[1][0]
    cofactorMatrix[1][0] = temp

    #calculating the inverse of the matrix
    for i in range(2):
        for j in range(2):
            cofactorMatrix[i][j] = float(cofactorMatrix[i][j]) / determinant
    print("The inverse of the vector matrix is : ")
    print(cofactorMatrix)
    print("")
    return cofactorMatrix



if __name__ == '__main__':
    #declaring variables
    matrix = []

    #opening the file
    f = open(input("Enter the name of the file to be opened  : "),"r")
    for i in range(2):
        data = f.readline()
        datalist = data.split(" ")

        mat = []
        for j in datalist:
            mat.append(int(j))
        matrix.append(mat)
        mat = []
    print(matrix)

    calculateEigenValue(matrix)



