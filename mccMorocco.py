#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:31:25 2021

@author: fatimazahraelmansouri
"""

import time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import urllib
from http.cookiejar import CookieJar
from html.parser import HTMLParser
from urllib.request import build_opener, HTTPCookieProcessor
import re
import googletrans
from googletrans import Translator
from google_trans_new import google_translator  
# translator = Translator()
URL='https://mcc.dgmarket.com/tenders/adminShowBuyer.do?buyerId=6972679'
r=requests.get(URL)
empty=[]
soup = BeautifulSoup(r.content,"lxml")
rows=soup.findAll("tr") 
list_rows = []
mcclist=[]
for row in rows:
    cells = row.find_all('a')
    # for c in cells:
    #     print(c.text.strip())
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)

df = pd.DataFrame(list_rows)
df = df.replace(r'\n','', regex=True) 
df = df.replace(r'\t','', regex=True) 
df1 = df.iloc[8:,:]
df1.head(10)

#Rename column
df2=df1.rename(columns = {0:'title', 
                       }, 
            inplace = True)
df1=df1.reset_index(drop=True)


entity=[]
for i in rows:
    children=i.findChildren('a') 
    for child in children:
        empty.append('http://mcc.dgmarket.com'+child['href'])
        ent="MCC"
        mcc= {  
                'Entity':ent,
               }
        mcclist.append(mcc)
        mcl=pd.DataFrame(mcclist)
        mcl=mcl.iloc[3:]
        mcl=mcl.iloc[0:20,:]
        mcl=mcl.reset_index(drop=True)

e=pd.DataFrame(empty)
e4 = e[e[0].str.contains('http://mcc.dgmarket.com/tender/')]
e4=e4.reset_index(drop=True)
e4 = e4.iloc[0:50,:]

finaldf1=pd.merge(df1,mcl,right_index=True, left_index=True)
finaldf2=pd.merge(finaldf1,e4,right_index=True, left_index=True)
finaldf3=finaldf2.columns=['title_or','Entity','URL']

a=finaldf2['title_or']


translator = google_translator()  

translations = {}
for element in a:
    # add translation to the dictionary
    translations[element] = translator.translate(element)
    data_items = translations.items()
    data_list = list(data_items)
    z = pd.DataFrame(data_list)
    z.columns=['title_or','title']
    type(z)
    zw=z.drop(columns=['title_or'])
finaldf2=finaldf2.drop(columns=['title_or'])
finaldf4=pd.merge(finaldf2,zw,right_index=True, left_index=True)



# e1 = e[~e[0].isin(["http://mcc.dgmarket.comjavascript:dispType('spn')"])]
# e2 = e1[~e1[0].isin(["http://mcc.dgmarket.comjavascript:dispType('ca')"])]
# e3 = e2[~e2[0].isin(["http://mcc.dgmarket.comjavascript:dispType('pp')"])]






# opener = build_opener(HTTPCookieProcessor())
# response = opener.open(url)
# raw_response = response.read().decode('utf8', errors='ignore')

# print (response.read())

# try:
#     req=urllib.request.Request(url)
#     cj = CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#     response = opener.open(req)
#     raw_response = response.read().decode('utf8', errors='ignore')
#     response.close()
# except urllib.request.HTTPError as inst:
#     output = format(inst)
#     print(output)

# req=urllib.request.Request(url=Target)


# df=pd.read_html(url)
# df=np.array(df)
# q=pd.DataFrame(np.concatenate(df))
# p1=pd.DataFrame(q)

# # xhtml=f.read().decode('utf-8')
# p=HTMLTableParser()
# p.feed(response)
# table_list=p.tables





