#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:03:16 2021
UNGM
@author: fatimazahraelmansouri
"""
import time
import googletrans
from googletrans import Translator
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import urllib
from html.parser import HTMLParser
from urllib.request import build_opener, HTTPCookieProcessor
import re
import googletrans
from googletrans import Translator
from selenium import webdriver

url="https://www.ungm.org/Public/Notice"
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
#drop all except the ones that contain : https://www.ungm.org/Public/Notice/
dvl1=dvl[dvl.URL.str.contains('https://www.ungm.org/Public/Notice/')]
dvl1=dvl1.reset_index(drop=True)

#This is a good way to extract everything
tt=driver.find_elements_by_class_name('tableCell')
da=[]
for t in tt:
    date=t.text
    dica= {  
        'date':date,
      }
    da.append(dica)
da=pd.DataFrame(da)

# splitting table into  2, 4, 6, etc. columns
d1=pd.DataFrame(np.hstack(np.split(da, 2)))
d2=pd.DataFrame(np.hstack(np.split(d1, 2)))
d3=pd.DataFrame(np.hstack(np.split(d2, 2)))
d4=pd.DataFrame(np.hstack(np.split(d3, 2)))
d5=d4.iloc[1:]
d6=d5.T
d7=d6.iloc[1:]

#rename cols 
d8=d7.columns=['title','submission','date','Entity','Type','ID','Country']

#Add links to the table
devbus=pd.merge(d7,dvl1,right_index=True, left_index=True)











