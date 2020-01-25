import unittest
from singular import singular


class singular_matrix(unittest.TestCase):
    def test_for_1(self):
        mat = [[2]]
        self.assertEqual(True, singular(mat))

    def test_for_two(self):
        mat = [[1, 0], [3, 4]]
        self.assertEqual(False, singular(mat))

    def tes_for_three(self):
        mat = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        self.assertEqual(True, singular(mat))

    def tes_for_four(self):
        mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 2], [7, 9, 6, 2]]
        self.assertEqual(True, singular(mat))


if __name__ == '__main__':
    unittest.main()
