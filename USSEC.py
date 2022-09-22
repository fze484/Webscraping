#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:15:13 2021

@author: fatimazahraelmansouri
"""

from bs4 import BeautifulSoup 
import pandas as pd
import requests

URL = 'https://www.unitedsoybean.org/request-for-proposals/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')

alm=soup.findAll("p")
ll=[]
for a in alm:
    texts=a.text
    print(texts)
    lls= {'text':texts,
         
           }          
    ll.append(lls)

df1=pd.DataFrame(ll)

#drop empty rows
nan_value = float("NaN")
df1.replace("", nan_value, inplace=True)
df1.replace(" ", nan_value, inplace=True)
df1.dropna(subset = ["text"], inplace=True)
print(df1)
dff=df1.reset_index(drop=True)
df2 = dff[~dff['text'].isin(['Click to view.'])]
df3=df2.reset_index()
df4=df3.iloc[:,1:]
df5=df4.T
df11=df5.reset_index(drop=True)
df11.columns=['title',"URL","Description","submission"]

ss=[]
u=len(df5.index)
      
for i in range (u):
    ent="USSEC"
    sss= {'Entity':ent,
         
           }          
    ss.append(sss)
ab=pd.DataFrame(ss)
ab.reset_index(drop=True)
ussec=pd.merge(df11,ab,right_index=True, left_index=True)

    
    
    
    
    
    
    
    
    
    
    