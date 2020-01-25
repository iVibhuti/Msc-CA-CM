import numpy as np

#def calc():
size=int(input('Enter size of sqaure matrix'))
i=0
j=0
mat=[]

for i in range(0,size):
    temp=[]
    for j in range(0,size):

        print(i,j)

        temp.append(int(input('Enter value for matrix')))
        j=j+1

    print(temp)
    mat.append(temp)
    i=i+1
    print(mat)


def cofactors(mat,p,q,n):
    i=0
    j=0
    t=[[]]
    print(mat,p,q,n)
    print(t)
    for r in range(0,n):
        for c in range(0,n):
            if(r!=p and c!=q):
                j=j+1
               
                t[i][j] = mat[r][c]
                
               # t.append(l)
            if(j < n-1):
                j=0
                i=i+1
    print(t)

cofactors(mat,0,0,size)
#if (np.linalg.det(mat))==0:
 #   print('Singular Matrix')
      #return(np.linalg.det(mat))
#else:
 #   print('Non-Singular Matrix')
        #return(np.linalg.det(mat))
  