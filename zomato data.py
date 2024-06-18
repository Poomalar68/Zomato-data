#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


pip install matplotlib


# In[ ]:


pip install numpy


# In[ ]:


pip install seaborn


# In[ ]:


import pandas as pd
import numpy as np
import matplotlib as mlt
import seaborn as sns


# In[ ]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe.head())


# In[ ]:


def handRate (value):
    value = str (value).split('/')
    value =value[0]
    return float(value)
dataframe['rate']= dataframe['rate'].apply(handRate)
print(dataframe.head())


# In[ ]:


DataFrame.head()


# In[ ]:


DataFrame.info()


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


sns.countplot(x=dataframe ['listed_in(type)'])
plt.xlabel("Type of Restaurant")


# In[ ]:


grouped_data = dataframe.groupby ('listed_in(type)')['votes'].sum()
result= pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='green',marker = 0)
plt.xlabel("Type of Restaurant",c = 'blue',size = 20)
plt.ylabel("Values",c= 'blue', size = 20 )


# In[ ]:


max_votes = DataFrame['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes']== max_votes , 'name']
print("Restaurant(s) with maximum votes:")
print(restaurant_with_max_votes)


# In[ ]:


sns.countplot(x=dataframe['online_order'])


# In[ ]:


plt.hist(dataframe ['rate'],bins = 5)
plt.title(" Rate Distribuation")
plt.show()


# In[ ]:


couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# In[ ]:


plt.figure(figsize =(6,6))
sns.boxplot(x='online_order',y='rate', data= dataframe)


# In[ ]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()


# In[ ]:




