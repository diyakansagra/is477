## Status Report (Weeks 1-4 completely done, subject to updates after midterm report feedback)

**Project Overview (from Project Plan):** Our project explores the relationship between movie characteristics such as genre, budget, release year, and their audience ratings and popularity. By integrating and analyzing two large movie datasets from IMDb and TMDB, we aim to identify trends that influence how well a movie performs. Our project will follow a complete data lifecycle, including acquisition, storage, cleaning, integration, analysis, and documentation, while emphasizing ethical handling, reproducibility, and transparency.

**Overview:** This status report aims to give a progress update on all of the tasks that we had detailed in our project plan, giving an updated timeline for the tasks that we have yet to complete, and an explanation of any changes we made to our project plan with the feedback that we were given.

**Task Updates:**

## Week 1 — Dataset Acquisition & Ethical Review - Diya

###  Status: Completed

I acquired both the IMDb Top 1000 and TMDb Movie Metadata datasets from Kaggle and began reviewing their ethical, licensing, and provenance implications. Because both datasets are from Kaggle rather than being official releases, their licensing is not explicitly stated, which raises reproducibility and compliance concerns. The IMDb dataset was scraped by the uploader, Arthur Chong, using Scrapy and is not an officially issued IMDb dataset, and since IMDb’s data is under restrictive terms, this version should be treated as only for academic and personal use and may not permit redistribution. The TMDb dataset was generated using the TMDb API but is not officially certified by TMDb, and although TMDb data is generally available for non-commercial use, the lack of a clear license on Kaggle means redistribution of the modified dataset may also be restricted. To address these concerns, I am documenting the provenance of both datasets, clearly noting that our use is limited to personal and academic purposes, and planning to include attribution and usage constraints in our README.

## Week 2 Data Cleaning (Missing Values, Duplicates, Outliers) - Brianna

### Status: Completed 

### Work Referenced:

/integration/Week_2_DataCleaning.ipynb

/integration/Week_2_DataCleaning.py

/integration/cleaned/imdb_cleaned.csv

/integration/cleaned/tmdb_cleaned.csv

### Summary of Progress:

This stage focused on preparing both datasets for integration by addressing:

Inconsistent column names

Title formatting differences

Missing release years

Duplicate entries

Outliers in runtime, financial metrics, and vote counts

Normalization steps such as replacing special characters, converting titles to lowercase, and standardizing runtime and date formats were implemented. 

All cleaning steps are fully documented in the notebook and exported to a reproducible .py script for transparency.

The cleaned datasets produced here became the inputs for Week 3’s integration pipeline.
