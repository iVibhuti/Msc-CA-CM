#Name:Edna Martis
#PRN:19030142015

import math
svd_f= open('svdinput', 'r')
matrix= [[int(num) for num in line.split(',')] for line in svd_f]
a = matrix[0][0]
b = matrix[0][1]
c = matrix[1][0]
d = matrix[1][1]

eigenval1 = ((a+d) + math.sqrt(math.pow(a-d,2) + 4*b*c))/2
eigenval2 = ((a+d) - math.sqrt(math.pow(a-d,2) + 4*b*c))/2
print("First Eigenvalue:",eigenval1)
print("Second Eigenvalue:",eigenval2)
e = eigenval1
x = b
y = e-a
r = math.sqrt(x*x+y*y)
if r > 0:
     x /= r
     y /= r
else:
    x = e-d
    y = c
    r = math.sqrt(x*x+y*y)
    if r > 0:
        x /= r
        y /= r
    else:
        x = 1
        y = 0

Vectone=[x,y]
print("Eigen vector1:",Vectone)
e = eigenval2
x = b
y = e-a
r = math.sqrt(x*x+y*y)
if r > 0:
    x /= r
    y /= r
else:
    x = e-d
    y = c
    r = math.sqrt(x*x+y*y)
    if r > 0:
         x /= r
         y /= r
    else:
        x = 0
        y = 1


Vecttwo=[x,y]
print("Eigenvector2:",Vecttwo)
DiagVal=[[eigenval1,0],[0,eigenval2]]
print("The eigenvalue matrix(^):", DiagVal)
VectMat=[Vectone,Vecttwo]
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


print("Inverse of Eigenvector Matrix(U-1):",getMatrixInverse(VectMat))
print("SVD:",VectMat,DiagVal,getMatrixInverse(VectMat))
