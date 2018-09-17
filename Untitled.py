
# coding: utf-8

# In[141]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df = pd.read_csv('https://cocl.us/datasciece_survey_data')

print ('Data read into a pandas dataframe!')

df.rename(columns={'What\'s your level of interest for the following areas of Data Science? [Data Visualization]':'Data Visualization', 'What\'s your level of interest for the following areas of Data Science? [Machine Learning]':'Machine Learning'}, inplace=True)
df.rename(columns={'What\'s your level of interest for the following areas of Data Science? [Data Analysis / Statistics]':'Data Analysis / Statistics', 'What\'s your level of interest for the following areas of Data Science? [Big Data (Spark / Hadoop)]':'Big Data (Spark / Hadoop)'}, inplace=True)
df.rename(columns={'What\'s your level of interest for the following areas of Data Science? [Data Journalism]':'Data Journalism', 'What\'s your level of interest for the following areas of Data Science? [Deep Learning]':'Deep Learning'}, inplace=True)
df=df.drop("Timestamp", axis=1)

df.head()


# In[16]:


df.head()


# In[142]:


df["Category"]=df["Deep Learning"]
df_group=df.groupby("Category",axis=0).count()
df_group=df_group.transpose()
df_group


# In[143]:


# use the inline backend to generate the plots within the browser
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot') # optional: for ggplot-like style
df_group=df_group[df_group.columns[::-1]]

df_group.sort_values(['Very interested'], ascending=False, axis=0, inplace=True)


df_group.head()
#df_group.plot(kind='bar', figsize=(20, 8))

#plt.ylabel('Number of Immigrants')
#plt.title('Icelandic Immigrants to Canada from 1980 to 2013')
#plt.show()


# In[144]:


df_group["Very interested"]=df_group["Very interested"]/len(df.index)
df_group["Somewhat interested"]=df_group["Somewhat interested"]/len(df.index)
df_group["Not interested"]=df_group["Not interested"]/len(df.index)


# In[58]:





# In[59]:


df_group


# In[145]:


df_group.head()
df_group.plot(kind='bar', figsize=(20, 8), width=0.8, color=['#5cb85c', '#5bc0de', '#d9534f']
)

plt.title('Percentage of Respondents\' Interest in Data Science',fontsize=16)
mpl.rc('xtick', labelsize=14) 
mpl.rc('ytick', labelsize=14) 
mpl.rc('figure', titlesize=16) 
# remove all the ticks and directly label each bar with respective value
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')


mpl.rc('legend',fontsize=14)

for i, row in enumerate(df_group.values):
    count=0
    for value in row:
        val=value*100
        label = "{0:.2f}".format(float(val))+"%"
        plt.annotate(label, xy=(i-0.35+count*0.25,value+0.01), color='black', fontsize=14)
        count=count+1
plt.show()

