# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import xlsxwriter
import datetime
import time

os.chdir("C:\\Temp")
##################################################

##### Wish login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options)  # Get local session of firefox

driver.get("http://www.wish.com")
time.sleep(2)

## Email Login
driver.find_element_by_xpath("//*[@id=\"signup-form\"]/div[6]").click()
## Input email & password
driver.find_element_by_xpath("//*[@id=\"login-email\"]").send_keys("cmes1988@163.com")
driver.find_element_by_xpath("//*[@id=\"login-password\"]").send_keys("film007love")

## Click login
driver.find_element_by_xpath("//*[@id=\"email-login-form\"]/button").click()
time.sleep(2)

###### Refresh
## driver.refresh()
driver.close()

""" 
//*[@id="tabbed_feed_latest"] ## Latest 
//*[@id='tag_53dc186321a86318bdc87ef8']  ## Fashion 
//*[@id='tag_53dc186421a86318bdc87f20']  ## Gadgets 
//*[@id='tag_54ac6e18f8a0b3724c6c473f']  ## Hobbies 
//*[@id="tag_53dc186321a86318bdc87ef9"]  ## Tops 
//*[@id="tag_53dc186421a86318bdc87f31"]  ## Shoes 
//*[@id="tag_53dc186421a86318bdc87f1c"]  ## Watches 

//*[@id="tag_53dc186321a86318bdc87f07"]  ## Bottoms 
//*[@id="tag_53dc2e9e21a86346c126eae4"]  ## Underwear 
//*[@id="tag_53dc186421a86318bdc87f22"]  ## Wallet & Bags 
//*[@id="tag_53dc186421a86318bdc87f16"]  ## Accessories 
//*[@id="tag_53dc186421a86318bdc87f0f"]  ## Phone Upgrades 
//*[@id="tag_53e9157121a8633c567eb0c2"]  ## Home Decor 
//*[@id=tag_53e9157121a8633c567eb0c2] 

## Categories 
driver.find_element_by_xpath("//*[@id='tabbed_feed_latest']").click() 
## Drop-down categories 
driver.find_element_by_xpath("//*[@id='feed-category-menu']/li[9]").click() 
driver.find_element_by_xpath("//*[@id='tag_53dc186421a86318bdc87f22']").click() 
"""

tags = [["Latest", "tabbed_feed_latest"],
        ["Fashion", "tag_53dc186321a86318bdc87ef8"],
        ["Gadgets", "tag_53dc186421a86318bdc87f20"],
        ["Hobbies", "tag_54ac6e18f8a0b3724c6c473f"],
        ["Tops", "tag_53dc186321a86318bdc87ef9"],
        ["Shoes", "tag_53dc186421a86318bdc87f31"],
        ["Watches", "tag_53dc186421a86318bdc87f1c"],
        ["Bottoms", "tag_53dc186321a86318bdc87f07"],
        ["Underwear", "tag_53dc2e9e21a86346c126eae4"],
        ["Wallets_Bags", "tag_53dc186421a86318bdc87f22"],
        ["Accessories", "tag_53dc186421a86318bdc87f16"],
        ["Phone_Upgrades", "tag_53dc186421a86318bdc87f0f"],
        ["Home_Decor", "tag_53e9157121a8633c567eb0c2"]
        ]

driver.refresh()
driver.execute_script("window.scrollTo(0, 0);")
## Excel File name
dt = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H-%M-%S')
workbook = xlsxwriter.Workbook(dt + '.xlsx')

for cat in tags:
    print cat
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)
    if cat[0] in ("Bottoms", "Underwear", "Wallets_Bags", "Accessories", "Phone_Upgrades", "Home_Decor"):
        driver.find_element_by_xpath("//*[@id='feed-category-menu']/li[9]").click()
        driver.find_element_by_xpath("//*[@id='" + cat[1] + "']").click()
    else:
        driver.find_element_by_xpath("//*[@id='" + cat[1] + "']").click()

    k = 10
    while k > 0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        print "k= " + str(k)
        k = k - 1
        #######################################
    ##### Get Items

    products = driver.find_elements_by_xpath("//meta[@itemprop='name']")
    urls = driver.find_elements_by_xpath("//a[@class='display-pic']")
    feed_actual_price = driver.find_elements_by_xpath("//div[@class='feed-actual-price']")
    feed_crossed_price = driver.find_elements_by_xpath("//div[@class='feed-crossed-price']")
    feed_number_bought = driver.find_elements_by_xpath("//div[@class='feed-number-bought']")

    Items = [[]]
    Items.append(["URL", "Product", "Actual_Price", "Crossed_Price", "Num_bought"])
    for i in range(len(products)):
        item = []
        item.append(urls[i].get_attribute('innerHTML')[30:-3])  ## URL
        item.append(products[i].get_attribute("content"))  ## Product Name
        item.append(feed_actual_price[i].text)
        item.append(feed_crossed_price[i].text)
        item.append(feed_number_bought[i].text)
        Items.append(item)

        ## Output to Excel
    worksheet = workbook.add_worksheet(cat[0])
    for i in range(len(Items)):
        worksheet.write_row('A' + str(i + 1), Items[i])

    worksheet.set_column('A:A', 25)
    worksheet.set_column('B:B', 80)
    ## Move to top and refresh
    driver.execute_script("window.scrollTo(0, 0);")
    driver.refresh()
    time.sleep(8)
    ## End for

