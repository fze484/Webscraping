#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:42:28 2021

@author: fatimazahraelmansouri
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests

url="http://www.usaedc.org/about/employment-opportunities/"
r=requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
als=soup.findAll("p")
ls=[]
ls1=[]
ls2=[]
for a in als: 
    title=a.text.strip()
    children=a.find_all('a',href=True)
    for link in children:
        ls.append(url+link['href'])           
        posted=link.find_next("p").text
        entity="USDA Opps"
        dic2= {'title':title,
               'Entity':entity,
               'date':posted
           }                
        ls2.append(dic2)

df2=pd.DataFrame(ls2)
df3=pd.DataFrame(ls)
df3.columns=["URL"]
usdaopps=pd.merge(df2,df3,right_index=True,left_index=True)


        
    
    