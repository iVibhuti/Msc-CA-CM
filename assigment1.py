import unittest

from assignemnt1 import isSingular,calculateDeterminant,formTempMatrix




class checkTestCases(unittest.TestCase):

    def test_2by2_singular(self):
	
        matrix = [[1, 1], [1, 1]]
    
        self.assertEqual(isSingular(matrix), 0)

		
    def test_2by2_non_singular(self):
	
        matrix = [[2, 2], [3, 5]]
		
        self.assertNotEqual(isSingular(matrix), 0)

    def test_3by3_singular(self):
	
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		
        dim = 3
		
        self.assertEqual(calculateDeterminant(dim,matrix), 0)

    def test_3by3_non_singular(self):
	
        matrix = [[1, 1, 1], [4, 5, 6], [7, 8, 9]]
		
        dim = 3
		
        self.assertNotEqual(calculateDeterminant(dim,matrix), 0)


if __name__ == '__main__':
    unittest.main()
