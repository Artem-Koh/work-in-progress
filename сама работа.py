import urllib3

h = urllib3.PoolManager()
u = 'https://coronavirus-monitor.ru/coronavirus-v-moskve/'
resp = h.request('GET', u)
a = str(resp.data.decode('utf-8'))
a = a[10200:len(a)//25 - 295]
c = 0
x = ''
while a[c] + a[c + 1] != 'на':
    c += 1
c += 3
while a[c] != '<':
    x += a[c]
    c += 1
print(x)
