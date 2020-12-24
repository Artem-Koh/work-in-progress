from bs4 import BeautifulSoup
import urllib3
import os
import datetime

connection = urllib3.PoolManager()
resp = connection.request('GET', 'https://coronavirus-control.ru/coronavirus-moscow/')
a = resp.data.decode('utf-8')
soup = BeautifulSoup(a, 'lxml')
quantity = str(soup.article.b.span).strip('<span><span class="plus">+').strip('</span></span>')
new_cases = str(soup.article.b).strip('<b>')
new_cases = new_cases[:12].replace(' ', '')
date = str(soup.article.div.select('div:nth-of-type(2)'))
for i in range(len(date) - 300):
        if date[i:i + 10] == 'На сегодня':
                date = date[i + 14:i + 24]
                break
time = datetime.datetime.today().strftime("%d.%m.%Y - %H:%M")

the_way = os.path.join('C:\\','Users','bbrit','Desktop','data_corona.csv')
with open (the_way, 'a') as file:
        file.write(quantity + ', ' + new_cases + ', ' + date + ', ' + time + '\n')
        print('Дело сделано')


