def checkSingNonSing(matrix):

    determinant = 0
    i = 0
    j = 0
	
    determinant = (matrix[i][j] * matrix[i + 1][j + 1]) - (matrix[i][j + 1] * matrix[i + 1][j])
	
    return determinant

def tempMatrixFormation(row,matrix,col):

    det = 0
    sign = 1
	
    for i in range(0,row):
            res = callMatrix(matrix,col,row,i)
            det+=sign*(matrix[0][i]*res)
            sign = -sign
            res = 0
			
    return det


def callMatrix(matrix,col,row,i):

    tempmatrix = []
	
    for k in range (1,row):
        mat = []
		
        for j in range(0,col):
            if(i!=j):
                mat.append(matrix[k][j])
        tempmatrix.append(mat)
		
    print(tempmatrix)
	
    result = checkSingNonSing(tempmatrix)
	
    return result




if __name__ == '__main__':

    tempmatrix =[]
    result = 0
	
    row = int(input("Enter the number of rows above 1: "))
    col = int(input("Enter the number of columns above 1: "))

    if(row != col):
        print("Kindly enter correct values")
		
    else:
        matrix = []
		
        for i in range(0, row):
            mat = []
			
            for j in range(0, col):
                data = int(input("Enter the element : "))
                mat.append(data)
            matrix.append(mat)
			
        print(matrix)

    if(row == 2 ):
        result = checkSingNonSing(matrix)
		
    else:
        result = tempMatrixFormation(row,matrix,col)
		
    if(result == 0):
        print("Singular Matrix ")
		
    else:
        print("Non Singular Matrix")





