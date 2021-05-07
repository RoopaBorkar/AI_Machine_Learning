#!/usr/bin/env python
# coding: utf-8

# # Fetching the data from REST API 

# In[1]:


import requests


# In[2]:


response=requests.get('https://api.covid19api.com/summary').text


# In[3]:


response


# # Json data is loaded as Dictionary

# In[4]:


import json


# In[5]:


response_info=json.loads(response)


# In[7]:


type(response_info)


# # Defining a list where values from dictionary with Key as Country and Total Confimed are appended

# In[10]:


country_list=[]


# In[13]:


for country_info in response_info['Countries']:
    country_list.append([country_info['Country'],country_info['TotalConfirmed']])


# In[14]:


country_list


# # Reading the data in panads dataframe

# In[15]:


import pandas as pd


# In[17]:


country_df=pd.DataFrame(data=country_list,columns=['Country','Total Confirmed'])


# In[18]:


country_df.head(7)


# # Plotting the Covid Data in bar chart

# In[21]:


import matplotlib.pyplot as plot


# In[28]:


country_df.plot.bar(x="Country", y="Total Confirmed", rot=100000000, title="Number of Covid Cases - Year 2021");

plot.show(block=True);


# In[30]:


country_df.describe()


# In[37]:


country_max=country_df['Total Confirmed'].max()


# In[34]:


country_max

