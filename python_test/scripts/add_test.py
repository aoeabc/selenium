from scripts.count import CalcClass
import unittest

class TestUnitAdd(unittest.TestCase):


    def doAction(self,numA,numB):
        c = CalcClass(numA,numB)
        return c.add_data()
        
    def test_add_1(self):
        '''----测试说明-----
        测试报告中只会展示第一行
        '''
        fun_num=self.doAction(2,3)
        self.assertEqual(fun_num,5)

    def test_add_2(self):        
        fun_num=self.doAction(2.1,3.3)
        self.assertEqual(fun_num,5.4)

if __name__=='__main__':
    suit= unittest.TestSuite()
    suit.addTest(TestUnitAdd('test_add_1'))
    suit.addTest(TestUnitAdd('test_add_2'))
    run=unittest.TextTestRunner()
    run.run(suit)
