import unittest
import numpy as np
from singular import rows_cols


class testsingular(unittest.TestCase):

    def test_two_cross_two(self):
        b = 0.0
        a = [[2, 2], [2, 2]]
        self.assertEqual(np.linalg.det(a), b)

    def test_three_cross_three(self):
        b = 0
        a = [[1, 0, 0], [1, 2, 3], [4, 5, 6]]
        self.assertNotEquals(np.linalg.det(a), b)

    def test_four_cross_four(self):
        b=0
        a=[[0,0,0,0],[1,1,1,10],[7,8,9,12],[14,15,16,17]]
        self.assertIs(np.linalg.det(a),b)

    def test_for_eqality(self):
        b=0
        a = [[0, 0, 0, 0], [1, 1, 1, 10], [7, 8, 9, 12], [14, 15, 16, 17]]
        self.assertEqual(np.linalg.det(a),b)
