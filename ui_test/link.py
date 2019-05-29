import time
from selenium import  webdriver
# id方式定位
url2 = 'C:/Users/Administrator/Desktop/lww/UI/SeleniumDemo/multiple.html'
url1='https://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url2)
time.sleep(3)

#获取全部链接

ele = driver.find_element_by_id('div-id-5')
all_link = ele.find_elements_by_tag_name('a')
# print(len(all_link))
for i in range(len(all_link)):  # 遍历点击每个链接
    ele = driver.find_element_by_id('div-id-5')
    all_link = ele.find_elements_by_tag_name('a')
    driver.maximize_window()
    all_link[i].click()
    all_of = driver.window_handles  # 获取当前全部窗口
    if len(all_of) > 1:  # 窗口数大于1时切换到最新窗口
        driver.switch_to.window(all_of[-1])
        driver.close()  # 关闭新的窗口
        driver.switch_to.window(all_of[0])  # 切回第一个窗口
    else:
        driver.back()
        time.sleep(2)






