from selenium.webdriver.common.by import By
from selenium import webdriver
from pageObject.common.getdriver import Driver

class Login(Driver):

    login_username=(By.ID, 'username')
    login_password=(By.ID, 'password')
    login_submit=(By.XPATH, '//input[@value="登 录"]')

    def input_username(self,username):
        self.driver.find_element(*self.login_username).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.login_password).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.login_submit).click()

    def loginAction(self,username='admin',password='admin'):
        self.get_url()
        self.input_username(username)
        self.input_password(password)
        self.click_submit()
        return self.driver

if __name__ == '__main__':
    l=Login()
    l.loginAction('admin','admin')