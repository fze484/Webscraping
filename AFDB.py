#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:18:21 2021

@author: fatimazahraelmansouri
"""

from urllib.request import urlretrieve 
from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import urllib.request
import pandas as pd
import io
import requests

##################   AFDB #################################

q=("http://www.afdb.org/en/projects-and-operations/procurement")
url=urllib.request.urlopen("http://www.afdb.org/en/projects-and-operations/procurement")
s = url.read()

productlinks=[]
afdblist=[]
for x in range (0,25):
    r=requests.get(f'https://www.afdb.org/en/projects-and-operations/procurement?page={x}')
    soup = BeautifulSoup(r.content,"lxml")
    productlist=soup.findAll('td',class_="views-field views-field-title")
    
    for item in productlist:
        for link in item.find_all('a',href=True):
            productlinks.append(q+link['href'])
   
    # title=soup.findAll('td',class_="views-field views-field-title")
    entity="AfDB"
    title = soup.find('td',class_="views-field views-field-title").text.strip()
    dates=soup.find('td',class_="views-field views-field-field-publication-date").text.strip()
    afdb= {'title':title,
               'date':dates,
               'Entity':entity,
               'URL':productlinks               
               }
    afdblist.append(afdb)
    print("Saving:",afdb['title'])
df=pd.DataFrame(afdblist)
print(df.head(15))   
             





