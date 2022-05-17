#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[1]:


import pandas as pd
from urllib import request
import tempfile
from pathlib import Path


# In[2]:


with tempfile.TemporaryDirectory() as tmpdirname:
    # Define the remote file to retrieve
    remote_url = 'http://data.insideairbnb.com/greece/attica/athens/2021-12-23/visualisations/listings.csv'
    # Define the local filename to save data
    local_file = Path(tmpdirname) / 'listings.csv'
    # Download remote and save locally
    request.urlretrieve(remote_url, local_file)
    print('created temporary directory', tmpdirname)
    # read the airbnb NYC listings csv file
    airbnb = pd.read_csv(local_file)


# In[3]:


airbnb


# In[4]:


airbnb.head(10)


# In[5]:


airbnb.tail()


# In[6]:


# Results for a single column
airbnb['name']


# In[7]:


# results for multiple columns
hosts = airbnb[['host_id', 'host_name']]
hosts.head()


# In[8]:


# Show the data types for each column
airbnb.dtypes


# In[9]:


airbnb['last_review'] = pd.to_datetime(airbnb['last_review'])
airbnb.dtypes


# In[10]:


# extract the year from a datetime series
airbnb['year'] = airbnb['last_review'].dt.year

# to integer
airbnb['year'] = airbnb['year'].astype('UInt16')

airbnb['year'].head()


# In[11]:


# Strip leading and trailing spaces from a string series

airbnb['name'] = airbnb['name'].str.strip()
airbnb['name'].head()


# In[12]:


airbnb['name_lower'] = airbnb['name'].str.lower()
airbnb['name_lower'].head()


# In[13]:


# calculate using two columns
airbnb['min_revenue'] = airbnb['minimum_nights'] * airbnb['price']
airbnb[['minimum_nights', 'price', 'min_revenue']].head()


# In[14]:


# get the mean price
airbnb['price'].mean()


# In[15]:


# get the median price
airbnb['price'].median()


# In[16]:


# get the mean grouped by type of room
airbnb[['room_type', 'price']].groupby('room_type', as_index=False).mean()


# In[17]:


# get the median grouped by type of room
airbnb[['room_type', 'price']].groupby('room_type', as_index=False).median()


# In[18]:


# get the median grouped by type of room and year
airbnb[['room_type', 'year', 'price']].groupby(['room_type', 'year'], as_index=False).median()


# In[19]:


# get all rows with price < 1000
airbnb_under_1000 = airbnb[airbnb['price'] < 1000]
airbnb_under_1000.head()


# In[20]:


# get all rows with price < 1000 and year equal to 2020
airbnb_2019_under_1000 = airbnb[(airbnb['price'] < 1000) & (airbnb['year'] == 2020)]
airbnb_2019_under_1000.head()


# In[21]:


# distribution of prices under $1000
ax = airbnb_under_1000['price'].plot.hist(bins=40)


# # Βιβλιογραφία
# https://www.datacamp.com/tutorial/pandas

# In[ ]:




