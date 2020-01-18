"""
Author : SahajKumar Lad
PRN : 19030142027
MSC CA 2019-21
Desc : Test cases for various inputs in singularMatrixNumpy.py file.
"""
import unittest
from singularMatrixNumpy import check_singular


class TestMatrix(unittest.TestCase):

    def test_determinant(self):
        self.assertEqual(check_singular([[0, 1], [0, 1]]), 0)
        self.assertNotEqual(check_singular([[0, 1], [1, 1]]), 0)

    def test_square_matrix(self):
        self.assertTrue(check_singular([[5, 1], [2, 3]]))


if __name__ == '__main__':
    unittest.main()
