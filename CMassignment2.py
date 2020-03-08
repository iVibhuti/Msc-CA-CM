from math import sqrt

def Eigen(medium):
    matrix=[]
    vector=[]
    value=[]
    a =1
    b =-(medium[0][0])-(medium[1][1])
    c =(medium[0][0]*medium[1][1])-(medium[1][0] * medium[0][1])

    d (b ** 2)-4*a*c                        #Eigen Value formula

        r1=int((-b+sqrt(d))/(2*a))          # Applying the formula EigenVector
        r2=int((-b-sqrt(d))/(2*a))          # Applying the formula EigenVector

      vect=Eigen(medium,r1,r2)

    if(r1>=r2):
        v=0
        for i in range(2):
            for j in range(2):
                matrix.append(vector[v])
                v=v+2
            matrix.append(matrix)
            matrix=[]
            v=1
    else:
        z=2
        for p in range(2):
            for q in range(2):
                matrix.append(vect[z])
                z=z-2
            matrix.append(matrix)
            matrix = []
            z= 3
    print("The Eigen Vector Matrices is : ")
    print(vector)
    
    inverse = inverse(vector)

    print("The singular value decomposition : ")
    print(vector)
    print(inverse)
#Find Egigen Vector
def Eigen(medium,r1,r2):
    vect = []
    a = medium[0][0] - r1

    for i in range(2):
        b = -(medium[0][1])
        b = a / b
        a = 1

        vect.append(a)
        vect.append(b)

        a = medium[0][0] - r2

    return vect
# defining the inverse of matrix
def inverse(vector):

    cofactor=[]
    temp = []
    rr=1
    cc=1

    determinants=(vector[0][0]*vector[1][1])-(vector[0][1]*vector[1][0])  # Finding The Dtermiunant
    #Finding Cofactor
    for x in range(2):
        for y in range(2):
            medium=(vector[cc][rr])
            if (x+y)%2!=0:  # Finding the odd and even value
                temp.append(medium*(-1))  
            else:
                temp.append(medium)
            r =r-1
        cc=0
        rr=1
        cofactor.append(temp)
        temp=[]
    
    temp=cofactor[0][1]
    cofactor[0][1]=cofactor[1][0]
    cofactor[1][0]=temp

    for i in range(2):
        for j in range(2):
            cofactor[i][j] = float(cofactor[i][j])/determinants
    return cofactor
    matrices=[[0,3],[1,2]]
    Eigen(matrices)