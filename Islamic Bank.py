#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:00:50 2021

@author: fatimazahraelmansouri
"""
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import googletrans
from googletrans import Translator
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

URL='https://www.isdb.org/project-procurement/tenders'

r=requests.get(URL)
soup = BeautifulSoup(r.content,"lxml")

driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
driver.get(URL)
page = driver.page_source
time.sleep(5)

gi=soup.findAll('div',class_="views-row")

l=[]
isb=[]
for g in gi:
    #titles
    title=g.find("div",class_="field-title")    
    title=title.text
    #country
    co=g.find("div",class_="field field--name-field-world-country field--type-entity-reference field--label-hidden field--item")
    country=co.text.strip()
    #submission dates
    su=g.find('div',class_='field field--name-field-close-date field--type-datetime field--label-hidden field--item')
    submission=su.text.strip()
    #links
    children=g.findChildren('a') 
    for child in children:
        l.append(URL+child['href'])
    dic= {  
        
        'submission':submission,
        'title':title,
        'country':country,
        'URL':l,
     }
    
    isb.append(dic)
isbdf=pd.DataFrame(isb)



