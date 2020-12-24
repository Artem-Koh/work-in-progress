from bs4 import BeautifulSoup
import urllib3
import os
import datetime

h = urllib3.PoolManager()
resp = h.request('GET', 'https://coronavirus-control.ru/coronavirus-moscow/')
a = resp.data.decode('utf-8')
soup = BeautifulSoup(a, 'lxml')
c = str(soup.article.b.span).strip('<span><span class="plus">+').strip('</span></span>')
print(c)
k = str(soup.article.b).strip('<b>')
k = k[:12].replace(' ', '')
print(k)
o = str(soup.article.div.select('div:nth-of-type(2)'))
for i in range(len(o) - 300):
        if o[i:i + 10] == 'На сегодня':
                d = o[i + 14:i + 24]
                break
print(d)
t = datetime.datetime.today().strftime("%d.%m.%Y - %H:%M")
print(t)
x = os.path.join('C:\\','Users','bbrit','Desktop','data_corona.csv')
with open (x, 'a') as f:
        f.write(c + ', ' + k + ', ' + o + ', ' + t + '\n')
        print('Дело сделано')


