from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class BaseElement(object):

    def __init__(self,driver):
        self.driver=driver

    def find_ele(self,*locator):
        wait=WebDriverWait(self.driver,10)
        try:
            ele=wait.until(EC.visibility_of_element_located(locator))
            return ele
        except BaseException as e:

            print(e)            

    def find_alert(self):
        wait=WebDriverWait(self.driver,10)
        try:
            a=wait.until(EC.alert_is_present())
            return a
        except BaseException as e:
            print(e)  


if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get('http://localhost/admin.php')
    time.sleep(5)
    b=BaseElement(driver)
    b.find_ele(By.ID,'username').send_keys('admin')
##    driver.find_element_by_id('username').send_keys('admin')
##    driver.find_element(By.ID,'username').send_keys('admin')
##    wait=WebDriverWait(driver,10)
##    ele=wait.until(EC.visibility_of_element_located((By.ID,'username')))
##    ele.send_keys('admin')
    
