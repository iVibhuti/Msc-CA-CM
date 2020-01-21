import numpy as np


def rows_cols(ro, colm):
    simple = []
    print("enter the value to add in to the given matrics data will be enterd row wise")
    for i in range(ro):
        value1 = []
        for j in range(colm):
            value1.append(int(input()))
        simple.append(value1)
    for i in range(ro):
        for j in range(colm):
            print(simple[i][j], end=" ")
        print()
    print(np.linalg.det(simple))
    if np.linalg.det(simple) == 0:
        print("it is singular")
    else:
        print("non-singular")


