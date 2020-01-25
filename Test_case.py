#Name: ISHAN PATEL
#PRN - 19030142013


import unittest
from SingMat import matrix



class TestMatrix(unittest.TestCase):

    def test_square_matrix(self):
        self.assertTrue(matrix([[5, 1], [2, 3]]))

    def test_determinant(self):
        self.assertEqual(matrix([[0, 1], [0, 1]]), 0)
        self.assertNotEqual(matrix([[0, 1], [1, 1]]), 0)
        self.assertEqual(matrix([[1, 2], [3, 5]]), -1)


if __name__ == '__main__':
    unittest.main()