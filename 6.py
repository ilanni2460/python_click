# encoding=utf
# coding=utf-8
# '''刷百度关键词点击开始'''
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.proxy import *
import time, re

chromedriver = r"E:\software\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)


# '''可以改成别的浏览器'''
browser.get("http://www.baidu.com")
# '''启动浏览器后进入第一网页'''
browser.find_element_by_id("kw").send_keys(u"confluence wiki 迁移")
# '''输入关键词'''

# '''超时设置，如果超过指定时间，则抛出异常'''
browser.implicitly_wait(10)

# '''通过键盘回车来代替搜素按钮的点击操作'''
browser.find_element_by_id("su").send_keys(Keys.ENTER)

line_list = browser.find_elements_by_xpath("//h3[@class='t']")
# '''xpath提取特征'''
for line in line_list:
    t = line.find_element_by_xpath("a")
    print '%s - %s' % (t.text, type(t.text))
    if u'烂泥行天下' in t.text:
        print 'yes'
        t.click()
        time.sleep(5)
#browser.quit()