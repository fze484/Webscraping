#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:19:21 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
from selenium import webdriver

import time
URL="https://westafricatradehub.com/co-investment/ "

driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
driver.get(URL)
driver.execute_script("window.scrollTo(0, 1000)") 
time.sleep(5)

#titles
rt=[]
elems = driver.find_elements_by_xpath("//h2")
for e in elems:
    ti=e.text                 
    print(ti.strip)    
    dica= {  
        'title':ti,
      }
    rt.append(dica)
g5=pd.DataFrame(rt)

#Drop last n rows and first n rows
g5.drop(g5.tail(2).index,inplace=True)
g5.drop(g5.head(1).index,inplace=True)


####NEW CODE
rt=[]

alls = driver.find_elements_by_xpath("//main/div/div[2]")
for a in alls:
    elems = a.find_elements_by_xpath("//div/div/h2")
for e in elems:
    big=e.text
    small=e.find_elements_by_xpath('//p/a')
    for s in small:
        hh=s.get_attribute('href')     
                     
        dica= {  
        'title':big,
        'URL': hh 
        }
        rt.append(dica)
g5=pd.DataFrame(rt)

#Drop last n rows and first n rows
g5.drop(g5.tail(2).index,inplace=True)
g5.drop(g5.head(1).index,inplace=True)

driver.close()

#websites
#you can retrieve everything. Gotta do selection after. 
# aa=[]
# eee = driver.find_elements_by_xpath("//a")
# for e in eee:
#     oo=e.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/main/div/div[2]/p[2]/a')
#     for o in oo:
#         hh=o.get_attribute('href')   
#         dica= {  
#             'URL':hh,
#           }
#         aa.append(dica)
# gg2=pd.DataFrame(aa)
# print(gg2)
# gg3=gg2[gg2['URL'].str.contains(".pdf")]
# gg4=gg3.reset_index(drop=True)









