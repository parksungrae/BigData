import os

print(os.getcwd())

from bs4 import BeautifulSoup


# filename = "C:/Users/user/PycharmProjects/gsm/Data/ex.html"

#
# f = open(filename, 'r', encoding='utf-8')
#
# for line in f:
#     print(line)
#
#
# f.close()

# with open(filename, 'r', encoding='utf-8') as ex :
#     soup = BeautifulSoup(ex, 'html.parser')
#
#
# print(soup.find('title'))
# print(soup.find('p'))
# print(soup.find('img'))
#
# print(soup.find_all('p'))
#
# print(soup.find('p',align = "center"))
# print(soup.find(align = "center"))


# list_1 = soup.find_all('p')
#
# for i in list_1 :
#     print(i.string)
#     print(i.get_text())


# f = open('C:/Users/user/PycharmProjects/gsm/Data/ex.html', 'w', encoding='utf-8')
#
# list_1 = soup.find_all('p')
#
# for i in list_1 :
#     txt = i.get_text()
#     f.write(txt+'\n')
#
# f.close()

# filename = "../Data/bs.html"
#
# with open(filename, 'r', encoding='utf-8') as ex :
#     soup2 = BeautifulSoup(ex, 'html.parser')
#
#
# print(soup2.find_all('p'))
# print()
#
# print(soup2.find_all('span'))
# print(soup2.select('span'))
# print(soup2.select('div > p > span')) # div 밑 p 밑 span 가져오기
# print()
#
# #class name1의 데이터만 가져오고 싶을 때
# print(soup2.select('.name1'))
# print()
#
# print(soup2.select('p[class="name1"]'))
#
#
# y1 = soup2.find('p', 'name1').find_all('span')
# y2 = soup2.select('.name1 > span')
# print(y1)
# print(y2)
#
# print()
#
# y3 = soup2.select('.name1 > span.store')
# y3_2 = soup2.select('.name1 > .store')
#
# print(y3)
# print(y3_2)
#
# y4 = soup2.select('span.store')
# y5 = tag_span_store2 = soup2.select('.store')
# print(y4)
# print(y5)

# f = open('../Data/span.txt', 'w', encoding='utf-8')
#
# list_1 = soup2.find_all('span')
#
# for i in list_1 :
#     txt = i.get_text()
#     f.write(txt+'\n')
#
# f.close()
# print()
#
# print(soup2.select('.name1'))
# print(soup2.select('#fruits1'))
# print()
#
#
# print(soup2.select('.name1 > span.store'))
# print(soup2.select('p.name1 > span.store'))
# print(soup2.select('#fruits1 > span.store'))
#
# data = soup2.select('a')
#
# print(data)
#
# for c in data :
#     g = c['href']
#     print(g)
#     print(c.get_text())
#
#
# print()
filename = "../Data/bs_example.html"

with open(filename) as ex:
    soup = BeautifulSoup(ex, 'html.parser')

# img_src = soup.find('div', 'flex_grid credits search_results').find_all('img')
# img_src2 = soup.select('div[class="flex_grid credits search_results"] > div.item > a > img')
#
# print(img_src)
# print(img_src2)

f = open('../Data/img.txt', 'w', encoding='utf-8')

img_src = soup.find('div', 'flex_grid credits search_results').find_all('img')
#
# print(len(img_src))
#
# for c in img_src:
#     img = c['src']
#     f.write(img + '\n')

img_src_2017 = []
img_src_2018 = []

for c in img_src:
    img_src1 = c['src']

    if '2017' in img_src1:
        img_src_2017.append(img_src1)
    elif '2018' in img_src1:
        img_src_2018.append(img_src1)

print(img_src_2017)
print(img_src_2018)
f.close()
