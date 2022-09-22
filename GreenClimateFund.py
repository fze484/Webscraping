#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:54:36 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup 
import requests


URL="https://www.greenclimate.fund/about/procurement"
r=requests.get(URL)
soup=BeautifulSoup(r.content,'lxml')

o=[]
p=[]
#title and URL
zp=soup.findAll("td",class_="views-field views-field-title")
for i in zp:
    children=i.findChildren("a")
    for child in children:
        title=child.text.strip()
        ent="Green Climate Fund"
        print(title)
        o.append(URL+child['href'])
    gc= {'title':title,
           
           'Entity':ent,
           'URL':o               
           }          
    p.append(gc)
df1=pd.DataFrame(p)
        

#type
q=[]        
wo=soup.findAll("td",class_="views-field views-field-field-subtype" )       
for w in wo:
    typ=w.text.strip()
    print(typ)
    dc={'type':typ,            
           }          
    q.append(dc)
df2=pd.DataFrame(q)



#dates
r=soup.findAll("span",class_="date-display-single")    
g=[]
for y in r:
    d=y.text.strip()
    dictio={
           'date':d,
        
           } 
    g.append(dictio)
df=pd.DataFrame(g)
#get even rows as date posted and even rows as submission deadline
dates=df.iloc[::2]
da1=dates.reset_index()
da1=da1.iloc[:,1:]

submission = df.iloc[1::2]
sb1=submission.reset_index()
sb1=sb1.iloc[:,1:]


gf=pd.merge(da1,sb1,left_index=True, right_index=True)
gff=pd.merge(df1,df2,left_index=True, right_index=True)
greencf=pd.merge(gff,gf,left_index=True, right_index=True)     
greencf.columns= ["title","Entity","URL","type","date","submission"]
    
    
    
    
    
    
    