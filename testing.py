import unittest
from MatrixSingularity import matrix


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(matrix([[0, 1], [0, 1]]), 0)
        self.assertNotEqual(matrix([[0, 1], [1, 1]]), 0)
        self.assertEqual(matrix([[1, 2], [3, 5]]), -1)

    def test_square_matrix(self):
        self.assertTrue(matrix([[5, 3], [2, 3]]))

if __name__ == "__main__":
    unittest.main()
