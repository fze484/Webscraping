#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:50:07 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib
import re

URL= "https://www.chemonics.com/our-procurements/"
r=requests.get(URL)
soup = BeautifulSoup(r.content,"lxml")
contain=soup.findAll("div",class_="news-facet-columns")
li=[]
one=[]
for c in contain:
    idd=c.find("h3").text
    print(idd)
    sub=c.find("span",class_="date").text.strip()
    print(sub)
    ex=c.find("div",class_='excerpt').text.strip()
    print(ex)
    children=c.findChildren('a')
    for child in children:
        li.append(child['href'])
        lis=pd.DataFrame(li)
    
        dii= {      
            'id':idd,
            'submission':sub,
            'description':ex,
            'URL':li
            }
        one.append(dii)
        chem=pd.DataFrame(one)
        chem['submission'] = chem['submission'].str.replace(r'Expiration Date: ', '')
        
