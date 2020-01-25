import unittest

from MatrixAssignment import tempMatrixFormation,callMatrix,checkSingNonSing,checkSquareMatrix




class CheckMatrix(unittest.TestCase):

    def test_correct_file_input(self):
        name = "input.txt"
        self.assertEqual(name,"input.txt")

    def test_incorrect_file_input(self):
        name = "inputdata.txt"
        self.assertNotEqual(name,"input.txt")

    def test_correct_square_matrix(self):
        row = 3
        col = 3
        self.assertEqual(checkSquareMatrix(row,col),0)
    
    def test_incorrect_square_matrix(self):
        row = 3
        col = 2
        self.assertEqual(checkSquareMatrix(row,col),1)

    def test_one_matrix(self):
        matrix = [[1]]
        row = 1 
        self.assertEqual(row,len(matrix[0]))
    
    def test_two_singular(self):
        matrix = [[1, 2], [3,6]]
        self.assertEqual(checkSingNonSing(matrix), 0)

    def test_two_non_singular(self):
        matrix = [[1, 2], [4,6]]
        self.assertNotEqual(checkSingNonSing(matrix), 0)


    def test_three_singular(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        row = col = 3
        self.assertEqual(tempMatrixFormation(row,matrix,col), 0)

    def test_three_non_singular(self):
        matrix = [[1, 2, 1], [4, 5, 6], [7, 8, 9]]
        row = col = 3
        self.assertNotEqual(tempMatrixFormation(row,matrix,col), 1)


if __name__ == '__main__':
    unittest.main()