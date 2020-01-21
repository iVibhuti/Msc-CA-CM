"""Name:Edna Martis
PRN:19030142015"""
import numpy as np

def check_singular(mat):
    det = np.linalg.det(mat)
    return int(det)


if __name__ == "__main__":
    # mat = [[0, 1,2], [0, 1,3],[1,2,3]]
    mat = [[0, 1], [0, 1]]  # Define the matrix(should be square matrix)
    if check_singular(mat) == 0:
        print("Matrix is Singular")
    else:
        print("Matrix is Non-Singular")
