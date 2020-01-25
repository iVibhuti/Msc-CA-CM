"""
Author : SahajKumar Lad
PRN : 19030142027
MSC CA 2019-21
Desc : Test cases for various inputs in singularMatrix.py file.
"""
import unittest
from singularMatrix import determinant_recursive
from singularMatrix import copy_of_matrix
from singularMatrix import zeros_matrix
from singularMatrix import read_matrix
from singularMatrix import check_squareness


class TestMatrix(unittest.TestCase):

    def test_singular_matrix(self):
        self.assertEqual(determinant_recursive([[0, 1], [0, 1]]), 0)
        self.assertNotEqual(determinant_recursive([[1, 2], [2, 1]]), 0)

    def test_copy_of_matrix(self):
        self.assertEqual(copy_of_matrix([[1, 2], [1, 2]]), [[1, 2], [1, 2]])
        self.assertNotEqual(copy_of_matrix([[2, 4], [5, 6]]), [[1, 2], [5, 6]])

    def test_zero_matrix(self):
        self.assertEqual(zeros_matrix(2, 2), [[0, 0], [0, 0]])
        self.assertNotEqual(zeros_matrix(2, 2), [[0, 0], [1, 1]])

    def test_matrix_input(self):
        self.assertRaises(Exception, read_matrix, "/matrix.txt")
        self.assertRaises(Exception, read_matrix, "matrix")

    def test_square_matrix(self):
        self.assertTrue(check_squareness([[0, 1], [0, 1]]))
        self.assertRaises(ArithmeticError, check_squareness, [[1, 2, 3], [3, 2, 1]])


if __name__ == '__main__':
    unittest.main()
