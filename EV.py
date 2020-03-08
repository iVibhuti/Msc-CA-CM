import math
f = open('svdfile', 'r')
basis = [[int(num) for num in line.split(',')] for line in f]
a = basis[0][0]
b = basis[0][1]
c = basis[1][0]
d = basis[1][1]

eigenvalue1 = ((a+d) + math.sqrt(math.pow(a-d,2) + 4*b*c))/2
eigenvalue2 = ((a+d) - math.sqrt(math.pow(a-d,2) + 4*b*c))/2
print(eigenvalue1)
print(eigenvalue2)
e = eigenvalue1
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
print("Eigenvector1: (", x , "," ,y , ")")
Vectone=[x,y]
print("Eigen vector1:",Vectone)
e = eigenvalue2
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

print("Eigenvector2: (" , x , "," , y , ")")
Vecttwo=[x,y]
print("Printing eigen vector two:",Vecttwo)
D=[[eigenvalue1,0],[0,eigenvalue2]]
print("The matrix of eigen values:", D)
P=[Vectone,Vecttwo]
print("Matrix of eigen vectors is as follows",P)
# transpose of matrix
def transpose(P, l2):

    for i in range(len(P[0])):
        row = []
        for item in P:
            row.append(item[i])
        l2.append(row)
    return l2
l2 = []
print(transpose(P, l2))
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


print("Inverse of matrix P:",getMatrixInverse(P))