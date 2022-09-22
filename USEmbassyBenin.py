#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 21:20:40 2021

@author: fatimazahraelmansouri
"""

from bs4 import BeautifulSoup 
import pandas as pd
import requests

URL = 'https://bj.usembassy.gov/embassy/u-s-embassy-cotonou-bid-solicitations/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')

aa=soup.findAll('a')
bnlist=[]
for l in aa:
    title=l.text
    entity="US Embassy of Benin"
    ebn= {'title':title,
           
           'Entity':entity,
                      
           }          
    bnlist.append(ebn)
  
df1=pd.DataFrame(bnlist)
df1.drop(df1.head(89).index,inplace=True)
df1.drop(df1.tail(19).index,inplace=True)
df2=df1.reset_index(drop=True)
li=soup.findAll('li')
lll=[] 
for l in li:
    emb=l.findAll('a',href=True)
    for link in emb:
        lll.append(link['href'])
df=pd.DataFrame(lll)
df.drop(df.tail(12).index,inplace=True)
df.drop(df.head(229).index,inplace=True)
dff=df.reset_index(drop=True)
dff.columns=['URL']
dff.drop(dff.tail(1).index,inplace=True)  
dffp=dff.drop_duplicates()
dffpr=dffp.reset_index(drop=True)

usebenin=pd.merge(df2,dffpr,right_index=True,left_index=True)    
    
    