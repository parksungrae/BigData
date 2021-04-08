from bs4 import  BeautifulSoup
from selenium import webdriver
import time

query_txt = "인공지능"
f_name = 'Data/인공지능1.txt'

path = "c:/Temp/chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://naver.com")
driver.maximize_window()
time.sleep(1)

element = driver.find_element_by_id("query")
element.send_keys(query_txt)
element.send_keys("\n")
time.sleep(1)

driver.find_element_by_link_text('뉴스').click()

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

f = open(f_name, 'w', encoding='utf-8')

news_list = soup.select('ul[class="list_news"] > li')

for i in news_list:
    try:
        title = i.find('a', 'news_tit').get_text()
        f.write(title)
        f.write('\n')
    except:
        pass

    try:
        contents = i.find('div', 'news_dsc').get_text()
        print(contents)
        print('\n')
    except:
        pass



