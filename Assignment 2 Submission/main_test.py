#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test file for main.py
   Checks various inputs and verifies if results are
   correct or not.

   Author: Yash Dave
   email: mail2ypd@gmail.com
   PRN: 19030142011
   Batch: MSc CA 2019-21 @ SICSR
"""

import unittest
import numpy as np

from main import get_2d_inverse, get_eigen_values, get_eigen_vectors, read_input


class TestSingularMatrixChecker(unittest.TestCase):

    def test_eigen_values(self):
        matrix = read_input('sample_test.txt')
        w, v = np.linalg.eig(np.array(matrix))
        ans = get_eigen_values(matrix)
        ans.sort()
        w.sort()
        self.assertAlmostEqual(ans, list(w))

    def test_svd(self):
        matrix = read_input('sample_test.txt')
        eigen_values = get_eigen_values(matrix)

        eigenvector = get_eigen_vectors(matrix, eigen_values[0], eigen_values[1])

        u = [
             [eigenvector[0][0], eigenvector[1][0]],
             [eigenvector[0][1], eigenvector[1][1]]
            ]

        wedge = [
                 [eigen_values[0], 0],
                 [0, eigen_values[1]]
                ]

        u_inverse = get_2d_inverse(list(u))

        self.assertAlmostEqual(u, [[-100,  100], [-100, -100]])
        self.assertAlmostEqual(wedge, [[0.0, 0.0], [0.0, 2.0]])
        self.assertAlmostEqual(u_inverse, [[-0.005, -0.005], [0.005, -0.005]])


if __name__ == '__main__':
    unittest.main()
