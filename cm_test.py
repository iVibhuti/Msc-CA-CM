import unittest 
from cm import cofactors,isSingular
class TestMatrix(unittest.TestCase):

 

    #The matrix will always be square matrix because the code accepts one value from user and creates square matrix for the same

    def test_file_input(self):
        file = "matrix.txt"
        self.assertEqual(file,"marix.txt")

    def test_file1(self):
        file = "matrixdata.txt"
        self.assertNotEqual(file,"matrix.txt")

    def test_for_1x1(self):

        mat=[[5]]

        self.assertAlmostEqual(mat[0][0],5)

    #checking for 2x2 matrix

 

    def test_for_2x2(self):

        mat=[[4,2],[4,2]]
        n=2

        self.assertEqual(isSingular(mat,n),0)

    

    #cgecking for 4x4 matrix

    def test_for_3x3(self):

        mat=[[1,2,1],[5,6,2],[1,2,1]]
        n=3

        self.assertNotEqual(isSingular(mat,n),0)

 

    #Similarly we can check for nxn matrix.
