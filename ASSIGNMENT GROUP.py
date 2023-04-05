#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # IMPORT DATA

# In[3]:


data = pD.read_csv("epl21.csv")
data


# In[4]:


data.dtypes


# In[5]:


#tmpt true ade null value
data.isnull()


# In[6]:


check_null_value = pd.isnull(data["Penalties Saved"])
data[check_null_value]


# In[7]:


check_null_value = pd.isnull(data["Punches"])
data[check_null_value]


# In[8]:


check_null_value = pd.isnull(data["High Claims"])
data[check_null_value]


# In[9]:


check_null_value = pd.isnull(data["Catches"])
data[check_null_value]


# In[10]:


check_null_value = pd.isnull(data["Throw outs"])
data[check_null_value]


# In[11]:


data['Through balls'].isna().sum()


# In[12]:


data['Accurate long balls'].isna().sum()


# In[13]:


data['Own goals'].isna().sum()


# In[14]:


data['Big Chances Created'].isna().sum()


# In[15]:


data['Cross accuracy %'].isna().sum()


# In[16]:


data.isna().sum().sum()


# DROP COLUMN

# In[17]:


data.drop(('Last man tackles'), axis = 1, inplace = True)


# In[18]:


data.drop(('Punches'), axis = 1, inplace = True)


# In[19]:


data.drop(('High Claims'), axis = 1, inplace = True)


# In[20]:


data.drop(('Clearances off line'), axis = 1, inplace = True)


# In[21]:


data.drop(('Throw outs'), axis = 1, inplace = True)


# In[22]:


data


# AFTER DROP COLUMN

# In[23]:


data.isna().sum().sum()


# REPLACE NULL VALUE WITH ZERO

# In[24]:


data_fillna = data.fillna(0)


# In[25]:


data_new = data_fillna[data_fillna["Position"].isin(['Forward','Midfielder','Defender','Goalkeeper'])]
data_new


# In[26]:


grp1= data_new[['Name', 'Position', 'Goals','Assists', 'Passes']]
grp1.head()


# In[27]:


grp1.dtypes


# In[28]:


grp3 = data_new[['Name', 'Position', 'Yellow cards','Red cards', 'Fouls']]
grp3.head()


# In[29]:


grp3.dtypes


# In[30]:


grp2= data_new[['Name','Position','Clearances','Tackles']]
grp2.head()


# In[31]:


grp2.dtypes


# In[32]:


grp4 =  data_new.groupby(['Name'],as_index = False).Goals.mean()
grp_head=grp4.head()
grp_head


# In[33]:


grp4.dtypes


# In[34]:


df2 = pd.DataFrame(grp1)


# Vizualization

# In[35]:


viz1_grp1=df2.pivot(columns='Position',values='Assists').mean()
viz1_grp1.plot.bar(color='purple')


# Using choropleth

# Using seaborn

# In[36]:


df3=pd.DataFrame(grp2)


# In[37]:


viz2_grp2=df3.pivot(columns='Position',values='Clearances').mean()
viz2_grp2.plot.bar()


# In[38]:


df4 = pd.DataFrame(grp3)


# In[39]:


df4.groupby('Position').mean().plot(subplots = True)


# In[40]:


df5 = pd.DataFrame(grp_head)


# In[41]:


df5.groupby('Name')[['Goals']].mean().plot.barh(figsize=(6,6),color="Purple")
plt.show()                                    


# In[42]:


df_gk = data_new.query("Position=='Goalkeeper'")
df_gk


# In[43]:


gk_data = df_gk[['Name','Saves','Sweeper clearances','Penalties Saved','Clean sheets']].nlargest(5, ['Saves'])
gk_data


# In[44]:


gk_data.dtypes


# In[45]:


import seaborn as sns
import pandas


# In[46]:


sns.lineplot(gk_data["Name"], gk_data["Saves"], gk_data["Penalties Saved"])


# In[47]:


df_def = data_new.query("Position=='Defender'")
df_def


# In[48]:


def_data = df_def[['Name','Tackles','Blocked shots','Clearances','Appearances']].nlargest(3, ['Tackles'])
def_data


# In[49]:


def_data.dtypes


# In[50]:


sns.set(style='whitegrid')

sns.barplot(data=def_data, x='Name', y= 'Tackles')
plt.show()


# In[51]:


df_mid = data_new.query("Position=='Midfielder'")
df_mid


# In[52]:


mid_data = df_mid[['Name','Interceptions','Blocked shots','Tackles','Appearances']].nlargest(3, ['Tackles'])
mid_data


# In[53]:


sns.stripplot(x='Name',y='Tackles',data=mid_data)
plt.show()


# In[54]:


df_fwd = data_new.query("Position=='Forward'")
df_fwd


# In[55]:


fwd_data = df_fwd[['Name','Goals','Goals per match','Shooting accuracy %','Big chances missed']].nlargest(3, ['Goals'])
fwd_data


# In[56]:


sns.histplot(x="Name", y="Goals", data=fwd_data, color="Blue")
plt.show()

