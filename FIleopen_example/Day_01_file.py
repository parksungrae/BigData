filename = 'Data/poem2.txt'

f = open(filename, 'r', encoding='utf-8')
lines = f.readlines()
for i in lines :
    print(i.strip())
f.close()