from bs4 import BeautifulSoup
import urllib3
import os
import datetime

h = urllib3.PoolManager()
resp = h.request('GET', 'https://coronavirus-monitor.ru/coronavirus-v-moskve/')
a = resp.data.decode('utf-8')
soup = BeautifulSoup(a, 'lxml')
c = str(soup.select("strong:nth-of-type(3)")).strip('[<strong>увеличилось на ')
c = c.strip('</strong>]')
x = os.path.join('C:\\','Users','bbrit','Desktop','data.csv')
if c == 'зменилось':
    print('Сайт не обновил данные')
    
else:
    with open (x, 'a') as f:
        f.write(c + ', ' + datetime.datetime.today().strftime("%Y-%m-%d") + '\n')
        print('Дело сделано')
