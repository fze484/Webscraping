#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:41:20 2021

@author: fatimazahraelmansouri
"""
from bs4 import BeautifulSoup 
import pandas as pd
import requests

URL = ' http://www.tanmia.ma/en/category/appels-offres/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')

pp=[]  
tanlist=[]
thtlist=[]
art=soup.findAll("article")
for a in art:
    ti=a.find("h2")
    title=ti.text
    #date=ti.find("p",class_"post-meta")
    tht= {'title':title,        
           }          
    thtlist.append(tht)

fat=soup.findAll("div",class_="entry")
mrd=soup.find_all('a',href=True)
for link in fat:
    children=link.findChildren('a')
    for child in children:
        pp.append(child['href'])
        
        entity="Tanmia"
        tan= {
               'Entity':entity,
               'URL':pp               
               }          
    tanlist.append(tan)
df=pd.DataFrame(thtlist)
df1=pd.DataFrame(tanlist)
tanmia=pd.merge(df1,df,right_index=True,left_index=True)

blist=[]        
tes=soup.findAll("p",class_="post-meta")  
for t in tes:
    date=t.find("span",class_="tie-date").text
    bl= {
               'date':date               
               }          
    blist.append(bl)
dsf=pd.DataFrame(blist)
tanmia=pd.merge(tanmia,dsf,right_index=True,left_index=True)
    



  
