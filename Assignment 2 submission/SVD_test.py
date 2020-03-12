import unittest
from SVD import calculateEigenValue,calculateEigenVector,calculateInverse


class CheckForSVD(unittest.TestCase):
    def test_correct_file_input(self):
        name = "data.txt"
        self.assertEqual(name,"data.txt")

    def test_incorrect_file_input(self):
        name = "inputdata.txt"
        self.assertNotEqual(name,"data.txt")
    def test_eigenVector(self):
        matrix = [[0,1],[-2,-3]]
        root1 = 2
        root2 = 0
        self.assertEqua(calculateEigenVector(matrix,root1,root2),[1, -1.0, 1, 1.0])
    def test_incorrect_eigenVector(self):
        matrix = [[1, 1], [-2, -3]]
        root1 = 2
        root2 = 0
        self.assertNotEqua(calculateEigenVector(matrix, root1, root2), [1, -1.0, 1, 1.0])



if __name__ == '__main__':
    unittest.main()
