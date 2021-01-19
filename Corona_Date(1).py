#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[ ]:


from bs4 import BeautifulSoup
import urllib3
import os
#import datetime


# In[5]:


h = urllib3.PoolManager()
resp = h.request('GET', 'https://gogov.ru/covid-19/msk')
a = resp.data.decode('utf-8')
soup = BeautifulSoup(a, 'lxml')
date = []
quantity = []
new_cases = []
j = 0
y = 0
for tag in soup.find_all("tr"):
        x = str("{0}: {1}".format(tag.name, tag.text).strip('tr: '))
        date += [x[:8]]
        x = x[8:]
        if x != 'лучаев зараженияУмерлоВыздоровело' and len(x) > 32:
                while x[j] != '(':
                        j += 1
                quantity += [x[:j]]
        x = x[j:]
        if x != 'лучаев зараженияУмерлоВыздоровело' and len(x) > 25:
                while x[y] != ')':
                        y += 1
                new_cases += [x[1:y]]
        
        y = 0
        j = 0
date = date[1:12]
quantity = quantity[:11]
new_cases = new_cases[:11]


# In[8]:


table = pd.DataFrame([quantity, new_cases], 
columns = [date])

table


# In[ ]:




