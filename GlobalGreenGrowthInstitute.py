#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:46:55 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
import numpy as np
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import requests

URL="https://in-tendhost.co.uk/gggi/aspx/Tenders/Current"
# response = requests.get(URL)
# soup = BeautifulSoup(response.text, 'lxml')

driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
driver.get(URL)

da=[]
elems = driver.find_elements_by_xpath("//td")
for e in elems:
    ti=e.text                 
    print(ti.strip)
    dica= {  
        'elements':ti,
      }
    da.append(dica)
gg=pd.DataFrame(da)
#drop empty rows
nan_value = float("NaN")
gg.replace("", nan_value, inplace=True)
gg.dropna(subset = ["elements"], inplace=True)
print(gg)
gg.reset_index()

#drop last rows
gg1=gg.drop(gg.tail(12).index)
print(gg1)
gg1.reset_index()
d1=pd.DataFrame(np.hstack(np.split(gg1, 5)))

#transpose the DF
gggi=d1.T

#Name the columns
gggi.columns=["submission","title","id","type","date"]
print(gggi)


        




