#!/usr/bin/env python
# coding: utf-8

# In[91]:


# Week 2: Cleaning TMDb Dataset (Handling Missing Values, Outliers, and Duplicates)

# This notebook contains all Python-based cleaning steps derived from insights gathered during the OpenRefine exploration.
# Please review the OpenRefine documentation beforehand, as it thoroughly explains the visual findings that guide our cleaning process.
# OpenRefine was used to visually identify inconsistencies, formatting issues, and potential data discrepancies.
# Python is used here to carry out precise and reproducible data cleaning for the TMDb dataset.
# A separate notebook contains the IMDB data cleaning process, the two datasets were divided for clarity and ease of visibility.


# In[92]:


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


# In[93]:


#confirm raw dataset is read in properly

tmdb = pd.read_csv('tmdb_5000_movies.csv')


# In[94]:


tmdb.head()


# In[95]:


# Check data types, missing values, and overall info
tmdb.info()


# In[96]:


# Look for duplicate rows (just to confirm none slipped in)
tmdb.duplicated().sum()


# In[97]:


# Drop columns that are not relevant to the project goals
cols_to_drop = [
    'homepage', 'id', 'keywords', 'original_language', 'overview', 
    'production_companies', 'production_countries', 'spoken_languages', 
    'status', 'tagline', 'original_title'
]
tmdb.drop(columns=cols_to_drop, inplace=True)


# In[98]:


# Confirm column removal
tmdb.head()


# In[99]:


# Ensure 'budget' is numeric and convert to millions to match IMDb
tmdb['budget'] = pd.to_numeric(tmdb['budget'], errors='coerce') / 1000000
tmdb.rename(columns={'budget': 'budget_in_millions'}, inplace=True)


# In[100]:


# Drop rows with zero budget (unreleased movies)
tmdb = tmdb[tmdb['budget_in_millions'] > 0]


# In[101]:


# Confirm 'budget'

tmdb.head(10)


# In[102]:


# TMDB genres column is complex JSON-like string that is quite confusing. Here I am extracting just the genre names, alphabetizing them, and separating them by commas to match the IMDB data set

def parse_genres(genre_str):
    if pd.isna(genre_str) or genre_str == '[]':
        return np.nan
    try:
        genre_list = [d['name'] for d in ast.literal_eval(genre_str)]
        genre_list.sort()
        return ', '.join(genre_list)
    except:
        return np.nan

# I will apply parsing function to get rid of unecessary characters
tmdb['genre'] = tmdb['genres'].apply(parse_genres)

# Drop the original 'genres' column
tmdb.drop(columns=['genres'], inplace=True)

# Drop rows where genre is missing to avoid discrepencies in our future analysis
tmdb = tmdb.dropna(subset=['genre'])

# Confirm the result
tmdb[['genre']].head()


# In[103]:


#Convert popularity to be read as a number, not a string
tmdb['popularity'] = pd.to_numeric(tmdb['popularity'], errors='coerce')

# Drop outliers / missing values
tmdb = tmdb[tmdb['popularity'] > 0]


# In[104]:


# Extract year from 'release_date' and convert to integer
tmdb['release_date'] = pd.to_datetime(tmdb['release_date'], errors='coerce')
tmdb['release_year'] = tmdb['release_date'].dt.year.astype('Int64')

# Drop rows where release_year is missing
tmdb = tmdb.dropna(subset=['release_year'])

# Drop the original release_date column
tmdb.drop(columns=['release_date'], inplace=True)


# In[105]:


# Convert revenue to millions, drop zeros
tmdb['revenue'] = pd.to_numeric(tmdb['revenue'], errors='coerce') / 1000000
tmdb.rename(columns={'revenue': 'revenue_in_millions'}, inplace=True)
tmdb = tmdb[tmdb['revenue_in_millions'] > 0]


# In[106]:


# Ensure runtime is numeric, drop zero or missing runtimes
tmdb['runtime'] = pd.to_numeric(tmdb['runtime'], errors='coerce')
tmdb.rename(columns={'runtime': 'runtime_in_minutes'}, inplace=True)
tmdb = tmdb[tmdb['runtime_in_minutes'] > 0]


# In[112]:


# Ensure titles are unique
tmdb.duplicated(subset='title').sum()
# Two titles were the same, so I confirmed that they are indeed different, no further action is needed, as they are unique.
tmdb[tmdb.duplicated(subset='title', keep=False)].sort_values('title')


# In[108]:


#Verify Vote Average is read correctly

tmdb['vote_average'] = pd.to_numeric(tmdb['vote_average'], errors='coerce')
tmdb = tmdb[tmdb['vote_average'] > 0]


# In[109]:


# Confirm the count is read as a number, not a string
tmdb['vote_count'] = pd.to_numeric(tmdb['vote_count'], errors='coerce')
tmdb = tmdb[tmdb['vote_count'] > 10]  # Drop low-sample movies to avoid skew in later analysis


# In[110]:


#Confirm everything looks correct
tmdb.info()
tmdb.head()


# In[113]:


tmdb.to_csv('tmdb_cleaned.csv', index=False)


# In[ ]:




