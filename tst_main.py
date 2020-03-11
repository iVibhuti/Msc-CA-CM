#Author : ISHAN PATEL

import unittest
from main_m import main_m
from matrix.mat_operations import read_csv


class Testmain_m(unittest.TestCase):
    def test_order_2(self):
        # Reading input from file
        matrix = read_csv("input_matrix.csv")
        #print(main_m(matrix))
        self.assertEqual(([[1.0, 0.0], [0.8944271909999159, -0.4472135954999579]], [[3.0, 0], [0, 2.0]], [[1.0, 0.0], [2.0, -2.23606797749979]]), main_m(matrix))

if __name__ == '__main__':
    unittest.main()