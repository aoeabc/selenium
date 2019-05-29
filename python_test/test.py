#给出32位有符号的整数，你讲整数的中每位上的数字进行翻转
# def trans(num):
#     if num>0:
#         result= str(num)[::-1]
#     else:
#         result = -int(str(abs(num))[::-1])
#     return result
#

import unittest
from HTMLTestReportCN import HTMLTestRunner

# def setUpModule():
#     print('测试模块执行开始')
#
# def tearDownModule():
#     print('测试模块执行结束')

class UnitTest(unittest.TestCase):
    # def setUp(self):
    #     print('测试用例开始')
    a=1
    def test_case1(self):
        print('test_case1测试用例开始')

    # @unittest.skipIf(a==1,'这是个理由')
    # @unittest.skip('1111')
    # @unittest.skipUnless(a!=1,'这是个理由')
    def test_case2(self):
        print('test_case2测试用例开始')

    # def tearDown(self):
    #     print('测试用例结束')
    #
    # @classmethod
    # def setUpClass(cls):
    #     print('测试类开始执行')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('测试类执行结束')


if __name__ == '__main__':
    # unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(UnitTest('test_case1'))
    # # suit.addTest(UnitTest('test_case2'))
    # run = unittest.TextTestRunner()
    # run.run(suit)
    suit=unittest.TestSuite()
    suit.addTest(UnitTest('test_case1'))

    run=unittest.TextTestRunner()
    run.run(suit)

