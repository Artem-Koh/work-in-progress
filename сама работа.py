from bs4 import BeautifulSoup
import urllib3

h = urllib3.PoolManager()
resp = h.request('GET', 'https://coronavirus-monitor.ru/coronavirus-v-moskve/')
a = resp.data.decode('utf-8')
soup = BeautifulSoup(a, 'lxml')
c = str(soup.select("strong:nth-of-type(3)")).strip('[<strong>увеличилось на ')
print(c.strip('</strong>]'))
