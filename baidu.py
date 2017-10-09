# coding:gbk
# http://www.cnblogs.com/paisen/p/3312631.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


chromedriver = r"E:\software\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.baidu.com")
driver.find_element_by_id('lb').click()
# driver.find_element_by_id('TANGRAM__PSP_10__unameLoginLink').click()
time.sleep(3)

driver.find_element_by_name('userName').send_keys('lanni654321')
driver.find_element_by_name('password').send_keys('wxy123456')
driver.find_element_by_id('TANGRAM__PSP_10__submit').click()

try:
    dr = WebDriverWait(driver, 10)  # 10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄
    '''WebDriverWait参见下：
http://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver_support/selenium.webdriver.support.wait.html'''
    dr.until(lambda the_driver: the_driver.find_element_by_css_selector('.user-name-top').is_displayed())
except  Exception:
    print '登录失败'

user = driver.find_element_by_css_selector('.user-name-top')
webdriver.ActionChains(driver).move_to_element(user).perform()  # 鼠标定位到用户名
driver.find_element_by_css_selector('a.sep').click()