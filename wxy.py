#coding=utf-8
from selenium import webdriver
import os

chromedriver = r"E:\software\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.baidu.com")
print driver.title, driver.current_url
# 百度首页搜索输入框的元素id='kw'，搜索按钮的元素id='su'，注意搜索中包含中文使用u
driver.find_element_by_id('kw').send_keys(u'jira破解')
driver.find_element_by_id('su').click()
print driver.title, driver.current_url
#driver.close()