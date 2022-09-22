#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 04:52:17 2021

@author: fatimazahraelmansouri
"""

from bs4 import BeautifulSoup 
import pandas as pd
import requests

URL = 'https://sn.usembassy.gov/embassy/dakar/business-opportunities/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')

snlist=[]
t=[]
panels=soup.findAll("div",class_="panel-group")
for p in panels:
    zz=p.findChildren("h4",class_="panel-title")
    for z in zz:
        title=z.text
        entity="US Embassy of Senegal"
        ti={'title':title  }
        esn= {
           
           'Entity':entity,
           'URL':URL
                      
           }          
        snlist.append(esn)
        t.append(ti)
  
df1=pd.DataFrame(snlist)
tie=pd.DataFrame(t)

tie[['title','date']] = tie.title.str.split("Closing date:",expand=True)
tie['title']=tie['title'].str.replace("(","")
tie['date']=tie['date'].str.replace(")","")

usems=pd.merge(tie, df1,right_index=True, left_index=True)


    