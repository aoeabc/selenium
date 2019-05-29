from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pageObject.common.getdriver import Driver
from pageObject.common.loginPage import Login
from pageObject.vipCenter.menu_student import Menu_studet

class AddTeacher(Driver):

    addstu_username=(By.ID, 'username')
    addstu_realname=(By.ID, 'realname')
    addstu_email=(By.ID, 'email')
    addstu_phone=(By.ID, 'phone')
    addstu_sunmit=(By.ID, 'btn_sub')
    addstu_check_null=(By.CLASS_NAME,'Validform_checktip Validform_right')

    def input_uername(self,username):
        #   输入用户账号
        self.driver.find_element(*self.addstu_username).send_keys(username)

    def input_realname(self,realname):
        #   输入用户昵称
        self.driver.find_element(By.ID, 'realname').send_keys(realname)

    def input_email(self, email):
        #   输入邮箱
        self.driver.find_element(By.ID, 'email').send_keys(email)

    def input_phone(self, phone):
        #   输入手机号
        self.driver.find_element(By.ID, 'phone').send_keys(phone)

    def click_submit(self):
        #   点击确认保存
        self.driver.find_element(By.ID, 'btn_sub').click()

    def check_message(self):
        text=self.driver.find_element(*self.addstu_check_null).text
        return text

    def get_alert(self):
        #  获取提示框信息，没获取到提示框返回None
        try:
            wait = WebDriverWait(self.driver, 10)
            a = wait.until(EC.alert_is_present())
            # alert_a = self.driver.switch_to.alert
            mes = a.text
            ##  点击确定
            a.accept()
            return mes
        except BaseException as e:
            return None


    def add_teacher(self,username,realname,email,phone):
        #   有弹框，返回弹框内容，点保存没有弹框，返回None
        self.input_email(email)
        self.input_uername(username)
        self.input_realname(realname)
        self.input_phone(phone)
        self.click_submit()
        alert_text=self.get_alert()
        return alert_text

if __name__ == '__main__':
    l=Login()
    driver=l.loginAction('admin','admin')
    m=Menu_studet(driver)
    m.menu_into_addstudent()
    add=AddTeacher(driver)
    add.add_teacher('15712341234','asdf','67fks@qq.com','15712341234')
