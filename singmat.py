import numpy as np
def sample(mat):
    #mat=[[1,4],[2,8]]
    det=np.linalg.det(mat)
    if(det!=0):
        print(det)
        print("number is non-singular")
    else:
        print(det)
        print("number is singular")
sample([[1,4],[2,8]])


#[[1,4],[2,8]]
