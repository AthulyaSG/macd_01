#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('data/AAPL.csv')


# In[3]:


data.head()


# In[4]:


data[['Open']].plot()


# In[5]:


data.dtypes


# In[6]:


data['Date'] = pd.to_datetime(data['Date'])


# In[7]:


data = data.set_index('Date')


#     data[index_col] = pd.to_datetime(data[index_col]) 
#     data = data.set_index(index_col)

# In[8]:


data.describe()


# In[9]:


data.plot()


# In[10]:


data['Open'].plot()


# In[11]:


data.info()


# In[12]:


data.columns


# In[13]:


data.dtypes


# In[14]:


data.describe()


# In[15]:


data.info


# In[16]:


data.describe


# In[17]:


data.info


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




