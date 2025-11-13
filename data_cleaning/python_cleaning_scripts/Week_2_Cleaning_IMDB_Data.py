#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Week 2: Cleaning IMDb Dataset (Handling Missing Values, Outliers, and Duplicates)

# This notebook contains all Python-based cleaning steps derived from insights gathered during the OpenRefine exploration.
# Please review the OpenRefine documentation beforehand, as it thoroughly explains the visual findings that guide our cleaning process.
# OpenRefine was used to visually identify inconsistencies, formatting issues, and potential data discrepancies.
# Python is used here to carry out precise and reproducible data cleaning for the IMDb dataset.
# A separate notebook contains the TMDB data cleaning process, the two datasets were divided for clarity and ease of visibility.


# In[20]:


#import functions

import requests
import pandas as pd
from datetime import datetime
import json
import os
import hashlib
from pathlib import Path
import numpy as np
import gzip
import io


# In[21]:


#confirm raw dataset is read in properly

imdb = pd.read_csv('imdb_top_1000.csv')


# In[22]:


imdb.head()


# In[24]:


#Now that the dataset is loaded in, I will proceed to clean the imdb data

# Check data types, missing values, and overall info
imdb.info()

# Look for duplicate rows (just to confirm none slipped in)
imdb.duplicated().sum()


# In[25]:


# Check for repeated titles to confirm what OpenRefine found
duplicate_titles = imdb[imdb.duplicated(subset='title', keep=False)].sort_values('title')
duplicate_titles


# In[26]:


# Strip whitespace from director names to avoid any hidden inconsistencies
imdb['director'] = imdb['director'].str.strip()

# Check unique director count and sample a few names to confirm theres no odd whitespaces
print("Unique directors:", imdb['director'].nunique())
imdb['director'].sample(5)


# In[27]:


# Remove parentheses and Roman numeral suffixes like (I), (II), (III)
imdb['release_year'] = imdb['release_year'].str.replace(r'\(|\)', '', regex=True)
imdb['release_year'] = imdb['release_year'].str.replace(r'(I+)$', '', regex=True)

# Strip any trailing whitespaces to confirm its read in correctly 
imdb['release_year'] = imdb['release_year'].str.strip()

# Convert to numeric (integer)
imdb['release_year'] = pd.to_numeric(imdb['release_year'], errors='coerce').astype('Int64')

# Mark empty or invalid release years as NaN
imdb['release_year'] = pd.to_numeric(imdb['release_year'], errors='coerce')

# Drop rows where release_year is missing
imdb = imdb.dropna(subset=['release_year'])


# In[28]:


# Remove the "min" text, strip spaces, convert to integer
imdb['runtime_in_minutes'] = imdb['runtime'].str.replace('min', '', regex=False).str.strip()
imdb['runtime_in_minutes'] = pd.to_numeric(imdb['runtime_in_minutes'], errors='coerce').astype('Int64')

# Drop the old runtime column
imdb.drop(columns=['runtime'], inplace=True)


# In[29]:


# Strip whitespace and check unique values to confirm everything is read in correctly 
imdb['genre'] = imdb['genre'].str.strip()
imdb['genre'].value_counts().head(10)


# In[30]:


# Convert rating from string to float for ease of analysis
imdb['rating'] = pd.to_numeric(imdb['rating'], errors='coerce')


# In[31]:


# Convert to numeric values to ensure it is ready for integration and analysis
imdb['metascore'] = pd.to_numeric(imdb['metascore'], errors='coerce')

# Replace 0 with NaN (missing data), it makes it easier to drop these values, as they are missing data points that could skew our data
imdb['metascore'].replace(0, np.nan, inplace=True)


# In[32]:


# Remove "$" and "M", strip spaces, and convert the variables to numeric values 
imdb['gross_in_millions'] = imdb['gross'].str.replace('$', '', regex=False).str.replace('M', '', regex=False).str.strip()
imdb['gross_in_millions'] = pd.to_numeric(imdb['gross_in_millions'], errors='coerce')

# Replace 0s with NaN
imdb['gross_in_millions'].replace(0, np.nan, inplace=True)

# Drop old column name 
imdb.drop(columns=['gross'], inplace=True)


# In[34]:


# Drop rows where critical variables are missing to avoid bias/skews in data
imdb_clean = imdb.dropna(subset=['metascore', 'gross_in_millions'])

# Confirm cleaning results
imdb_clean.info()
imdb_clean.head()


# In[35]:


#Make finalized clean data file and confirm everything is up to par
imdb_clean.to_csv('imdb_cleaned.csv', index=False)
imdb_clean


# In[36]:


#Summary of Python Cleaning
#This notebook implements all data transformations derived from OpenRefine insights:
#Removed formatting inconsistencies from `release_year` and `runtime`
#Verified uniqueness of titles and consistency of director names
#Converted textual numeric columns (`rating`, `metascore`, `gross`) into numeric types for easier analysis
#Replaced zeros with NA for missing numeric data
#Dropped incomplete rows to ensure data accuracy and interpretability
#Analyzed dataset to ensure the objectives above were fulfilled, and to confrim the data is complete and accurate

#By using both OpenRefine and Python, we wereable to provide a transparent, systematic approach.
#OpenRefine was used for rapid exploration and issue detection  
#Python was used for reproducible, programmatic data cleaning 

