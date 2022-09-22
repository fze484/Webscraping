#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:12:51 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib
import re
from selenium import webdriver

URL= "https://www.dai.com/our-work/working-with-dai/current-procurements"
r=requests.get(URL)
soup = BeautifulSoup(r.content,"html.parser")
contain=soup.findAll("div",class_="node-inner")

dailist=[]
for string in soup.stripped_strings:
    f=repr(string)        
    dai= {'title':f,               
               }
    dailist.append(dai)
df=pd.DataFrame(dailist)
df1=df.iloc[34:,:]
df2=df1.iloc[0:6,:]
df3=df2.reset_index()

h=[]

for link in soup.find_all('a'):
    l=link.get('href')
    h.append(l)
#     entity="DAI"
#     dictio= {
           
#            'Entity':entity,
           
#            }          
#     f.append(dictio)
    
# ent=pd.DataFrame(f)
hs=pd.DataFrame(h)
# hss=pd.merge(hs,ent,left_index=True, right_index=True)
#Rename column
hs.rename(columns = {0:'URL', 
                       }, 
            inplace = True)

#drop empty rows
nan_value = float("NaN")
hs.replace("", nan_value, inplace=True)
hs.dropna(subset = ["URL"], inplace=True)
# Drop rows you don't need 
hs1=hs.iloc[31:,:]
hs2=hs1.iloc[0:6,:]
hs3=hs2.reset_index()

#Drop the column named index
hs3.drop(['index'], axis=1)
df3.drop(['index'], axis=1)

dai=pd.merge(df3,hs3,left_index=True, right_index=True)
dai.head(10)
dai1=dai.drop(['index_x'], axis=1)
dai2=dai1.drop(['index_y'], axis=1)

#adding entity column 
f=[]
for e in dai2["URL"]:
    entity="DAI"
    dictio= {
           
           'Entity':entity,
           
           }          
    f.append(dictio)
    
ent=pd.DataFrame(f)
dai3=pd.merge(dai2,ent,right_index=True, left_index=True)

    
# hs1=hs[hs['URL'].str.contains("http")]


#     ll=h.append[URL+]
#     print(ll)
#     hh= {'URL':ll,               
#                }
#     h.append(hh)


    
    
    

# URL= "https://www.dai.com/our-work/working-with-dai/current-procurements"
# driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
# driver.get(URL)
# page = driver.page_source

# elems = driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]")
# emp=[]
# dvlist=[]
# for elem in elems:
#     a=elem.find_elements_by_xpath("/html/body/div/div[2]/div[1]/ul")
#     emp.append(a)
#     print(emp)
#     for b in a:
#         c=b.find_elements_by_xpath("/html/body/div/div[2]/div[1]/ul/li[1]")
#         print(c.text)
#     e=elem.get_attribute("href")
#     #emp.append(e)
#     dic= {  
#         'URL':e,
#      }
    
#     dvlist.append(dic)
# dvl=pd.DataFrame(dvlist)    
    
