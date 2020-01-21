"""Name:Edna Martis
PRN:19030142015"""
import unittest
from Matrix import check_singular


class TestMatrix(unittest.TestCase):

    def test_determinant(self):
        self.assertEqual(check_singular([[0, 1], [0, 1]]), 0)
        self.assertNotEqual(check_singular([[0, 1], [1, 1]]), 0)
        self.assertEqual(check_singular([[1, 2], [3, 5]]), -1)

    def test_square_matrix(self):
        self.assertTrue(check_singular([[5, 3], [2, 3]]))


if __name__ == '__main__':
    unittest.main()
