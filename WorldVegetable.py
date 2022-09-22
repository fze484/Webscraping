#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:15:00 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib
import re
from selenium import webdriver

URL= "https://avrdc.org/join-us/consultants/"
r=requests.get(URL)
soup = BeautifulSoup(r.content,"lxml")

contain=soup.findAll("span")
for c in contain:
   title= c.find("a").text
   print(title)
