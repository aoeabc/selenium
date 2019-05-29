from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.cjol.com/')
#  搜索中软国际
driver.find_element_by_id('txtKeyWords_tip').send_keys('软件测试')
#   选择地区
driver.find_element_by_class_name('icon-placedown').click()
time.sleep(3)
#  点击弹出框操作
ele=driver.find_element_by_id('winLocation_dropdivlli_2008')
driver.execute_script('arguments[0].scrollIntoView(false);',ele)
ele.click()
time.sleep(2)
# 选深圳
driver.find_element_by_xpath('//input[@id="winLocation_dropdiv200804"]/parent::li').click()
#选宝安
driver.find_element_by_id('winLocation_dropdivselected_ok').click()
#  点搜索按钮
driver.find_element_by_link_text('搜索').click()
time.sleep(5)
# 选月薪范围
driver.find_element_by_xpath('//li[@maxsalary="15000"]').click()
#  选工作年限
driver.find_element_by_xpath('//li[@maxyear="5"]').click()
#  选学历要求
driver.find_element_by_xpath('//li[@maxedu="50"]').click()
#   选职业类型
result=driver.find_element_by_id('p_mainfilters')
print(result.get_attribute('innerText'))
job=driver.find_elements_by_xpath('//h3/a//h3/a')
l=[]
for j in job:
    l.append(j.get_attribute('innerText'))

print('搜索结果',l)

# js = "window.scrollTo(0,document.body.scrollHeight)"
#
# driver.execute_script(js)

# js="var q=document.documentElement.scrollTop=document.body.scrollHeight"
# driver.execute_script(js)

# ele3=driver.find_element_by_xpath('//strong')
# driver.execute_script('arguments[0].scrollIntoView();',ele3)
# ele3.click()











