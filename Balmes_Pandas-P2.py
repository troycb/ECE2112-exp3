#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## Problem 2

# In[3]:


cars = pd.read_csv('cars.csv')
cars


# In[6]:


cars.iloc[0:5,1::2]


# In[8]:


cars.loc[cars['Model']=='Mazda RX4']


# In[16]:


cars.loc[cars['Model']=='Camaro Z28',['cyl']]


# In[14]:


cars.loc[cars['Model'].isin(["Mazda RX4 Wag", "Ford Pantera L", "Honda Civic"]), ['cyl', 'gear']]

