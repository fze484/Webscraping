#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:13:21 2021

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

url="http://solicitations.fhi360.org/ConsultantSolicitation.aspx"
r=requests.get(url)
soup = BeautifulSoup(r.content,"lxml")


rows=soup.findAll("p",class_="rteindent1") 
# for row in rows:
#     cells = row.findAll('b')
#     for cell in cells:
#         title=cell.find('span')
#         print(title)
        
list_rows = []
fhilist=[]
numrows=len(rows)
numrows=numrows/2
numrows=int(numrows)
ls=[]

for i in rows:
    children=i.findChildren('a') 
    for child in children:
        ls.append('http://mcc.dgmarket.com'+child['href'])
        lsd=pd.DataFrame(ls)
        
for row in rows:
    cells = row.find_all('span')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
    
for x in range (numrows):
    entity="fhi360"
    fhi= {  
            'Entity':entity,
           }
    fhilist.append(fhi)
    fhil=pd.DataFrame(fhilist)
    fhil=fhil.reset_index(drop=True)

df = pd.DataFrame(list_rows)
df = df.replace(r'\n','', regex=True) 
df = df.replace(r'\t','', regex=True) 
# df1 = df.iloc[2:]
df= df[~df[0].isin(["[]"])]
df=df.reset_index(drop=True)
s=df[0].str.split(',',expand=True)
s1=s.columns=['title','ID','date','year','submission','submission year']

#remove weird characters
s['submission year']=s['submission year'].str.replace(r'\W',"")
cols = ['date', 'year']
cols1 = ['submission', 'submission year']
#combining columns
s['date'] = s[cols].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
s['submission date'] = s[cols1].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
s3=s.drop(columns=['year', 'submission','submission year','combined'])

s4=pd.merge(s3,lsd,right_index=True, left_index=True)
s5=s4.columns=['title','ID','date','submission date','URL']

















