#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:29:53 2021

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

URL="https://www.mcc.gov/resources/doc/report-business-forecast-fy-2020"

driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
driver.get(URL)
time.sleep(3)

sort_xpath='//*[@id="table_1_wrapper"]/div[1]/a[3]/span'
list_ch=driver.find_element_by_xpath(sort_xpath)
ActionChains(driver).click(list_ch).perform()
time.sleep(2)

flag_xpath='//*[@id="ENGLISH"]'
list_ch=driver.find_element_by_xpath(flag_xpath)
ActionChains(driver).click(list_ch).perform()
time.sleep(5)

import glob
import os
import csv
import pandas as pd
import pathlib
from pandas import *
import xlsxwriter

p=input('Please enter the path of your downloads folder')

all_files = glob.glob('/Users/fatimazahraelmansouri/Downloads/*.csv') #User input: give path to your downloads folder file path
latest_csv_path = max(all_files, key=os.path.getctime)
print (latest_csv_path)
path = pathlib.PurePath(latest_csv_path)
print(path)
latest_csv_name=path.name
print(latest_csv_name)
file = open(latest_csv_path)
df=pd.read_csv(latest_csv_path)



