#Name : Ankita Acharekar
#PRN : 19030142005



import math
#Read matrix input from file
svdfile= open('svdip', 'r')
matrix= [[int(num) for num in line.split(',')] for line in svdfile]
p = matrix[0][0]
q = matrix[0][1]
r = matrix[1][0]
s = matrix[1][1]

#Solving quadratic equation to obtain eigen values
eigenvalue1 = ((p+s) + math.sqrt(math.pow(p-s,2) + 4*b*c))/2
eigenvalue2 = ((p+s) - math.sqrt(math.pow(p-s,2) + 4*b*c))/2
print("First Eigenvalue:",eigenvalue1)
print("Second Eigenvalue:",eigenvalue2)

#Calculating Eigen vector
E = eigenvalue1
x = q
y = E-p
z = math.sqrt(x*x+y*y)
if z > 0:
     x /= z
     y /= z
else:
    x = E-s
    y = r
    z = math.sqrt(x*x+y*y)
    if z > 0:
        x /= z
        y /= z
    else:
        x = 1
        y = 0

Vectorone=[x,y]
print("Eigen vector1:",Vectorone)
E = eigenvalue2
x = q
y = E-p
z = math.sqrt(x*x+y*y)
if z > 0:
    x /= z
    y /= z
else:
    x = E-s
    y = r
    z = math.sqrt(x*x+y*y)
    if z > 0:
         x /= z
         y /= z
    else:
        x = 0
        y = 1


Vectortwo=[x,y]
print("Eigenvector2:",Vectortwo)

#Matrix of the eigenvalue
DiagVal=[[eigenvalue1,0],[0,eigenvalue2]]
print("The eigenvalue matrix(^):", DiagVal)

#Matrix of eigenvector
VectMat=[Vectorone,Vectortwo]
print("Eigen Vector Matrix(U):",VectMat)


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
     determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
     if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

#printing inverse of eigenvector matrix
print("Inverse of Eigenvector Matrix(U-1):",getMatrixInverse(VectMat))

#Obtain the Single Value Decomposition Matrix
print("SVD:",VectMat,DiagVal,getMatrixInverse(VectMat))