workbook.close()

""" 
#### By class name and innerHTML 
demo_div = driver.find_elements_by_class_name("feed-product-item") 
print demo_div[0].get_attribute('innerHTML') 
"""

""" 

origFeedItems=driver.execute_script("return origFeedItems;")    
Items=[[]] 
Items.append(["id", "Name", "Inventory", "URL", "Sold", "Buyer", "Rating", "Rating_Count", "Source", "Currency", "Value", "Price", "Retail Price" ]) 

for i in range(len(origFeedItems)): 
    data=origFeedItems[i] 
    item=[] 
    item.append(data["id"]) 
    item.append(data["name"]) 
    item.append(data["commerce_product_info"]["total_inventory"]) 
    item.append(data["external_url"]) 
    item.append(data["num_bought"]) 
    item.append(data["feed_tile_text"]) 
    item.append(data["product_rating"]["rating"]) 
    item.append(data["product_rating"]["rating_count"]) 
    item.append(data["source_country"]) 
    item.append(data["commerce_product_info"]["variations"][0]["localized_price"]["currency_code"]) 
    item.append(data["commerce_product_info"]["variations"][0]["localized_price"]["localized_value"]) 
    item.append(data["commerce_product_info"]["variations"][0]["localized_price_before_personal_price"]["localized_value"]) 
    item.append(data["commerce_product_info"]["variations"][0]["localized_retail_price"]["localized_value"]) 
    Items.append(item) 

dt=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H-%M-%S') 
workbook = xlsxwriter.Workbook(dt+'.xlsx') 
worksheet = workbook.add_worksheet('Summary') 

for i in range(len(Items)): 
    worksheet.write_row('A'+str(i), Items[i]) 

worksheet.set_column('A:A', 25) 
worksheet.set_column('B:B', 80) 
worksheet.set_column('D:D', 20) 
workbook.close() 
"""

