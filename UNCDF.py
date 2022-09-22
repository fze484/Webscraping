#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:19:44 2021

@author: fatimazahraelmansouri
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import numpy as np

url="https://www.uncdf.org/calls-for-tenders"

r=requests.get(url)
soup = BeautifulSoup(r.content,"lxml")

driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
driver.get(url)
page = driver.page_source
time.sleep(5)

page_soup = soup(page,'html.parser')

# test=driver.find_elements_by_class_name('ungm-flex-row')
# for t in test:
#     title=t.text

# links=driver.find_elements_by_class_name('open-in-new-tab')

elems = driver.find_elements_by_xpath("//div/a[@href]")
emp=[]
dvlist=[]
for elem in elems:
    e=elem.get_attribute("href")
    #emp.append(e)
    dic= {  
        'URL':e,
     }
    
    dvlist.append(dic)
dvl=pd.DataFrame(dvlist)
dvl.reset_index(drop=True)
dvl.drop(dvl.tail(3).index,inplace=True)
dvl.drop(dvl.head(1).index,inplace=True)
dvl.reset_index(drop=True)
#This is a good way to extract everything
da=[]
tt=driver.find_elements_by_xpath('//h3')
for t in tt:
    title=t.text
    print(title)
    dica= {  
        'title':title,
      }
    da.append(dica)
ti=pd.DataFrame(da)
#drop empty rows
nan_value = float("NaN")
ti.replace("", nan_value, inplace=True)
ti.dropna(subset = ["title"], inplace=True)
print(ti)
ti.reset_index(drop=True)

jj=driver.find_elements_by_class_name('date')
ra=[]
for t in jj:
    date=t.text
    entity="UNCDF"
    print(date)
    di= {  
        'date':date,
        'entity':entity
      }
    ra.append(di)
de=pd.DataFrame(ra)

uncdf=pd.merge(ti,de,right_index=True,left_index=True)





