#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:02:04 2021

@author: fatimazahraelmansouri
"""

from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests

URL= "https://www.giz.de/en/worldwide/340.html"
r=requests.get(URL)
soup = BeautifulSoup(r.content,"html.parser")

# cont=soup.findAll("section",class_="accordion col-xl-12 row")

# for c in cont:
#     tipe= c.find("h3",class_="col-xs-12").text
#     print(tipe)
ls=[]
ls2=[]
lss=[]
dvs=soup.findAll("div",class_="accordion-content col-xs-12")
for d in dvs:    
    
    # dic= {'title':title,               
    #    }                
    # lss.append(dic)
    children=d.find_all('a',href=True)
    for link in children:
        title=link.text
        ls.append(URL+link['href'])           
        entity="GIZ(2)"
        dic2= {
               'Entity':entity,
               'title':title,
               
           }                
        ls2.append(dic2)


df2=pd.DataFrame(ls2)
df=pd.DataFrame(ls)
df.columns=['URL']

gi=pd.merge(df,df2,right_index=True,left_index=True)
giz2=gi.iloc[2:,]
giz2.drop(giz2.tail(1).index, inplace=True)




