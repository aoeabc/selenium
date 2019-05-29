from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

bro = webdriver.Chrome()
bro.get('C:/Users/Administrator/Desktop/lww/UI/SeleniumDemo/multiple.html')
# bro.get('http://www.baidu.com')
# e=bro.find_element(By.CSS_SELECTOR,'input[#id]')
#
# time.sleep(3)
# bro.execute_script('arguments[0].scrollIntoView();', bro.find_element_by_id('ShippingMethod'))
# # ele=bro.find_element_by_id('ShippingMethod').find_element_by_xpath('//option[@value="12.51"]')
# # time.sleep(2)
# # bro.close()
# ele=bro.find_element(By.XPATH,'//button')
# v=WebDriverWait(bro,0.5,10).until(EC.visibility_of(ele))
# print(v)
# ele=bro.find_element_by_xpath('//a[@href="http://www.baidu.com/more/"]')
# ActionChains(bro).move_to_element(ele).perform()
# bro.find_element_by_xpath('//a[@name="tj_mp3"]').click()
#
# bro.get_screenshot_as_file('./a.png')
d=bro.find_element_by_id('f')
# bro.execute_script('arguments[0].removeAttribute(arguments[0],arguments[1])', d,'readonly');
bro.execute_script("var setDate=document.getElementById(\"f\");setDate.removeAttribute('readonly');")
print(d.get_attribute('readonly'))