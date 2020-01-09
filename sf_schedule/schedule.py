from selenium import webdriver
import os
import time
import image_code
from PIL import Image
# url='http://sfim-sms-bg.sf-express.com/h5/v5.4/pages/fs/schedule.html?ver=5.4.2019070519#/index'
# url='http://fs-biz-task-ng-gate.sf-express.com:8080/authsrv/userpath/pages/fs/schedule.html'
# url='http://hos.sf-express.com/frame.pvt;jsessionid=19srov7piigcs1o7fs2hxwcs2f'
url='https://cas.sf-express.com/cas/login?service=http%3A%2F%2Fsfim-sms-bg.sf-express.com%2Fadmin%2Flogin#/index'

def get_driver(url=url):
    driver=webdriver.Chrome()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)
    return driver

def close_driver(driver):
    driver.quit()
    # os.system('taskkill /im chromedriver.exe /F')

def login(driver):

    driver.find_element_by_id('username').send_keys('80004202')
    driver.find_element_by_id('password').send_keys('..Xiaochen622')
    get_login_image(driver,'h:\\Image\\capture.png')
    co=image_code.ImageCode('h:\\Image\\capture.png')
    code=co.get_login_code()
    driver.find_element_by_id('verifyCode').send_keys(code)
    time.sleep(3)
    driver.find_element_by_xpath('//a[@onclick="login()"]').click()


def check_login_status(driver):
    status=False
    try:
        ele=driver.find_element_by_id('status')
        print(ele.get_attribute('innerText'))
        if '验证码不正确' in ele.get_attribute('innerText'):
            status=True
    except:
        pass
    return status


def get_login_image(driver,ima_file):

    # driver=schedule.get_driver()
    # ele=driver.find_element_by_class_name('yzmImg')
    ele = driver.find_element_by_id('imgcode')
    driver.save_screenshot(ima_file)

    left = ele.location['x']
    top = ele.location['y']
    right = left + ele.size['width']
    bottom = top + ele.size['height']

    im = Image.open(ima_file)
    im = im.crop((left, top, right, bottom))  # 元素裁剪

    im = im.convert('RGBA')
    im = im.convert('L')
    im.save(ima_file)

if __name__ == '__main__':
    driver=get_driver()
    login(driver)
    time.sleep(2)
    # 待修改，登录成功后找不到状态
    while check_login_status(driver):
        login(driver)
    close_driver(driver)