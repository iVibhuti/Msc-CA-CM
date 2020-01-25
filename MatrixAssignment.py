def checkSquareMatrix(row,col):
    if(row == col):
        return 0
    else:
        return 1 


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

    matrix =[]
    result = 0
	
    f = open(input("Name  : "),"r")
    row = int(f.readline())
    col = int(f.readline())

    square = checkSquareMatrix(row,col)
    if(square == 1): 
        print("Row and column dimension must be same")
            
    else:
        for i in range(row):
            data = f.readline()
            print(data)
            mat = []
            for j in data: 
                if(str(j) != "\n" and str(j) != " "):
                    mat.append(int(j))
            matrix.append(mat)
        print(matrix)
        
    if(row == 1):
        print(matrix[0][0])

    elif(row == 2 ):
        result = checkSingNonSing(matrix)
		
    else:
        result = tempMatrixFormation(row,matrix,col)
		
    if(result == 0):
        print("Singular Matrix ")
		
    else:
        print("Non Singular Matrix")





