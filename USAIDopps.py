#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:18:25 2021

@author: fatimazahraelmansouri
"""

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

URL='https://www.usaid.gov/work-usaid/partnership-opportunities/search-for-opportunities'
r=requests.get(URL)
soup = BeautifulSoup(r.content,"lxml")
rf=[]
fordic=[]

alls=soup.findAll("div",class_="view-content")

for a in alls:
    titles=a.findAll('h3',class_="field-content")
    for t in titles:
        pt=t.find("a")
        children=t.findChildren('a') 
        for child in children:
            rf.append(child['href'])
            lsd=pd.DataFrame(rf)
            lsd.drop_duplicates()
            ussr=lsd.columns=['URL']
            dic= {      
            'title':pt 
            }
            fordic.append(dic)
    tt=pd.DataFrame(fordic)
    tt.reset_index()
    
    tp=[]
    types=a.findAll('div',class_="views-field views-field-field-opportunity-type")
    for ty in types:
        typ=ty.find("div",class_="field-content").text.strip()
        dicti= {      
            'type':typ
         }
        tp.append(dicti)
    tpe=pd.DataFrame(tp)
    tpe.reset_index()
    ct=[]    
    country=a.findAll('div',class_="views-field views-field-field-country-mission")
    for c in country:
        count=c.find("div",class_="field-content").text.strip()
        dictio= {      
            'country':count
         }
        tp.append(dictio)
    cty=pd.DataFrame(tp)
    cty.reset_index()
        
        
    sb=[] 
    submission=a.findAll('span',class_="date-display-single")
    for s in submission:
        sub=s.text
        diction= {    
            'submission':sub
         }
        sb.append(diction)
    sbn=pd.DataFrame(sb)
    sbn.reset_index()
    
    #Field of the tender, not in all opps
    # sector=soup.findAll("div",class_="views-field views-field-field-sectors")
    # for s in sector:
    #     se=s.find("div",class_="field-content").text
    #     print(se)
    
    usaidopp=pd.merge(tt,tpe,right_index=True,left_index=True)
    usaidopp1=pd.merge(usaidopp,cty,right_index=True,left_index=True)
    usaidopp2=pd.merge(usaidopp1,sbn,right_index=True,left_index=True)
    usaidopp3=pd.merge(usaidopp1,lsd,right_index=True,left_index=True)
    
    print(usaidopp3)



















