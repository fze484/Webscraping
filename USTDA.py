#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:46:41 2021

@author: fatimazahraelmansouri
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re
import time


URL='https://ustda.gov/work/contracts-with-ustda/'
re=requests.get(URL)
soup=BeautifulSoup(re.content,'lxml')

links=[] 
io=[]
opps=soup.findAll('div',class_='wp-block-file')
for opp in opps:
    title=opp.find("a").text
    print(title)
    ent='USTDA'
    print(ent)
    dic={'title':title,
          'Entity':ent,              
           }  
    io.append(dic)
df=pd.DataFrame(io)
 

    
opps=soup.findAll('div',class_='wp-block-file')    
for opp in opps:    
    prd=opp.find_all('a',href=True)
    for link in prd:
        links.append(link['href'])    
dfl=pd.DataFrame(links)
dfl.columns=['URL']
ustda=pd.merge(df,dfl,right_index=True,left_index=True)
ustda.drop(ustda.tail(1).index, inplace=True)  






