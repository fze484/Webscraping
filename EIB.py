#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:38:53 2021

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
import html5lib
# translator = Translator()


URL='http://www.eib.org/en/about/procurement/index.htm'
driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
driver.get(URL)
r=requests.get(URL)


soup = BeautifulSoup(r.content,"lxml")
page = driver.page_source
page_soup = soup(page,'lxml')


url = 'https://www.eib.org/tools/jsp/calls.jsp?&lang=en&language=en&l=en&url=/about/procurement/index.htm&forceLanguage=en&_=1616778335822'
df = pd.read_html(url)[0]


df1=df['Status'].replace("OnÂ going","Ongoing",inplace=True)
df3=df['Title'].replace(" â ","",inplace=True)
df3=df.replace('\â','',regex=True)
# df3['Title'].str.replace(r'\W','',regex=True)
df4=df3[~df3.Status.str.contains("Closed")]
df5=df4.iloc[:25,:]
df5=df5.reset_index()
df5=df5.iloc[:,2:]

#retrieving links
understand_xpath='//*[@id="accept_cookies_footer"]'
understand_ch=driver.find_element_by_xpath(understand_xpath)
ActionChains(driver).click(understand_ch).perform()
time.sleep(5)

driver.execute_script("window.scrollTo(0, 500)")

orderby_id='status'
orderby = Select(driver.find_element_by_id(orderby_id))
orderby.select_by_visible_text('On going')


search_xpath='//*[@id="goPL"]'
search_ch=driver.find_element_by_xpath(search_xpath)
ActionChains(driver).click(search_ch).perform()
time.sleep(5)
driver.execute_script("window.scrollTo(0, 500)")

list_xpath='/html/body/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[3]/div[1]/select'
listp = Select(driver.find_element_by_xpath(list_xpath))
listp.select_by_visible_text('25')

elems = driver.find_elements_by_xpath("//td")
elems
eilist=[]
for elem in elems:
    e=elem.get_attribute("href")
    #emp.append(e)
    ent="EIB"
    dic= {  
        'URL':e,
        'Entity':ent
     }
    
    eilist.append(dic)
eil=pd.DataFrame(eilist)
eib=pd.merge(df5,eil,right_index=True,left_index=True)









