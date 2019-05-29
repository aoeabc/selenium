from selenium import webdriver
import time

bro = webdriver.Chrome()
bro.get('https://readfree.me/auth/login')
bro.find_element_by_id('id_login').send_keys('1111')
time.sleep(5)
bro.quit()




