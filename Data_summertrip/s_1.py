from bs4 import BeautifulSoup
from selenium import webdriver
import time

query_txt = "봄여행"

path = "c:/Temp/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.naver.com/")
driver.maximize_window()


element = driver.find_element_by_id("query")
element.send_keys(query_txt)
element.send_keys("\n")
time.sleep(3)

driver.find_element_by_link_text("뉴스").click()
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

f_name = 'Data/네이버_봄여행.txt'
f = open(f_name, 'w', encoding='utf-8')

content_list = soup.select('ul[class="list_news"] > li')
for i in content_list:

    # title = i.find('a', 'api_txt_lines total_tit').get_text()
    # f.write(title+'\n')

    # contents_1 = i.find('div', 'api_txt_lines dsc_txt').get_text()
    # f.write(contents_1+'\n')


    # try:
    #     tag = i.find('div', 'total_tag_area').get_text()
    #     f.write(tag+'\n\n')

    # except:
    #     pass

    content = i.find('a', 'api_txt_lines dsc_txt_wrap').get_text()
    
    f.write(content+'\n\n')

f.close()
