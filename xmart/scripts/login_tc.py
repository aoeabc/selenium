from selenium.webdriver.common.by import By
import unittest
from pageObject.common.loginPage import Login
import time
import sys
from libs.tool import DoExcel

class TestLogin(unittest.TestCase):
    '''测试登录功能'''

    def setUp(self):
        #  登录类
        self.l = Login()
        #  excel操作类
        self.sheet=DoExcel('Login_cases')

    def login(self,name):
        #  根据用例编号获取测试数据
        test_data = self.sheet.get_test_data(name)
        #  执行登录
        self.driver = self.l.loginAction(test_data['username'], test_data['password'])

    def test_login_001(self):
        '''用户名密码都正确，登录成功'''
        #  获取当前方法名，与用例编号一致
        name=sys._getframe().f_code.co_name
        #  执行登录
        self.login(name)
        time.sleep(2)
        #  获取页面源代码
        text_mes=self.driver.page_source
        #  判断是否登录成功
        self.assertIn('欢迎',text_mes)

    def test_login_002(self):
        '''密码为空，登录失败'''
        # self.driver = self.l.loginAction('admin','')
        name=sys._getframe().f_code.co_name
        self.login(name)
        time.sleep(2)
        text_mes = self.driver.page_source
        self.assertNotIn('欢迎', text_mes)

    def test_login_003(self):
        '''密码错误，登录失败'''
        # self.driver = self.l.loginAction('admin','123456')
        name=sys._getframe().f_code.co_name
        self.login(name)
        time.sleep(2)
        text_mes = self.driver.page_source
        self.assertNotIn('欢迎', text_mes)

    def tearDown(self):
        self.driver.close()


if __name__=='__main__':
    unittest.main()
