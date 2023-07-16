#!/usr/bin/env python
# coding: utf-8

# # 1. Load and sense check the three data sets

# In[1]:


# Import pandas and numpy

import pandas as pd
import numpy as np


# # Actual_Duration.csv

# In[11]:


# load the three csv files. 
# Set actual_duration.csv as ad, appointments_regional.csv as ar, and national_categories.xlsx as nc.

ad = pd.read_csv('actual_duration.csv')

display(ad)

# number of rows and columns, data types, and number of missing values. 

print(ad.dtypes)


# In[14]:


# check for number of missing values. no rows with NaN in 8 columns
ad_na = ad[ad.isna().any(axis=1)]
ad_na.shape


# In[20]:


# Determine Descriptive Statistics

ad.describe()


# In[21]:


ad.info()


# # Appointments_regional.csv

# In[8]:


ar = pd.read_csv('appointments_regional.csv')

display(ar)

print(ar.dtypes)


# In[15]:


# check for number of missing values. no rows with NaN in 7 columns
ar_na = ar[ar.isna().any(axis=1)]
ar_na.shape


# In[22]:


# Determine Descriptive Statistics

ar.describe()


# # national_categories.xlsx

# In[46]:


nc = pd.read_excel('national_categories.xlsx')

display(nc)

print(nc.dtypes)


# In[16]:


# check for number of missing values. no rows with NaN in 8 columns
nc_na = nc[nc.isna().any(axis=1)]
nc_na.shape


# In[24]:


# Determine Descriptive Statistics

nc.describe()


# # Explore data to respond to objectives

# In[25]:


# Use the value.counts(), count(), and print() methods. 
# Inset an appropriate docstring to present your output in a sensible way. 
# For example, print("Count of locations: ", …]).
# Use the nc DataFrame and appropriate column names (e.g. sub_icb_location_name).


# # How many locations are there in the data set?

# In[38]:


# Counting Unique Values

nc_locations = len(pd.unique(nc['sub_icb_location_name']))
print("Count of locations: ", nc_locations)


# In[39]:


nc_locations_list = nc['sub_icb_location_name'].value_counts()
nc_locations_list


# # What are the five locations with the highest number of records? 

# In[41]:


nc_locations_list = nc['sub_icb_location_name'].value_counts(sort=True)
nc_locations_list


# # How many service settings, context types, national categories, and appointment statuses are there?

# In[43]:


# Counting Unique Values for service settings

nc_ss = len(pd.unique(nc['service_setting']))
print("Count of service settings: ", nc_ss)


# In[44]:


# Counting Unique Values for countext types

nc_cc = len(pd.unique(nc['context_type']))
print("Count of context types: ", nc_cc)


# In[45]:


# Counting Unique Values for national categories

nc_nc = len(pd.unique(nc['national_category']))
print("Count of national categories: ", nc_nc)


# In[48]:


# Counting Unique Values for appointment statuses? 

ar_as = len(pd.unique(ar['appointment_status']))
print("Count of appointment statuses: ", ar_as)


# In[ ]:




