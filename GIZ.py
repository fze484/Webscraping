#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:02:29 2021

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
from google_trans_new import google_translator  



URL='https://ausschreibungen.giz.de/Satellite/company/welcome.do'
#Setting website to French
# driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
# driver.get(URL)
# time.sleep(3)

# sort_xpath='/html/body/div[1]/div[2]/ul[1]/li/a/span'
# list_ch=driver.find_element_by_xpath(sort_xpath)
# ActionChains(driver).click(list_ch).perform()
# time.sleep(2)

# flag_xpath='//*[@id="ENGLISH"]'
# list_ch=driver.find_element_by_xpath(flag_xpath)
# ActionChains(driver).click(list_ch).perform()
# time.sleep(5)

#extracting table, creating DF
df=pd.read_html(URL) #use parse_dates=True to change format of dates
df=np.array(df)

q=pd.DataFrame(np.concatenate(df))
p=pd.DataFrame(q)
p.head(15)
p.columns=['date','submission deadline','title_german','Type','Entity','URL','Unnamed']
p.drop(p.tail(1).index,inplace=True)
print(p)
type(p)
# p.to_csv('GIZ.csv')


# data = pd.read_csv("GIZ.csv")

#Translate dataframe, remove extra columns and add links in the right column
df_en=p.copy()

translator = google_translator()  
a=df_en['title_german']
translations = {}
for element in a:
    # add translation to the dictionary
    translations[element] = translator.translate(element)
    data_items = translations.items()
    data_list = list(data_items)
    z = pd.DataFrame(data_list)
    z.columns=['title_german','title']
    type(z)
    z0=z.reset_index()
p0=p.reset_index()

fa=pd.merge(p0,z0,right_index=True, left_index=True)
giz=fa.drop(columns=['index_x', 'index_y','title_german_x','title_german_y','Unnamed'])
# df_en['title'].replace({z}, inplace=True)



