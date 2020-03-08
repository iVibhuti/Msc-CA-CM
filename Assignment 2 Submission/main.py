#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Code file for computing SVD of
   2x2 symmetric matrix.

   Author: Yash Dave
   email: mail2ypd@gmail.com
   PRN: 19030142011
   Batch: MSc CA 2019-21 @ SICSR
"""
import numpy as np
from math import sqrt


def get_eigen_values(matrix: list) -> list:
    quad_coeff_arr = []

    quad_coeff_arr.append(matrix[0][0] * matrix[1][1] - matrix[0][1] *
                          matrix[1][0])
    quad_coeff_arr.append(-matrix[0][0]-matrix[1][1])
    quad_coeff_arr.append(1)

    discriminant = (quad_coeff_arr[1]**2) - (4*quad_coeff_arr[0] *
                                             quad_coeff_arr[2])

    root1 = round((-quad_coeff_arr[1]-sqrt(discriminant))/(2*quad_coeff_arr[2]), 3)
    root2 = round((-quad_coeff_arr[1]+sqrt(discriminant))/(2*quad_coeff_arr[2]), 3)

    return [root1, root2]


def get_eigen_vectors(matrix: list, root1: float, root2: float) -> list:
    eigenvector = list()

    flag1, flag2 = True, True

    for i in range(-100, 101):
        for j in range(-100, 101):
            if (matrix[0][0]-root1)*j + matrix[0][1]*i == 0 and matrix[1][0]*j + (matrix[1][1]-root1)*i == 0:
                eigenvector.append([j, i])
                flag1 = False
                break
        if flag1 is False:
            break

    for i in range(-100, 101):
        for j in range(-100, 101):
            if (matrix[0][0]-root2)*j + matrix[0][1]*i == 0 and matrix[1][0]*j + (matrix[1][1]-root2)*i == 0:
                eigenvector.append([j, i])
                flag2 = False
                break
        if flag2 is False:
            break

    return eigenvector


def get_2d_inverse(matrix: list) -> list:
    calc_u_inverse = [
        [matrix[0][0], matrix[0][1], 1, 0],
        [matrix[1][0], matrix[1][1], 0, 1]
    ]

    modifier = calc_u_inverse[0][0]
    for k in range(4):
        calc_u_inverse[0][k] = calc_u_inverse[0][k] / modifier

    modifier = calc_u_inverse[1][0]
    for k in range(4):
        calc_u_inverse[1][k] = calc_u_inverse[1][k] - modifier*calc_u_inverse[0][k]

    modifier = calc_u_inverse[1][1]
    for k in range(4):
        calc_u_inverse[1][k] = calc_u_inverse[1][k] / modifier

    modifier = calc_u_inverse[0][1]
    for k in range(4):
        calc_u_inverse[0][k] = calc_u_inverse[0][k] - modifier*calc_u_inverse[1][k]

    u_inverse = [
        [calc_u_inverse[0][2], calc_u_inverse[0][3]],
        [calc_u_inverse[1][2], calc_u_inverse[1][3]]
    ]

    return u_inverse


def read_input(input_file='') -> list:
    matrix = list()
    if input_file == '':
        f = open(input("Enter the name of the file to be opened: "), "r")
    else:
        f = open(input_file, 'r')
    for i in range(2):
        data = f.readline()
        datalist = data.split()

        row = []
        for j in datalist:
            row.append(float(j))
        matrix.append(row)
    f.close()

    return matrix


if __name__ == "__main__":
    matrix = read_input()

    eigen_values = get_eigen_values(matrix)

    eigenvector = get_eigen_vectors(matrix, eigen_values[0], eigen_values[1])

    u = np.array([
                  [eigenvector[0][0], eigenvector[1][0]],
                  [eigenvector[0][1], eigenvector[1][1]]
                 ])

    wedge = np.array([
                      [eigen_values[0], 0],
                      [0, eigen_values[1]]
                     ])

    u_inverse = np.array(get_2d_inverse(list(u)))

    print("The Matrix is:", matrix, sep='\n')
    print("The three factors are:\nU:", u, "Wedge:", wedge, "U^-1:", u_inverse, sep='\n')
