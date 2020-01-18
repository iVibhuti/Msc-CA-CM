import singmat
import unittest
import calc
class Testcalc(unittest.TestCase):
    def test_sample(self):
        #result=calc.sample([[1,4],[2,8]])
        self.assertEqual(calc.sample([[1,4],[2,8]]),0.0)
        self.assertEqual(calc.sample([[1,3],[2,5]]),-1.0)
        self.assertEqual(calc.sample([[1,2],[2,4]]),0.0)
        self.assertEqual(calc.sample([[1,1],[2,3]]),1.0)
if __name__=='__main__':
    unittest.main()
