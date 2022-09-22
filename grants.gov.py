#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:15:47 2021

@author: fatimazahraelmansouri
"""
#this is the right code for grants.gov
import requests
import pandas as pd
import json


url = "https://www.grants.gov/grantsws/rest/opportunities/search"

payload = {
    "startRecordNum": 0,
    "sortBy": "openDate|desc",
    "oppStatuses": "forecasted|posted"
}

data = requests.post(url, json=payload).json()

# uncomment to print all data:
print(json.dumps(data, indent=4))

df = pd.DataFrame(data["oppHits"])
df["cfdaList"] = df["cfdaList"].apply(lambda x: ", ".join(x))
print(df)
#dff = pd.DataFrame(data["fundingCategories"])

#df.to_csv("data.csv", index=False)








