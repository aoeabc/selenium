from selenium.webdriver.common.by import By
from pageObject.common.getdriver import Driver
from pageObject.common.loginPage import Login


class Menu_teacher(Driver):

    vip_center=(By.LINK_TEXT,'会员中心')
    teacher_list=(By.LINK_TEXT,'教师列表')
    add_teacher_button=(By.PARTIAL_LINK_TEXT, '添加教师')

    def click_vip_center(self):
        #   进入会员管理页面
        self.driver.find_element(*self.vip_center).click()

    def click_teacher_list(self):
        #   进入会员管理页面
        self.driver.find_element(*self.teacher_list).click()

    def click_addteacher_button(self):
        #   iframe跳转
        self.driver.switch_to.frame('mainframe')
        #  点击添加教师
        self.driver.find_element(*self.add_teacher_button).click()

    def menu_into_addteacher(self):
        self.click_vip_center()
        self.click_teacher_list()
        self.click_addteacher_button()

if __name__=='__main__':
    l=Login()
    driver=l.loginAction('admin','admin')
    m=Menu_teacher(driver)
    m.menu_into_addteacher()

