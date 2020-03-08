import unittest
from SVD import calculateEigenValue,calculateEigenVector,calculateInverse


class CheckForSVD(unittest.TestCase):
    def test_correct_file_input(self):
        name = "data.txt"
        self.assertEqual(name,"data.txt")

    def test_incorrect_file_input(self):
        name = "inputdata.txt"
        self.assertNotEqual(name,"data.txt")



if __name__ == '__main__':
    unittest.main()
