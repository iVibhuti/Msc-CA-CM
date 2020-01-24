#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A python file which calculates determinant of a n*n matrix
   Uses Recursion to calculate the determinant

   Author: Yash Dave
   email: mail2ypd@gmail.com
   PRN: 19030142011
   Batch: MSc CA 2019-21 @ SICSR
"""


def find_determinant(matrix: list) -> int:  # Calcuates determinant
    matrix_dim = len(matrix)
    if matrix_dim == 1:
        return matrix[0][0]
    elif (matrix_dim > 2):
        i, counter, sum = 1, 0, 0
        while counter <= matrix_dim - 1:
            filter_dict = {}
            min_row = 1
            while min_row <= matrix_dim - 1:
                min_col = 0
                filter_dict[min_row] = []
                while min_col <= matrix_dim - 1:
                    if (min_col != counter):
                        filter_dict[min_row].append(matrix[min_row][min_col])
                    min_col += 1
                min_row += 1
            minor = [filter_dict[x] for x in filter_dict]
            sum = sum + i * (matrix[0][counter]) * (find_determinant(minor))
            i = i * (-1)
            counter += 1
        return sum
    else:
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])


def row_input(row_num: int, cols: int) -> list:  # Reads a matrix row from user
    row_string = input("Enter values in row %d separated by spaces: " %
                       (row_num + 1))
    row_arr = row_string.split()
    if len(row_arr) is cols:
        row_arr = [int(i) for i in row_arr]
        return row_arr
    return row_input(row_num, cols)


def input_sq_matrix(rows: int, cols: int) -> list:  # Forms a 2D square matrix
    matrix = list()
    for i in range(rows):
        matrix.append(row_input(i, cols))
    print("Input Matrix:\n", matrix, sep='')
    return matrix


if __name__ == "__main__":
    rows = int(input("Enter number of rows & cols in square matrix: "))
    cols = rows
    matrix = input_sq_matrix(rows, cols)
    determinant = 0
    determinant = find_determinant(matrix)
    print("Determinant:", determinant)
    if determinant == 0:
        print("Matrix is Singular")
    else:
        print("Matrix is Non-Singular")
