#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:11:00 2021

@author: fatimazahraelmansouri
"""
from bs4 import BeautifulSoup 
import pandas as pd
import requests

URL = 'https://ma.usembassy.gov/embassy-consulate/rabat/procurement-opportunities/?_ga=1.197172072.691969622.1485885392'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')
molist=[]
t=[]
pan=soup.findAll('div',class_='panel-group')
for p in pan:
    zz=p.findChildren("h4",class_="panel-title")
    for z in zz:
        title=z.text
        entity="US Embassy of Morocco"
        esn= {'title':title,  
           'Entity':entity,
           'URL':URL
           }          
        molist.append(esn)      
usemo=pd.DataFrame(molist)

