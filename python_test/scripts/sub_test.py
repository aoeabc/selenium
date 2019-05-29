from scripts.count import CalcClass
import unittest

class TestUnitAdd(unittest.TestCase):

    def doAction(self,numA,numB):
        c = CalcClass(numA,numB)
        return c.sub_data()
        
    def test_sub_1(self):        
        fun_num=self.doAction(2,3)
        self.assertEqual(fun_num,5)

    def test_sub_2(self):        
        fun_num=self.doAction(2.3,3.3)
        self.assertEqual(fun_num,-1)

if __name__=='__main__':
    suit= unittest.TestSuite()
    suit.addTest(TestUnitAdd('test_sub_1'))
    suit.addTest(TestUnitAdd('test_sub_2'))
    run=unittest.TextTestRunner()
    run.run(suit)
