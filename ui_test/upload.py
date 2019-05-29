import os
from time import sleep
from selenium import webdriver

b = webdriver.Chrome()
b.maximize_window()
b.implicitly_wait(10)

b.get('C:/Users/Administrator/Desktop/lww/UI/SeleniumDemo/multiple.html')

b.find_element_by_name('file').click()
os.system('C:\\Users\\Administrator\\Desktop\\lww\\UI\\up.exe')

sleep(5)
b.quit()