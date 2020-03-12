import unittest
from SingularValueDecomposition import calcluteSVD,calculateEigenVectors,calculateInverseMatrix


class FindSVD(unittest.TestCase):
    def test_correct_file_input(self):
        filename = "input.txt"
        self.assertEqual(filename,"input.txt")

    def test_file_input_incorrect(self):
        filename = "data.txt"
        self.assertNotEqual(filename,"input.txt")
    def test_SVD_one_Matrix(self):
        matrixdata = [[-5,2],[2,-2]]
        r1 = 2
        r2 = 0
        self.assertEqua(calculateEigenVectors(matrixdata,r1,r2),[1, 2.0, 1, -0.5])
    def test_SVD_one_Matrix_incorrect(self):
        matrixdata = [[-5,2],[2,-2]]
        r1 = 2
        r2 = 0
        self.assertNotEqua(calculateEigenVectors(matrixdata, r1, r2), [1, 2.0, 1, -0.5])



if __name__ == '__main__':
    unittest.main()
