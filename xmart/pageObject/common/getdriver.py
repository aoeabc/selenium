from selenium import webdriver
from selenium.webdriver.common.by import By
from conf.config import test_url
import time

class Driver(object):

    def __init__(self,driver=''):
        if driver!='':
            self.dri=driver
        else:
            self.dri=webdriver.Chrome()

        self.driver=self.dri
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def get_url(self):
        self.driver.get(test_url)

    def driver_close(self):
        self.driver.close()

if __name__=='__main__':
    l=Driver()
    l.get_url()
    time.sleep(5)
    l.driver_close()

