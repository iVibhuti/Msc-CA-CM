"""Name:Prasanjeet Sinha
PRN:19030142033"""
import unittest
from SingularOrNot import determinant


class TesCase(unittest.TestCase):

    def test_determinant(self):
        self.assertEqual(determinant([[0, 1], [0, 1]]), 0)
        self.assertNotEqual(determinant([[0, 1], [1, 1]]), 0)
        self.assertEqual(determinant([[1, 2], [3, 5]]), -1)

    def test_square_matrix(self):
        self.assertTrue(determinant([[5, 3], [2, 3]]))


if __name__ == '__main__':
    unittest.main()
