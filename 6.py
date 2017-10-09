#coding:utf-8
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

reload(sys)
sys.setdefaultencoding('utf-8')

chromedriver = r"E:\software\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)

def get_search_content_title():
    browser.get("http://www.baidu.com")
	assert "百度" in browser.title
	search_text_blank = browser.find_element_by_id("kw")
	search_text_blank.send_keys(u"14_python爬虫")
	search_text_blank.send_keys(Keys.RETURN)

	time.sleep(3)
	#print browser.page_source
	assert 'python爬虫——爬出新高度' in browser.page_source

	element_List=browser.find_elements_by_xpath(".//*/h3/a")
	itemNum=len(element_List)
	print 'length is :'+str(itemNum)

	for a in element_List:
		tmptitle= a.text
		if 'python爬虫——爬出新高度' in tmptitle:
			print  a.get_attribute('href')
			tmpurl=  a.get_attribute('href')
			#a.click()
			browser.get(tmpurl)
			print 'I got it'
			break
	print browser.current_url
	print 'end'
	browser.close()
if __name__ == '__main__':
	print '''
			***************************************** 
			**  Welcome to Spider of baidu search  ** 
			**      Created on 2017-05-203         ** 
			**      @author: Jimy _Fengqi          ** 
			*****************************************
	'''
	get_search_content_title()
