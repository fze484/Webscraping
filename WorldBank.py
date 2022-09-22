#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:56:25 2021

@author: fatimazahraelmansouri
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from bs4 import BeautifulSoup 
import pandas as pd
import requests
from requests_html import HTMLSession
session = HTMLSession()
import re

# URL='https://wbgeconsult2.worldbank.org/wbgec/index.html#$h=1582042296662'

# #Enter Gecko driver path
# driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')

# driver.get(URL)
# # driver.minimize_window()

# opp_path='//*[@id="menu_publicads"]/a'
# list_ch=driver.find_element_by_xpath(opp_path)
# ActionChains(driver).click(list_ch).perform()
# time.sleep(5)

# sort_xpath='//*[@id="jqgh_selection_notification.publication_date"]'
# list_ch=driver.find_element_by_xpath(sort_xpath)
# ActionChains(driver).click(list_ch).perform()
# time.sleep(5)

# sort_xpath='//*[@id="jqgh_selection_notification.publication_date"]'
# list_ch=driver.find_element_by_xpath(sort_xpath)
# ActionChains(driver).click(list_ch).perform()
# time.sleep(5)


import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://wbgeconsult2.worldbank.org/wbgect/gwproxy"
data = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><GetCurrentPublicNotifications xmlns="http://cordys.com/WBGEC/DBT_Selection_Notification/1.0"><NotifTypeId3 xmlns="undefined">3</NotifTypeId3><DS type="dsort"><selection_notification.eoi_deadline order="asc"></selection_notification.eoi_deadline></DS></GetCurrentPublicNotifications></soapenv:Body></soapenv:Envelope>"""

soup = BeautifulSoup(requests.post(url, data=data).content, "xml")

# uncomment this to print all data:
# print(soup.prettify())

data = []
for sn in soup.select("SELECTION_NOTIFICATION"):
    d = {}
    for tag in sn.find_all(recursive=False):
        d[tag.name] = tag.get_text(strip=True)
    data.append(d)

df = pd.DataFrame(data)
print(df)

df['PUBLICATION_DATE']=df['PUBLICATION_DATE'].str.replace("T00:00:00.0","")

import dateparser

dd=[]
for row in df.iterrows():
    forma = row[1]['PUBLICATION_DATE']  
    date=dateparser.parse(forma).strftime("%d %B, %Y")
    dic= {  
        'date':date,
      }
    dd.append(dic)
dates=pd.DataFrame(dd)
dates=dates.reset_index(drop=True)

df=pd.merge(dates,df,right_index=True,left_index=True)
df=df.drop(['PUBLICATION_DATE'], axis=1)

df.sort_values(by='date')
df.columns = df.columns.str.replace('TITLE', 'title')

# response = session.get(URL)
# soup = BeautifulSoup(response.content, "html.parser")

# job_elms = soup.find_all('tr', class_=clas1)
# print(job_elms)

# for i in job_elms:
#     title = i.find('td').text
#     print(title)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



