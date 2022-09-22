#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:32:21 2021

@author: fatimazahraelmansouri
"""

import time
import googletrans
from googletrans import Translator
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import googletrans
from googletrans import Translator
from selenium import webdriver
import time
productlinks=[]
#page 1
e='AIDB'


url='https://www.iadb.org/en/procurement-notices-search?page=0'
from selenium.webdriver.firefox.options import Options
#options = Options()
#options.headless = True
driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')#,options=options)
driver.get(url)
driver.execute_script("window.scrollTo(0, 600)") 
stdquery= driver.find_element_by_xpath('/html/body/div[1]/div[2]/footer/div/div/div/div/div/div/div/div[2]/button[3]')
stdquery.click()
time.sleep(10)

download=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/main/section/div[1]/div/article/div/div[3]/div[2]/article/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/i')
download.click()
time.sleep(10)

print('click save to save the IDB opportunities into your donwloads folder')


import glob
import os
import csv
import pandas as pd
import pathlib
from pandas import *
import xlsxwriter

all_files = glob.glob('/Users/fatimazahraelmansouri/Downloads/*.xlsx') #User input: give path to your downloads folder file path
latest_xlsx_path = max(all_files, key=os.path.getctime)
print (latest_xlsx_path)
path = pathlib.PurePath(latest_xlsx_path)
latest_xlsx_name=path.name
print(latest_xlsx_name)
# =============================================================================
# f = open(latest_csv)
# csv_f = csv.reader(f)
# =============================================================================
file = open(latest_xlsx_path)
# =============================================================================

df=pd.read_excel(latest_xlsx_path)
               #skiprows=4,  skipfooter=4 )

df.columns=['Document Number','Notice Type','Country','title_or','Project Number','date','submission date','Sector Name',"Loan Number", "Project Name"]

df[['date', 'time']] = df['date'].str.split('T', expand=True)

df[['submission date', 'time2']] = df['submission date'].str.split('T', expand=True)

df.drop('time', inplace=True, axis=1)
df.drop('time2', inplace=True, axis=1)

ll=[]
for row in df.Country:
    enti='IADB'
    
    ll.append(enti)
en=pd.DataFrame(ll)
idb=pd.merge(df,en,right_index=True, left_index=True)
idb.columns=['Document Number','Notice Type','Country','title_or','Project Number','date','submission date','Sector Name',"Loan Number", "Project Name","Entity"]
ii=idb.sort_values('date',ascending=False)
iii=ii.iloc[:41,:]

a=iii['title_or'] 
translator = google_translator()   
for element in a:
    # add translation to the dictionary
    translations[element] = translator.translate(element)
    data_items = translations.items()
    data_list = list(data_items)
    z = pd.DataFrame(data_list)
    z.columns=['title_or','title']

table=pd.merge(iii,z,right_index=True, left_index=True)
final=table.drop(columns=['title_or_x','title_or_y'])
#translation

#from deep_translator import LingueeTranslator
#word = 'good'
#translated_word = LingueeTranslator(source='english', target='french').translate(word, return_all=True)

#from translate import Translator

# translations = {}
# lation = []
# for element in a:
#     # add translation to the dictionary
#     translations[element] = translator.translate(element)
#     data_items = translations.items()
#     data_list = list(data_items)
#     z = pd.DataFrame(data_list)
    
#     z.columns=['title_or','title']
#     type(z)
#     zw=z.drop(columns=['title_or'])
#     zw.reset_index(drop=True)
# lkj=[]
# from deep_translator import GoogleTranslator
# for element in a:
#     translated = GoogleTranslator(source='auto', target='en').translate(element)
    
#     print(translated)
#     data_ = list(translated)
#     z = pd.DataFrame(data_)
   



