# coding=utf-8
from selenium import webdriver
import os, time, unittest
import log
import logging
import traceback

logger = log.Logger('e:/1/web_log.log', clevel=logging.DEBUG, Flevel=logging.INFO)


def f(n):
    logger.info(n)
    print n


class baidu(unittest.TestCase):
    def setUp(self):
        self.chromedriver = 'C:\Users\li.liu\AppData\Local\Google\Chrome\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = self.chromedriver
        self.driver = webdriver.Chrome(self.chromedriver)
        print u'驱动定义完成'

    def test_baidu_search(self):
        u"""百度搜索"""

        driver = self.driver
        f(u'打开百度')
        driver.maximize_window()
        driver.get('http://baidu.com')
        time.sleep(2)
        print u'打开另一个网址'
        driver.get('http://news.baidu.com')
        print u'窗口最大化'
        driver.maximize_window()
        time.sleep(1)
        print u'返回上一个网页'
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(2)
        driver.back()
        time.sleep(1)
        driver.close()
        driver.quit()

    def test_baidu_set(self):
        driver = self.driver
        driver.get('http://baidu.com')
        time.sleep(3)
        driver.find_element_by_id('kw').send_keys(u'测试')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        driver.find_element_by_id('kw1').clear()
        driver.find_element_by_id('kw').send_keys(u'测试用例')
        time.sleep(3)
        print u'关闭浏览器'
        driver.close()
        print u'退出浏览器服务'
        driver.quit()


if __name__ == "__main__":
    unittest.main()