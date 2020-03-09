# author : Rahul Matai
# Dt:08-03-2020
import unittest
import  numpy as np
from S_v_d import eigenvalue,eigenvector


class Checkmatrix(unittest.TestCase):
    def test_eigenvector(self):
        matrix = [[1,1],[1,1]]
        eig_vec= eigenvector(matrix)
        eig_val1 = np.linalg.eig(matrix)
        self.assertAlmostEqual(eig_vec,eig_val1)
        
    def checkinver(self):
        matrix=[[1,2],[3,4]]
        eig_inv=inv(matrix)
        eig_inv1=np.linalg.inv(matrix)
        self.assertAlmostEqual(eig_inv,eig_inv1)


if __name__ == '__main__':
    unittest.main()

