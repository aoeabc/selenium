from selenium import webdriver
import time
from selenium.webdriver.common.by import By

bro = webdriver.Chrome()
bro.get('http://bologe.net/portal.php')
bro.maximize_window()
print(bro.current_url)
bro.find_element_by_link_text('测试社区').click()
print(bro.title)
#回到首页
bro.back()
#回到首页
texts=[]
eles=bro.find_elements_by_xpath('//div[@id="portal_block_86_content"]//li')
for ele in eles:
    texts.append(ele.text)
print('热帖推荐内容：',texts)
#进入第一个热帖推荐内容
eles[0].click()
#点导航
bro.find_element_by_id('qmenu').click()
bro.find_element_by_name('srchtxt').send_keys('python')
bro.find_element_by_css_selector('#searchsubmit')
bro.quit()