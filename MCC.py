#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:39:27 2021

@author: fatimazahraelmansouri
"""
import time
import googletrans
from googletrans import Translator
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

url='http://mcc.dgmarket.com'
req=urllib.request.Request(url, None, {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})
cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
response = opener.open(req)
response.read()

# translator = Translator()

URL='http://mcc.dgmarket.com/'
r=requests.get(URL)
empty=[]
soup = BeautifulSoup(r.content,"lxml")

rows=soup.findAll("tr") 

list_rows = []
mcclist=[]
other=[]
othe=[]
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
    
    dates = row.findChildren()
    for i, child in enumerate(dates):
        if i == 5:
            publish=child.text.strip()
            print(publish)
            oop= {  
                'date':publish,  
               }
            other.append(oop)   
        if i == 7:
            deadline=child.text.strip('\n')
            
            print(deadline)
            opp= {  
                
                'submission ':deadline
               }
            othe.append(opp)   
ddt=pd.DataFrame(other)
dtt=pd.DataFrame(othe)
dtt.head()
dtt.columns=['submission']
dtt.submission=dtt.submission.str.replace("\t"," ")
dtt.submission=dtt.submission.str.replace("\n"," ")
dtt.submission=dtt.submission.str.strip()
ddd =pd.merge(ddt,dtt,right_index=True, left_index=True)    
dd1= ddd.iloc[2:]
dd1=dd1.reset_index(drop=True)

df = pd.DataFrame(list_rows)
df = df.replace(r'\n','', regex=True) 
df = df.replace(r'\t','', regex=True) 
df1 = df.iloc[2:]
df1.head(10)
df1=df1.reset_index(drop=True)
df1.columns=['title']

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
e4 = e4.iloc[0:20,:]

#title+entity
finaldf1=pd.merge(df1,mcl,right_index=True, left_index=True)
#title entity links
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
    zw.reset_index(drop=True)
finaldf2=finaldf2.drop(columns=['title_or'])
finaldf2.reset_index(drop=True)
mc=pd.merge(finaldf2,zw,right_index=True, left_index=True)

mc.title=mc.title.str.replace("[","")
mc.title=mc.title.str.replace("]","")
mcc=pd.merge(mc,dd1,right_index=True, left_index=True)

    

    
   
    
   
    