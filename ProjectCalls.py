#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:56:36 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re
import time
import dateparser
driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')

URL='https://projectcalls.com/project-listings/'
driver.get(URL)
page = driver.page_source
time.sleep(10)
driver.execute_script("window.scrollTo(0, 100)")

#load more listings
driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/a').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/a').click()
time.sleep(5)

#Title 
t=[]
bloc=driver.find_elements_by_xpath('//h5')   
for b in bloc:
    ti=b.text
    dicatio= {  
        'title':ti,   
      }
    t.append(dicatio)
title=pd.DataFrame(t)

#Entity
org=[]
bloc=driver.find_elements_by_xpath('//div/strong')   
for b in bloc:
    sect=b.text
    dicat= {  
        'organisation':sect,
       
      }
    org.append(dicat)
organisation=pd.DataFrame(org)
    
    
#Country 
ct=[]
bloc=driver.find_elements_by_xpath('//a/div/div[3]')    
for b in bloc:
    country=b.text
    entity='Project Calls'
    dica= {  
        'country':country,
        'Entity':entity
      }
    ct.append(dica)
country=pd.DataFrame(ct)
  

#Date posted   
da=[]
bloc=driver.find_elements_by_xpath('//li/strong')    
for b in bloc:
    posted=b.text
    
    dica= {  
        'date':posted,
      }
    da.append(dica)
da=pd.DataFrame(da)
da['date'] = da['date'].str.replace(r'Posted ', '')

###### Date formatting: 'x months/days/hours' ago into 'DD MM, YYYY' format
dd=[]
for row in da.iterrows():
    forma = row[1]['date']  
    date=dateparser.parse(forma).strftime("%d %B, %Y")
    dic= {  
        'date':date,
      }
    dd.append(dic)
dates=pd.DataFrame(dd)
dates=dates.reset_index(drop=True)
        

##########################################################
##########################################################
###### Date formatting: 'x months/days/hours' ago into 'DD MM, YYYY' format
# import dateparser
# date_ago="4 hours ago" 
# date=dateparser.parse(date_ago).strftime("%d %B, %Y")
# date
##########################################################
##########################################################


#URLs 
els=[]
elems = driver.find_elements_by_xpath("//ul/li/a[@href]")
for elem in elems:
    els.append(elem.get_attribute("href"))
links=pd.DataFrame(els)    
links.drop(links.head(18).index, inplace=True)   
links=links.reset_index(drop=True) 
links.columns= ['URL']

# Putting it all together
df=pd.merge(title,organisation,right_index=True,left_index=True)
df2=pd.merge(df,dates,right_index=True,left_index=True)
df3=pd.merge(df2,country,right_index=True,left_index=True)
df4=pd.merge(df3,dates,right_index=True,left_index=True)
projectcalls=pd.merge(df4,links,right_index=True,left_index=True)
projectcalls=projectcalls.drop(['date_x'], axis=1)

projectcalls.columns=['title','organisation','country','Entity','date','URL']












  
    