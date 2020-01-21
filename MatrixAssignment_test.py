import unittest

from MatrixAssignment import tempMatrixFormation,callMatrix,checkSingNonSing




class CheckMatrix(unittest.TestCase):

    def test_two_singular(self):
        matrix = [[1, 2], [3, 6]]
    
        self.assertEqual(checkSingNonSing(matrix), 0)

    def test_two_non_singular(self):
        matrix = [[1, 2], [3, 5]]
        self.assertEqual(checkSingNonSing(matrix), -1)

    def test_three_singular(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        row = col = 3
        self.assertEqual(tempMatrixFormation(row,matrix,col), 0)

    def test_three_non_singular(self):
        matrix = [[1, 2, 1], [4, 5, 6], [7, 8, 9]]
        row = col = 3
        i = 0
        self.assertNotEqual(tempMatrixFormation(row,matrix,col), 1)


if __name__ == '__main__':
    unittest.main()