from selenium import webdriver
import os

chromedriver = r"E:\software\chromedriver_win32\chromedriver.exe"
os.environ["webdriver.ie.driver"] = chromedriver

browser = webdriver.Ie(chromedriver)

browser.get("https://ilanni.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
browser.quit()