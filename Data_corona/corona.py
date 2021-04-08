from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

query_txt = '코로나'

f_name = 'Data/코로나_n.txt'
fc_name = 'Data/코로나_n.csv'

path = 'c://Temp/chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://naver.com')
driver.maximize_window()
time.sleep(1)

element = driver.find_element_by_id('query')
element.send_keys(query_txt)
element.submit()

driver.find_element_by_link_text('VIEW').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

view_list = soup.find('ul', 'lst_total _list_base').find_all('li')

no2 = []
title2 = []
contents2 = []

no = 1

for i in view_list:
    f = open(f_name, 'a', encoding='UTF8')

    print(no)
    no2.append(no)
    f.write('1. 번호:' + str(no) + '\n')

    title = i.find('a', 'api_txt_lines total_tit').get_text()
    title2.append(title)
    f.write('2. 제목:' + str(title) + '\n')
    print(title)

    contents = i.find('div', 'api_txt_lines dsc_txt').get_text()
    contents2.append(contents)
    f.write('3. 내용:' + str(contents) + '\n')
    print(contents)

    f.write('=' * 80 + '\n')
    f.close()

    print()
    no += 1


print("txt 파일 저장 경로: %s" % f_name)


naver_blog = pd.DataFrame()

naver_blog['번호'] = no2
naver_blog['제목'] = title2
naver_blog['내용'] = contents2

naver_blog.to_csv(fc_name, encoding="utf-8-sig", index=False)
print(" csv 파일 저장 경로: %s" % fc_name)

df = pd.read_csv("Data/코로나_n.csv", index_col= 0)
print(df)
print(df['제목'])
print(df['내용'])

