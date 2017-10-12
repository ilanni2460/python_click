# coding=utf-8
# 登陆51cto
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.proxy import *
import time, re
#time模块是为了实现等待页面加载。

# '''可以改成别的浏览器'''
chromedriver = r"E:\software\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)


# 启动浏览器后打开51cto的home主页
driver.get("http://home.51cto.com/index")
# 全屏
driver.maximize_window()
name = driver.find_element_by_name('LoginForm[username]')
name.send_keys('duanzhanling')
passwd = driver.find_element_by_name('LoginForm[password]')
passwd.send_keys('13513971507')
submit = driver.find_element_by_xpath("//*[@name='login-button']")
submit.click()


# 下面开始签到，领取无忧
#driver.find_element_by_xpath("//*[@id='jsSignGetCredits']").click()
#driver.find_element_by_link_text(u"签到领无忧币").click()
driver.find_element_by_name(u"签到领无忧币").click()
#driver.find_element_by_id("jsSignGetCredits").click()
#driver.find_element_by_xpath(u"签到领无忧币").click()
#关闭浏览器使用
browser.quit()