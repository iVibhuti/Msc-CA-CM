
import unittest
import SVD_CM as SVD_CM


class SVDTEST(unittest.TestCase):
   

    def test_correct_file_input(self):
        filename = "MatrixData.txt"
        self.assertEqual(filename,"MatrixData.txt")

    def test_file_input_incorrect(self):
        filename = "MatrixData.txt"
        self.assertNotEqual(filename,"input.txt")
    def test_SVD_one_Matrix(self):
        matrixdata = [[-5,2],[2,-2]]
        r1 = 2
        r2 = 0
        self.assertEqual(SVD_CM.calEigenVectors(matrixdata,r1,r2),[1, 3, 1, 2])
    def test_SVD_one_Matrix_incorrect(self):
        matrixdata = [[-7,2],[2,-4]]
        r1 = 2
        r2 = 0
        self.assertNotEqual(SVD_CM.calEigenVectors(matrixdata, r1, r2), [1, 2.0, 1, -0.5])
    def test_matrix_transpose(self):
        self.assertEqual(SVD_CM.transpose([[2, 3], [4, 5]]), [[2, 4], [3, 5]])
        self.assertTrue(SVD_CM.transpose([[1, 2], [3, 4, 5]]))

 

    


if __name__ == '__main__':
    unittest.main()