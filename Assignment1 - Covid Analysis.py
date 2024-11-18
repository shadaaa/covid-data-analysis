#!/usr/bin/env python
# coding: utf-8

# # Problem for Covid-19 Data Analysis Project using Python
# ---------------------------------------------------------------------------

# ## Perform following analysis on the above dataset
# 

# ### 1. Import the dataset using Pandas from  above mentioned URL.

# In[4]:


import pandas as pd
url = "https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv"
data = pd.read_csv(url)


# In[10]:


data


# ### 2. High level Data Understanding
# 

# In[13]:


# a. Find no. of rows & columns in the dataset
rowcol = data.shape
print("number of rows = ",rowcol[0],"and number of columns =",rowcol[1])


# In[14]:


#b. Data types of columns
data.dtypes


# In[20]:


# c. info & describe of data in dataframe
#statistical information
data.describe()



# In[19]:


#detailed information
data.info()


# ### Low Level Data Understanding

# In[24]:


#a. find count of unique values in location column
unique_count = data['location'].nunique()
unique_count


# In[33]:


#b. Find which continent has maximum frequency using values counts.
count_value = data['continent'].value_counts()
max_continent = count_value.idxmax()
print("The continent with max value is",max_continent,"with count of",count_value.max())


# In[35]:


### c. Find maximum & mean value in 'total_cases'.
maximum_value = data['total_deaths'].max()
maximum_value


# In[37]:


mean_value =  data['total_deaths'].mean()
mean_value


# In[39]:


#Find 25%,50% & 75% quartile value in 'total_deaths'.
stati_data = data['total_deaths'].describe()
print("The 25% is",stati_data["25%"])
print("The 50% is",stati_data["50%"])
print("The 75% is",stati_data["75%"])


# In[45]:


#e.Find which continent has maximum 'human_development_index'.
continent_grp=data.groupby('continent')['human_development_index'].max()
continent_max_hdi = continent_grp.idxmax()
max_amnt = continent_grp.max()
print("The continent with maximum HDI is",continent_max_hdi,"with hdi of",max_amnt)


# In[46]:


#f. Find which continent has minimum 'gdp_per_capita'.
continent_grps=data.groupby('continent')['gdp_per_capita'].min()
continent_m = continent_grp.idxmin()
min_amnt = continent_grp.min()
print("The continent with minimum GDP is",continent_m,"with GDP of",min_amnt)


# In[65]:


#4. Filter the dataframe with only this columns['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index'] and update the data frame.
data=data[['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']]
data


# ### 5. Data Cleaning

# In[66]:


#a. Remove all duplicates observations
data = data.drop_duplicates()


# In[67]:


#b. Find missing values in all columns'
data.isnull().sum()


# In[69]:


# c. Remove all observations where continent column value is missing
data = data.dropna(subset=['continent'])


# In[70]:


#d. Fill all missing values with 0
data = data.fillna(0)


# ## 6. Date time format

# In[71]:


#a. Convert date column in datetime format using pandas.to_datetime
data['date'] = pd.to_datetime(data['date'])


# In[61]:


# b. Create new column month after extracting month data from date column.
datas['month'] = datas['date'].dt.month


# ### Data Aggregation

# In[73]:


df_groupby = data.groupby('continent').max().reset_index()
df_groupby


# ### 8. Feature Engineering

# In[74]:


# a. Create a new feature 'total_deaths_to_total_cases' by ratio of'total_deaths' column to 'total_cases'
df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']


# In[75]:


df_groupby


# ### 9. Data Visualization :

# In[76]:


#a. Perform Univariate analysis on 'gdp_per_capita' column byplotting histogram using seaborn dist plot.
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(20,12))
sns.histplot(df_groupby['gdp_per_capita'],kde=True)
plt.title("Distribution of GDP Capita")
plt.xlabel("GDP per Capita")
plt.ylabel("Count")
plt.show()


# In[87]:


#b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita'
plt.figure(figsize=(10,7))
plt.scatter(df_groupby['total_cases'],df_groupby['gdp_per_capita'])
plt.xlabel('total cases')
plt.ylabel('gdp per capita')
plt.title('Scatter plot')
plt.show()


# In[88]:


# Plot Pairplot on df_groupby dataset.
plt.figure(figsize=(20,10))
sns.pairplot(df_groupby)
plt.show()


# In[90]:


sns.catplot(data=df_groupby,x='continent',y='total_cases',kind='bar',aspect=1.5)
plt.title('Total cases in continents')
plt.xlabel("CONTINENT")
plt.ylabel('TOTAL CASES')
plt.show()


# In[91]:


df_groupby.to_csv('df_groupby.csv',index = True)

