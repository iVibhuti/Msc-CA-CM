"""
samak Aditya Ramchandra
PRN-19030142028 Msc(CA)
"""

global N 
N = 3
  
# Function to get cofactor of mat[p][q] in temp[][]. 
def getcofactor(mat,temp,p,q,n):
    i=0
    j=0
    for row in range(n):
        for col in range(n):
            if (row!=p and col!=q):
                temp[i][j]=mat[row][col] 
                j+= 1
                if (j==n-1):
                    j=0
                    i+=1
  
# Recursive function to check if mat[][] is singular or not.
def isSingular(mat,n): 
    D=0 # Initialize result 
    if (n==1):
        return mat[0][0] 
    temp=[[0 for i in range(N + 1)] for i in range(N + 1)]# To store cofactors 
    sign=1 
    for f in range(n):
        getcofactor(mat, temp,0, f, n) # getting Cofactor of mat[0][f] 
        D+=sign*mat[0][f]*isSingular(temp,n-1) 
        sign=-sign 
    return D 
  
if __name__=='__main__':
    mat=[[4,10,1],[0,0,0],[1,4,-3]] 
    if(isSingular(mat, N)): 
        print("Matrix is Singular") 
    else: 
        print("Matrix is non-singular") 

        
