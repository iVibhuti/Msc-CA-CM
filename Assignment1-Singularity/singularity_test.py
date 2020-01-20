import unittest, singularity


class SingularityTest(unittest.TestCase):
    #test for checking singularity of matrix of dimension 1x1
    def test_order_1(self):
        matrix = [[2]]
        self.assertEqual(True, singularity.singularity_check(matrix))


    #test for checking singularity of matrix of dimension 2x2
    def test_order_2(self):
        matrix = [[2,1],\
                  [4,2]]
        self.assertEqual(True, singularity.singularity_check(matrix))

    #test for checking singularity of matrix of dimension nxn
    def test_order_n(self):
        #test matrix can be changed
        matrix = [[2, 1, 1, 2], \
                  [4, 2, 2, 4], \
                  [3, 3, 2, 5], \
                  [3, 5, 0, 9]]
        self.assertEqual(True, singularity.singularity_check(matrix))

    def test_non_square(self):
        matrix = [[2,2,4],\
                  [1,3,7]]
        self.assertEqual(True, singularity.singularity_check(matrix))


if __name__ == '__main__':
    unittest.main()
