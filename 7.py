from selenium import webdriver
chromedriver = r"E:\software\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://171.37.135.94:8123')
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get('http://httpbin.org/ip')
print(chrome.page_source)
chrome.quit()
