#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test file for main.py
   Checks various inputs and verifies if results are
   correct or not.
"""

import unittest

from main import find_determinant


class TestSingularMatrixChecker(unittest.TestCase):

    def test_one_by_one__matrix(self):  # Tests a 1 x 1 Matrix input
        matrix = [[2]]
        self.assertEqual(2, find_determinant(matrix))

    def test_two_by_two_matrix(self):  # Tests a 2 x 2 Matrix input
        matrix = [[1, 2],
                  [3, 4]]
        self.assertEqual(-2, find_determinant(matrix))

    def test_three_by_three_singular_matrix(self):  # Tests a 3 x 3 Matrix
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        self.assertTrue(find_determinant(matrix) == 0)

    def test_three_by_three_nonsingular_matrix(self):  # Tests a 3 x 3 Matrix
        matrix = [[6, 5, 4],
                  [2, 3, 1],
                  [7, 8, 9]]
        self.assertTrue(find_determinant(matrix) != 0)

    def test_four_by_four_nonsingular_matrix(self):  # Tests a 4 x 4 Matrix
        matrix = [[13, 11, 10, 9],
                  [8, 7, 1, 2],
                  [3, 4, 11, 5],
                  [9, 0, 1, 2]]
        self.assertTrue(find_determinant(matrix) != 0)

    def test_four_by_four_singular_matrix(self):  # Tests a 4 x 4 Matrix
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]
        self.assertTrue(find_determinant(matrix) == 0)


if __name__ == '__main__':
    unittest.main()
