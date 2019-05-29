from selenium.webdriver.common.by import By
from pageObject.common.getdriver import Driver
from pageObject.common.loginPage import Login


class Menu_studet(Driver):

    vip_center=(By.LINK_TEXT,'会员中心')
    add_atudent_button=(By.PARTIAL_LINK_TEXT, '添加学生')

    def click_vip_center(self):
        #   进入会员管理页面
        self.driver.find_element(*self.vip_center).click()

    def click_addstudent_button(self):
        #   iframe跳转
        self.driver.switch_to.frame('mainframe')
        #  点击添加学生
        self.driver.find_element(*self.add_atudent_button).click()

    def menu_into_addstudent(self):
        self.click_vip_center()
        self.click_addstudent_button()

if __name__=='__main__':
    l=Login()
    driver=l.loginAction('admin','admin')
    m=Menu_studet(driver)
    m.menu_into_addstudent()

