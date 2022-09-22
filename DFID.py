#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 04:03:40 2021

@author: fatimazahraelmansouri
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re
import time

URL='https://www.gov.uk/topic/legal-aid-for-providers/tenders'
URL2='https://www.gov.uk'
re=requests.get(URL)
soup=BeautifulSoup(re.content,'lxml')
links=[]  
liste=[] 
grid=soup.findAll('ul',class_='app-c-topic-list')
for g in grid:    
   #retrieving title of tender, and name of entity    
   children=g.findChildren('li',class_='app-c-topic-list__item')
   for child in children:
       title=child.find('a').text
       entity='DFID'       
       d= {'title':title,     
            'Entity':entity,
              
            }          
       liste.append(d)       
   #retrieving links to tenders
   prd=g.find_all('a',href=True)
   for link in prd:
       links.append(URL2+link['href']) 
df=pd.DataFrame(links)
df.columns=['URL'] 
      
df1=pd.DataFrame(liste)
df1.reset_index(drop=True)

dfi=pd.merge(df1,df,right_index=True,left_index=True)           

# dfid.head(10)           

#Getting date on which tender was published
lt=[] 
driver=webdriver.Firefox(executable_path ='/Users/fatimazahraelmansouri/geckodriver')
for row in df.URL:
    driver.get(row)
    page = driver.page_source
    date=driver.find_element_by_xpath('/html/body/div[6]/main/div[2]/div/div[1]/div/dl/dd[2]')
    dates=date.text
    dic= {'date':dates,             
            }          
    lt.append(dic)
    time.sleep(5)           
dates=pd.DataFrame(lt)

dfid=pd.merge(dfi,dates,right_index=True,left_index=True)           


#########################################################################################################               
#######################################################################################################                
#########################################################################################################               
#######################################################################################################                
###### Iterating through rows and parsing URLs in DF
# import bs4 as bs
# import pandas as pd
# import urllib.request

# fr=[]
# wanted = ['tender','2020','date'] 
# for link in df.iterrows():
#     url = link[1]['URL']
#     x = urllib.request.urlopen(url)
#     new = x.read()
#     soup = bs.BeautifulSoup(new,"lxml")
#     for word in wanted:
#         a=requests.get(url).text.count(word)
#         dic={'phrase':word,
#              'frequency':a,
#              'URL':url                 
#                 }          
#         fr.append(dic)  

# data=pd.DataFrame(fr) 
# data1=data.T       
#########################################################################################################               
#######################################################################################################                     
#########################################################################################################               
#######################################################################################################                

    #print(len(re.findall(r'\Wtender\W', requests.get(row).text)))
    
    # cnt = Counter()
    # words = re.findall('\W+', requests.get(row).text)
    # for word in words:
        
    #     if word in wanted:
    #         cnt[word] += 1
    # print (cnt)

# for row in df.URL:
#     r=requests.get(row)
#     soup1=BeautifulSoup(r.content,'lxml')
#     fr=[] 
#     wanted = ['tender','2020','date']    
#     for word in wanted:
#         a=requests.get(row).text.count(word)
#         dic={'phrase':word,
#              'frequency':a,              
#                 }          
#         fr.append(dic)  
#         print('Frequency of',word, 'is:',a)
# data=pd.DataFrame(fr)    


###Counting word frequency from list of words, in 1 webpage###
# fr=[] 
# wanted = ['tender','2020','date']    
# for word in wanted:
#     a=requests.get(URL).text.count(word)
#     dic={'phrase':word,
#           'frequency':a,              
#             }          
#     fr.append(dic)  
#     print('Frequency of',word, 'is:',a)
# data=pd.DataFrame(fr)        
            

           