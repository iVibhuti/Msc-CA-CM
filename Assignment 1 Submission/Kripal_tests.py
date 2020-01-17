import unittest
from Kripal import single

class FirstTest(unittest.TestCase):

    def test_one(self):
        mat=[[1,2],[3,4]]
        self.assertEqual(1,single(mat,1))
        
    def test_second(self):
        mat=[[1,2,3],[3,4,5],[6,7,8]]
        self.assertTrue(single(mat,1)==1)
        
    def test_third(self):
        mat=[[12,23,45],[3,4,5],[56,65,74]]
        self.assertTrue(single(mat,1)!=0)
if __name__ == '__main__':
    unittest.main()
