def isSingular(matrix):

    deter = 0
    i = 0
    j = 0
	
    deter = (matrix[i][j] * matrix[i + 1][j + 1]) - (matrix[i][j + 1] * matrix[i + 1][j])
	
    return deter
	


def calculateDeterminant(dim,matrix):

    determinant = 0
    cofactor_sign = 1
	
    for i in range(0,dim):
            cofactor_result = formTempMatrix(matrix,dim,i)
			
            determinant += cofactor_sign * (matrix[0][i] * cofactor_result)
			
            cofactor_sign = -cofactor_sign
			
            cofactor_result = 0
			
    return determinant


def formTempMatrix(matrix,dim,i):

    temp = []
	
    for n in range (1,dim):
	
        tempmat = []
		
        for j in range(0,dim):
		
            if(i!=j):
			
                tempmat.append(matrix[n][j])
				
        temp.append(tempmat)
		
    result = isSingular(temp)
	
    return result


if __name__ == '__main__':

    matrix = []
    result = 0
    
    openfile = open(input("Enter name of the file : "),'r')
    dim = int(openfile.readline())
	
    for i in range(0, dim):
	
        tempmat = []
		
        line = openfile.readline()
		
        for j in line:
	
            if(str(j) != "\n" and str(j) != " "):	
                tempmat.append(int(j))
			
        matrix.append(tempmat)
			
        print(matrix)
    
    if(dim ==1) :
        print("Same matrix")
		
    elif(dim == 2 ):
	
        result = isSingular(matrix)
		
    else:
	
        result = calculateDeterminant(dim,matrix)
		
    if(result == 0):
	
        print("It is a Singular Matrix ")
		
    else:
	
        print("It is a Non Singular Matrix")





