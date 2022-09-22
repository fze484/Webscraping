#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:21:13 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
import numpy as np

URL="https://invest-procurement.com/forecast"
#extracting table, creating DF

#extracting table, creating DF
df=pd.read_html(URL) #use parse_dates=True to change format of dates
df=np.array(df)
n=np.reshape(df,(2,5))
usaidin=pd.DataFrame(n)

cols=usaidin.columns=['title','description','Country',"date",'Award amount']

rx=[]
#find number of table rows and loop through length of rows to add entity 
index=usaidin.index
len(index)

for row in range (len(index)):
    ent="USAID Invest"
    d= {  
        'Entity':ent,
     }
    rx.append(d)
ent=pd.DataFrame(rx)

usaidinvest=pd.merge(usaidin,ent,right_index=True, left_index=True)




    