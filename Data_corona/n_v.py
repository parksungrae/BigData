from konlpy.tag import *
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud
from collections import Counter
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

okt = Okt()

data1 = open('Data/코로나_n.txt', encoding='UTF8').read()
print()

data2 = okt.nouns(data1)
print('1. 추출된 키워드:', data2)

data3 = []
for a in data2:
    if a == '제목':
        data3.append(a.replace('제목', '박성래'))
    elif a == '내용':
        data3.append(a.replace('내용', ''))
    elif a == '번호':
        data3.append(a.replace('번호', ''))
    else:
        data3.append(a)

data4 = Counter(data3)
data5 = data4.most_common(100)
print('상위 100개 단어')
print('2. 단어별 빈도수:', data5)
print()

sword = open('Data/코로나불용어.txt', encoding='UTF8').read()
print(sword)

data6 = [ each_word for each_word in data3 if each_word not in sword ]

data7 = []
for i in data6:
    if len(i) > 2 and len(i) <= 5:
        data7.append(i)

data8 = Counter(data7)
print(data8)
data9 = data8.most_common(50)
print(data9)

word = dict(data9)

# wordcloud = WordCloud(font_path='c:\\windows\\fonts\\H2HDRM.TTF',
#                       relative_scaling=0.4,
#                       background_color='white',
#                       ).generate_from_frequencies(word)
# plt.figure(figsize=(10, 8))
# plt.imshow(wordcloud)
# plt.title('cym')
#
# plt.axis('off')
# plt.show()

korea = np.array(Image.open('Data/korea.jpg'))
save_image = ('Data/corona_korea.png')

wc = WordCloud(font_path='c:\\windows\\fonts\\a블랙B.ttf',
            relative_scaling=0.4,
            mask=korea,
            background_color='white',
            ).generate_from_frequencies(word)

plt.figure(figsize=(10, 10))
plt.imshow(wc)

plt.axis('off')
plt.savefig(save_image)
plt.show()