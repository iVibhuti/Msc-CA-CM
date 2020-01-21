import numpy as np  
import unittest


class TestMatrix(unittest.TestCase):

    #The matrix will always be square matrix because the code accepts one value from user and creates square matrix for the same
    def test_for_1x1(self):
        mat=[[5]]
        self.assertAlmostEqual(np.linalg.det(mat),5.0)
    #checking for 2x2 matrix

    def test_for_2x2(self):
        mat=[[4,2],[4,2]]
        self.assertEqual(np.linalg.det(mat),0.0)
    
    #cgecking for 4x4 matrix
    def test_for_4x4(self):
        mat=[[4,6,8,9],[5,6,2,1],[6,4,2,0],[5,0,0,8]]
        self.assertNotEqual(np.linalg.det(mat),0.0)

    #Similarly we can check for nxn matrix.

