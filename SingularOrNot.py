"""Name:Prasanjeet Sinha
PRN:19030142033"""

import numpy as np
def determinant(matrix):
    determinant=np.linalg.det(matrix)
    return determinant
def main():
    matrix=[[1,4],[2,8]]
    det=determinant(matrix)
    if det==0:
        print("Matrix is singular")
    else:
        print("Non singular")

if __name__=="__main__":
    main()
