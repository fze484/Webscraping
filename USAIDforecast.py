#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 04:14:45 2021

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
import os
#from selenium.webdriver.firefox.options import Options
#options = Options()
#options.headless = True
URL="https://www.usaid.gov/business-forecast/search"

driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')#options=options)
driver.get(URL)
time.sleep(3)

sort_xpath='//*[@id="block-views-c4a94e1a2a5f9015218fd1a479737717"]/div/div/div[2]/span/a'
list_ch=driver.find_element_by_xpath(sort_xpath)
ActionChains(driver).click(list_ch).perform()
print("click save to download the USAID forecast opportunities")
time.sleep(5)

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

usf=pd.read_excel(latest_xlsx_path)
               #skiprows=4,  skipfooter=4 )

#usf.columns=['Document Number','Notice Type','Country','title_or','Project Number','date','submission date','Sector Name',"Loan Number", "Project Name"]



