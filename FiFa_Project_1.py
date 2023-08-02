#!/usr/bin/env python
# coding: utf-8

# # ● Load and explore data 
# 1.Import the required libraries and read the dataset. 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv(r"C:\Users\Malang\Downloads\Dataset and relavant files - Python Project 1\fifa.csv")
data.head()


# 2.Check the first few samples, shape, info of the data 

# In[4]:


data.shape


# In[5]:


data.info()


# 3.Drop the columns which you think redundant for the analysis.

# In[6]:


data.drop('Photo', axis=1, inplace=True)
data.drop('Flag', axis=1, inplace=True)
data.drop('Club Logo', axis=1, inplace=True)

data.head()


# # Data Cleaning and Preprocessing 

# Convert the columns "Value", "Wage", "Release Clause" to float datatype 

# In[7]:


df=data.copy()


# In[15]:


df['Value']= df['Value'].str.replace('€','')


# In[16]:


df['Wage']= df['Wage'].str.replace('€','')


# In[17]:


df.Wage


# In[36]:


def convert_suffix_to_float(i):
    suffix = i[-1].upper()
    if suffix == 'M':
        return float(i[:-1]) * 1_000_000
    elif suffix == 'K':
        return float(i[:-1]) * 1_000
    else:
        return float(i)


# In[ ]:




