#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:44:23 2021

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
# translator = Translator()

URL='https://researchfunding.duke.edu/search-results'
#extracting table, creating DF
df=pd.read_html(URL) #use parse_dates=True to change format of dates
df=np.array(df)
n1=np.reshape(df,(20,7))
us=pd.DataFrame(n1)
us1=us.columns=['submission','title',"Entity",'Discipline',"Who's Eligible",'Award amount','date']

#removing "deadline: " text
uss=us.submission.str.split(": ",expand=True)
ussr=uss.columns=['dead','submission']
ussp=uss.drop(columns=['dead'])
#drop submission column
us2=us.drop(columns=['submission'])
#Add new submission column
usg=pd.merge(us2,ussp,right_index=True, left_index=True)

#Adding URLs
driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
driver.get(URL)

r=requests.get(URL)
soup = BeautifulSoup(r.content,"lxml")
page = driver.page_source
page_soup = soup(page,'html.parser')

elems = driver.find_elements_by_xpath("//td/a[@href]")
usglist=[]
for elem in elems:
    e=elem.get_attribute("href")
    #emp.append(e)
    dic= {  
        'URL':e,
     }
    
    usglist.append(dic)
usgl=pd.DataFrame(usglist)

usgrant=pd.merge(usg,usgl,right_index=True,left_index=True)





