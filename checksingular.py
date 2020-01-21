import numpy as np
def determinant(matrix):
    determinant=np.linalg.det(matrix)
    return determinant
def main():
    matrix=[[0,1],[0,1]]
    det=determinant(matrix)
    if det==0:
        print("Matrix is singular")
    else:
        print("Non singular")

if __name__=="__main__":
    main()


