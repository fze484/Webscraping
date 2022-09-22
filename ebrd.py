#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:01:33 2021

@author: fatimazahraelmansouri
"""
#################### EBRD 1############################
from urllib.request import urlretrieve 
from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import urllib.request
import pandas as pd
import io
import requests
from requests_html import HTMLSession
session = HTMLSession()
import numpy as np
import re

URL = 'https://www.ebrd.com/work-with-us/project-finance/project-summary-documents.html'
response = session.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

#search_for_stringonly = soup.find(text="bonds")
#print(search_for_stringonly)

links=[]  
ebrdlist=[]
  
# "Getting dates"
#dates = soup.find('tr',class_="post").find("td")
job_elems = soup.find_all('tr',class_="post")
for i in job_elems:
    dates=i.find("td").text.strip()
    
    children=i.findChildren('a')
    for child in children:
        title=child.get('title')
        
    entity=["EBRD"]
    
    prd=i.find_all('a',href=True)
    for link in prd:
        links.append(link['href'])
        
    ebrd= {'title':title,
           'date':dates,
           'Entity':entity,
           'URL':links               
           }          
    ebrdlist.append(ebrd)
    #print("Saving:",ebrd['title'])
    df1=pd.DataFrame(ebrdlist)
     
# # "Getting titles"
# job_elems = soup.find_all('td')    
# for i in job_elems:
#     children=i.findChildren('a')
#     for child in children:
#         title=np.array(child.get('title'))
        
# # "Getting links"             
# productlist=soup.findAll('td')
# for item in productlist:
#     for link in item.find_all('a',href=True):
#         links.append(link['href'])
#         entity=["EBRD"]

# df=pd.DataFrame()
# df['date'] = [dates]
# print(df)
# df['bua'] = [data.text for data in bua]

# print (entity)  
# print (links)
              
# ebrd= {'title':title,
#            'date':dates,
#            'Entity':entity,
#            'URL':links               
#            }      
# ebrdlist=[]
# ebrdlist.append(ebrd)
# print("Saving:",ebrd['title'])
# df=pd.DataFrame(ebrdlist)
# print(df.head(15))   


    # for p_job in job_elems:
    #     link = p_job.find('a')['href']
    #     print(p_job.text.strip())
    #     print(f"Apply here: {link}\n")
              
    #     for child in i:
    #         links.append(child['href'])
    #         entity="EBRD"  

    
    # x = job_elems['a'].get('title')
    # print(x)
# "Getting dates"
# job_elems = soup.find_all('tr',class_="post")
# print(job_elems)
# for i in job_elems:
#     c=i.findChildren("dt")
#     dates=i.text.replace("						","")
#     print(dates)

######################## EBRD 2 #################################
#https://www.ebrd.com/work-with-us/project-finance/technical-cooperation-project-summary-documents.html
URL = 'https://www.ebrd.com/work-with-us/project-finance/technical-cooperation-project-summary-documents.html'
response = session.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


links=[]  
ebrdlist=[]
  
# "Getting dates"
#dates = soup.find('tr',class_="post").find("td")
job_elems = soup.find_all('tr',class_="post")
for i in job_elems:
    dates=i.find("td").text.strip()
    print(dates)
    children=i.findChildren('a')
    for child in children:
        title=child.get('title')
        print(title)
    entity=["EBRD"]
    print(entity)
    prd=i.find_all('a',href=True)
    for link in prd:
        links.append(link['href'])
        print(links)
    ebrd= {'title':title,
           'date':dates,
           'Entity':entity,
           'URL':links               
           }          
    ebrdlist.append(ebrd)
    print("Saving:",ebrd['title'])
    df2=pd.DataFrame(ebrdlist)
   
######################## EBRD 3 #################################
#https://www.ebrd.com/work-with-us/procurement/notices.html?1=1&filterContract=Consultancy%20Services
URL = 'http://www.ebrd.com/work-with-us/procurement/notices.html?1=1&filterContract=Consultancy%20Services'
response = session.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

links=[]  
ebrdlist=[]
  
# "Getting dates"
#dates = soup.find('tr',class_="post").find("td")
job_elems = soup.find_all('tr',class_="post")
for i in job_elems:
    dates=i.find("td").text.strip()
    print(dates)
    children=i.findChildren('a')
    for child in children:
        title=child.get('title')
        print(title)
    entity=["EBRD"]
    print(entity)
    prd=i.find_all('a',href=True)
    for link in prd:
        links.append(link['href'])
        print(links)
    ebrd= {'title':title,
           'date':dates,
           'Entity':entity,
           'URL':links               
           }          
    ebrdlist.append(ebrd)
    print("Saving:",ebrd['title'])
    df3=pd.DataFrame(ebrdlist)
      

