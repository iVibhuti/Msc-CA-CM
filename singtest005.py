import singularmath
import unittest
import calc
class Testcalc(unittest.TestCase):
    def test_sample(self):
        #result=calc.sample([[2,4],[1,2]])
        self.assertEqual(calc.sample([[2,4],[1,2]]),0.0)
        self.assertEqual(calc.sample([[2,3],[1,5]]),-1.0)
        self.assertEqual(calc.sample([[2,2],[1,4]]),0.0)
        self.assertEqual(calc.sample([[2,1],[1,3]]),1.0)
if __name__=='__main__':
    unittest.main()
