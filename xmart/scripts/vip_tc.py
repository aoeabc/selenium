from selenium.webdriver.common.by import By
import unittest
from pageObject.common.loginPage import Login
from pageObject.vipCenter.menu_student import Menu_studet
from pageObject.vipCenter.mean_teacher import Menu_teacher
from pageObject.vipCenter.addStudent.addstudent import AddStudent
from pageObject.vipCenter.addteacher.addteacher import AddTeacher
from libs.tool import connectSql
from libs.tool import DoExcel
import sys

class TestVip(unittest.TestCase):
    '''测试会员管理-添加学生功能'''

    def setUp(self):
        #  登录类
        self.l = Login()
        self.driver = self.l.loginAction()
        #   菜单切换
        self.m = Menu_studet(self.driver)
        #   添加学生类
        self.add = AddStudent(self.driver)
        #   实例化添加学生表格
        self.sheet = DoExcel('Vip_cases')

    def add_student_ation(self,name):
        #  根据用例编号获取测试数据
        test_data = self.sheet.get_test_data(name)
        #  点击菜单操作
        self.m.menu_into_addstudent()
        #   执行添加学生操作
        text=self.add.add_student(test_data['username'],test_data['realname'],test_data['email'],test_data['phone'])
        return text

    def test_add_student_001(self):
        '''验证添加学生功能，数据合法保存成功'''
        #  获取当前方法名，与用例编号一致
        name = sys._getframe().f_code.co_name
        #   执行添加学生操作
        text=self.add_student_ation(name)
        #   判断是否添加成功
        self.assertEqual(text,'保存成功')
        #  删除新增的数据
        sql="delete a from xsmart_users a , (select max(id) as m_id from xsmart_users) b where a.id=b.m_id"
        connectSql(sql=sql)

    def test_add_student_002(self):
        '''验证添加学生功能,用户名为空保存失败'''
        name = sys._getframe().f_code.co_name
        text = self.add_student_ation(name)
        self.assertIsNone(text)

    def test_add_student_003(self):
        '''验证添加学生功能,昵称超长保存失败'''
        name = sys._getframe().f_code.co_name
        text = self.add_student_ation(name)
        self.assertIsNone(text)

    def test_add_student_004(self):
        '''验证添加学生功能,email不合法保存失败'''
        name = sys._getframe().f_code.co_name
        text = self.add_student_ation(name)
        self.assertIsNone(text)

    def test_add_student_005(self):
        '''验证添加学生功能,手机号码不合法保存失败'''
        name = sys._getframe().f_code.co_name
        text = self.add_student_ation(name)
        self.assertIsNone(text)

    def tearDown(self):
        self.driver.close()

class TestVipTeacher(unittest.TestCase):
    '''测试会员管理-添加教师功能'''

    def setUp(self):
        #  登录类
        self.l = Login()
        self.driver = self.l.loginAction()
        #   菜单切换
        self.m = Menu_teacher(self.driver)
        #   添加教师类
        self.add = AddTeacher(self.driver)
        #   实例化添加会员管理表格
        self.sheet = DoExcel('Vip_cases')

    def add_teacher_ation(self,name):
        #  根据用例编号获取测试数据
        test_data = self.sheet.get_test_data(name)
        #  点击菜单操作
        self.m.menu_into_addteacher()
        #   执行添加学生操作
        text=self.add.add_teacher(test_data['username'],test_data['realname'],test_data['email'],test_data['phone'])
        return text

    def test_add_teacher_001(self):
        '''验证添加学生功能，数据合法保存成功'''
        #  获取当前方法名，与用例编号一致
        name = sys._getframe().f_code.co_name
        #   执行添加学生操作
        text=self.add_teacher_ation(name)
        #   判断是否添加成功
        self.assertEqual(text,'保存成功')
        #  删除新增的数据
        sql="delete a from xsmart_users a , (select max(id) as m_id from xsmart_users) b where a.id=b.m_id"
        connectSql(sql=sql)

    def test_add_teacher_002(self):
        '''验证添加教师功能,用户名为空保存失败'''
        name = sys._getframe().f_code.co_name
        text = self.add_teacher_ation(name)
        self.assertIsNone(text)

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
