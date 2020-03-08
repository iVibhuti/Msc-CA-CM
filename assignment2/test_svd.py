import unittest
from svd import svd
from matrix.mat_operations import read_csv


class TestSvd(unittest.TestCase):
    def test_order_2(self):
        # Reading input from file
        matrix = read_csv("input_matrix.csv")
        #print(svd(matrix))
        self.assertEqual(([[1.0, 0.0], [0.8944271909999159, -0.4472135954999579]], [[3.0, 0], [0, 2.0]], [[1.0, 0.0], [2.0, -2.23606797749979]]), svd(matrix))

if __name__ == '__main__':
    unittest.main()