""" 
from selenium import webdriver   
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.common.keys import Keys   
import time   

browser = webdriver.Chrome() # Get local session of firefox   
browser.get("http://www.wish.com") # Load page   
assert "Yahoo!" in browser.title   
elem = browser.find_element_by_name("p") # Find the query box   
elem.send_keys("seleniumhq" + Keys.RETURN)   
time.sleep(0.2) # Let the page load, will be added to the API   
try:   
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")   
except NoSuchElementException:   
    assert 0, "can't find seleniumhq"   
browser.close()   

options = webdriver.ChromeOptions()   
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')   
browser = webdriver.Chrome(chrome_options=options) # Get local session of firefox   

 url='http://www.baidu.com'   
 browser = webdriver.Chrome() 
 browser.get(url)   
 elem=browser.find_element_by_id('s_tab') #by id   
 elem=browser.find_element_by_tag_name('video')  #by tag name   
 elem.get_attribute('src')#get url,python风格的词典结构，elem返回的是词典结构。   

from selenium import webdriver 
driver=webdriver.PhantomJS() 
driver.get('www.baidu.com') 
data = driver.find_element_by_id('cp').text 
print data 







##  -80%\n$1 $5\n5k+ bought this 
elem = driver.find_element_by_xpath("//*[@id=\"contest-containers\"]") 
elem.text 

##  -80%\n$1 $5\n5k+ bought this 
elem = driver.find_element_by_xpath("//*[@id=\"feed-grid\"]") 
elem.text 

elem = driver.find_element_by_xpath("//*[@id=\"feed-grid\"]/div[2]/a") 
elem.text 

elem = driver.find_elements_by_xpath("//*[@id=\"body-feed-page\"]/script[6]/text()") 
elem.text 

elem=driver.find_elements_by_xpath("//*[@id=\"feed-grid\"]/div[1]/meta") 
elem[0].text 

## Item Names 
priceValue=driver.find_elements_by_xpath("//meta[@itemprop='name']")  
for i in range(len(priceValue)): 
    print priceValue[i].get_attribute("content") 





a[0] 

//*[@id="body-feed-page"]/script[6]/text() 

//*[@id="body-feed-page"]/script[6] 

"feed-product-item"  
elem=driver.find_elements_by_css_selector("#feed-grid > div:nth-child(1) > meta") 

elem = driver.find_elements_by_xpath("//*[@id=\"body-feed-page\"]/script[6]/text()") 
driver.page_source 


for elem in driver.find_elements_by_xpath("//*[@id=\"body-feed-page\"]"): 
    print elem.text 

driver.find_elements_by_partial_link_text("body-feed-page") 

elem.get_attribute('text')     

//*[@id="body-feed-page"]/script[6]/text() 
//*[@id="body-feed-page"]/script[6]/text() 
elem = driver.find_element_by_class_name("feed-product-item") 
elem = driver.find_element_by_tag_name("content") 

elem.f 
elem.text 
elem.meta 
for i in range(len(elem)): 
    print elem[i].text 

len(elem) 





//*[@id="container"] 
driver.page_source 
<meta itemprop="name" content="DOOGEE X5 Quad Core Android 5.1 SmartPhone WCDMA Phone Bar CellPhone 5.0" IPS HD, 8GB ROM, OTG, GPS,"> 
<meta itemprop="name" content="DOOGEE X5 Quad Core Android 5.1 SmartPhone WCDMA Phone Bar CellPhone 5.0" IPS HD, 8GB ROM, OTG, GPS,"> 
driver.find_elements_by_xpath 
#feed-grid > div:nth-child(2) 
//*[@id="feed-grid"]/div[2]/a 
#feed-grid > div:nth-child(4) > a 





GET / HTTP/1.1 
Host: www.wish.com 
Connection: keep-alive 
Cache-Control: max-age=0 
Upgrade-Insecure-Requests: 1 
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 
Referer: https://www.wish.com/ 
Accept-Encoding: gzip, deflate, sdch, br 
Accept-Language: en-US,en;q=0.8 
Cookie: _xsrf=2e776ee67f58479a9f02bacbaf3d6f48; BIGipServer~CORP~corpproxy-sjd-3128=rd1o00000000000000000000ffff0af47f36o3128; sweeper_session="OWY3Nzk2MjQtNTA3MS00MmI0LTllNDUtYzRmNGU0YjAzYjJmMjAxNi0wNi0yNiAwMjo0OTowMy41OTYyNTY=|1466909343|11f641e3ddb1a581e122c2f3975dca13b516723e"; __utma=96128154.435042005.1466908942.1466908942.1466908942.1; __utmb=96128154.3.10.1466908942; __utmc=96128154; __utmz=96128154.1466908942.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); bsid=bc54e73b31264e1983adc887a9221795; sweeper_uuid=34efe456382045079598ac55f620853b 
If-None-Match: "3e557df3e08bfc67d8817a580fe17f71f669da7e" 



elem = driver.find_element_by_id("login-form") 
elem.click() 


email = browser.find_element_by_id('login-email') #by id  
email.send_keys("cmes1988@163.com")   

password =browser.find_element_by_id('login-password') #by id  
password.send_keys("film007love")   





element = driver.find_element_by_xpath("//select[@name='name']") 
all_options = element.find_elements_by_tag_name("option") 
for option in all_options: 
    print("Value is: %s" % option.get_attribute("value")) 
    option.click() 

    act = ActionChains(driver) 
    act.key_down(browserKeys.CONTROL) 
    act.click("").perform() 
    act.key_up(browserKeys.CONTROL)     

elem.clear() 
elem.send_keys("pycon") 
elem.send_keys(Keys.RETURN) 
assert "No results found." not in driver.page_source 
driver.close() 






driver = webdriver.Chrome() 
driver.get("https://www.wish.com") 
print driver.title 
driver.execute_script("https://connect.facebook.net/en_US/sdk.js") 
print driver.current_window_handle 

# Switch to new window 
driver.switch_to_window(driver.window_handles[-1]) 
print " Twitter window should go to facebook " 
print "New window ", driver.title 
driver.get("http://facebook.com") 
print "New window ", driver.title 

# Switch to old window 
driver.switch_to_window(driver.window_handles[0]) 
print " Linkedin should go to gmail " 
print "Old window ", driver.title 
driver.get("http://gmail.com") 
print "Old window ", driver.title 

# Again new window 
driver.switch_to_window(driver.window_handles[1]) 
print " Facebook window should go to Google " 
print "New window ", driver.title 
driver.get("http://google.com") 
print "New window ", driver.title 

"""