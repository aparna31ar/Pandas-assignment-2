#!/usr/bin/env python
# coding: utf-8

# ### Import the necessary libraries

# In[1]:


import pandas as pd


# ### Import the dataset from this(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
# Use sep= "|" while reading the data

# In[4]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
df=pd.read_csv(url)


# In[5]:


df.head()


# ### Assign it to a variable called users and use the 'user_id' as index

# In[10]:


users=pd.read_csv(url, sep="|" , index_col="user_id")
users


# ### See the first 10 and last 10 entries

# In[13]:


print("First 10 enteries")
users.head(10)


# In[12]:


print("Last 10 enteries")
users.tail(10)


# ### What is the number of observations in the dataset?

# In[16]:


print("Number of observation are: ")
users.shape[0]


# ### What is the number of columns in the dataset?

# In[18]:


len(users.columns)


# ### Print the name of all the columns.

# In[19]:


users.columns


# ### How is the dataset indexed?

# In[20]:


users.index


# ### What is the data type of each column?

# In[21]:


users.dtypes


# ### DataFrame Info.

# In[24]:


users.info()


# ### Print only the occupation column

# In[25]:


users['occupation']


# ### How many different occupations are in this dataset?

# In[27]:


users['occupation'].value_counts().count()


# ### What is the most frequent occupation?

# In[29]:


users["occupation"].value_counts().sort_values(ascending=False).head(1)


# ### Describe all the columns

# In[30]:


users.describe


# ### Summarize only the occupation column

# In[31]:


users['occupation'].value_counts()


# ### What is the mean age of users?

# In[32]:


users['age'].mean()


# ### What is the age with least occurrence?

# In[33]:


users['age'].value_counts().tail(1)


# In[ ]:




