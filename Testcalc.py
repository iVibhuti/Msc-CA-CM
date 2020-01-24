"""
Samak Aditya Ramchandra
PRN-19030142028 Msc(ca)
"""

import adimat
import unittest
class Testcalc(unittest.TestCase):
    def test_isSingular(self):
        #result=adimat.isSingular([[1,4],[2,8]])
        self.assertEqual(adimat.isSingular([[1,4],[2,8]]),0.0)
        self.assertEqual(adimat.isSingular([[1,3,4],[2,5,2],[2,3,5]),-17)
        self.assertEqual(adimat.isSingular([[1,2],[2,4]]),0.0)
        self.assertEqual(adimat.isSingular([[1,1],[2,3]]),1.0)
if __name__=='__main__':
    unittest.main()
