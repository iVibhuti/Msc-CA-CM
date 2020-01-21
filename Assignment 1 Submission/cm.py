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
if (np.linalg.det(mat))==0:
    print('Singular Matrix')
      #return(np.linalg.det(mat))
else:
    print('Non-Singular Matrix')
        #return(np.linalg.det(mat))
  