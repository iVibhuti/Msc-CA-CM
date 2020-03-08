"""
Author : SahajKumar Lad
PRN : 19030142027
MSC CA 2019-21
Desc : Test cases for various inputs in singularValueDecomposition.py file.
"""
import unittest
import singularValueDecomposition as svd


class MyTestCase(unittest.TestCase):

    def test_zero_matrix(self):
        self.assertEqual(svd.zeros_matrix(2, 2), [[0, 0], [0, 0]])
        self.assertNotEqual(svd.zeros_matrix(2, 2), [[0, 0], [1, 1]])

    def test_matrix_input(self):
        self.assertRaises(Exception, svd.read_matrix, "/matrix.txt")
        self.assertRaises(Exception, svd.read_matrix, "matrix")

    def test_singular_matrix(self):
        self.assertEqual(svd.determinant_recursive([[0, 1], [0, 1]]), 0)
        self.assertNotEqual(svd.determinant_recursive([[1, 2], [2, 1]]), 0)

    def test_matrix_subtraction(self):
        self.assertEqual(svd.matrix_subtraction([[5, 5], [5, 5]], [[5, 5], [5, 5]]), [[0, 0], [0, 0]])
        self.assertRaises(ArithmeticError, svd.matrix_subtraction, [[5, 5], [5, 5]], [[-5, -5], [-5, -5], [-5, -5]])

    def test_matrix_transpose(self):
        self.assertEqual(svd.transpose([[2, 3], [4, 5]]), [[2, 4], [3, 5]])
        self.assertTrue(svd.transpose([[1, 2], [3, 4, 5]]))

    def test_zero_matrix(self):
        self.assertTrue(svd.zeros_matrix(2, 3))
        self.assertEqual(svd.zeros_matrix(2, 2), [[0, 0], [0, 0]])

    def test_matrix_multiply(self):
        self.assertRaises(ArithmeticError, svd.matrix_multiply, [[5, 5], [5, 5]], [[-5, -5], [-5, -5], [-5, -5]])
        self.assertTrue(svd.matrix_multiply([[2, 3], [4, 5]], [[4, 5], [2, 3]]))

    def test_copy_matrix(self):
        self.assertEqual(svd.copy_matrix([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
        self.assertNotEqual(svd.copy_matrix([[1, 2], [3, 4]]), [[1, 2], [4, 3]])

    def test_identity_matrix(self):
        self.assertEqual(svd.identity_matrix(2), [[1, 0], [0, 1]])
        self.assertNotEqual(svd.identity_matrix(2), [[1, 0], [1, 0]])

    def test_check_matrix_equality(self):
        self.assertFalse(svd.check_matrix_equality([[1, 2], [3, 4]], [[4, 5], [2, 3], [1, 2]]))

    def test_check_squareness(self):
        self.assertFalse(svd.check_squareness([[1, 2], [3, 4]]))
        self.assertRaises(ArithmeticError, svd.check_squareness, [[1, 2], [3, 4], [2, 3]])

    def test_check_non_singular(self):
        self.assertRaises(ArithmeticError, svd.check_non_singular, [[1, 2], [1, 2]])
        self.assertEqual(svd.check_non_singular([[1, 2], [3, 2]]), -4)

    def test_inverse_matrix(self):
        self.assertRaises(ArithmeticError, svd.invert_matrix, [[4, 7], [2, 6]])

    def test_eigen_values(self):
        self.assertEqual(svd.eigen_values(svd.qrFactorization([[1, -1], [-1, 1]])), [2.0, 0.0])
        self.assertNotEqual(svd.eigen_values(svd.qrFactorization([[1, -1], [-1, 1]])), [2.0, 1.0])

    def test_reduced_row_echelon_form(self):
        self.assertFalse(svd.reduced_row_echelon_form([[-1, -1], [-1, -1]]))

    def test_eigen_vectors(self):
        self.assertTrue(svd.eigen_vectors([[1,-1], [-1, 1]], [2, 0]))
        self.assertEqual(svd.eigen_vectors([[1,-1], [-1, 1]], [2, 0]), [[-1.0, 1.0], [1.0, 1.0]])


if __name__ == '__main__':
    unittest.main()
