## OpenRefine_History Folder 

This folder contains the OpenRefine project files documenting the initial exploration and pre-cleaning of the IMDb and TMDB movie datasets. OpenRefine was used to:

Identify inconsistencies, missing values, duplicate entries, and other data quality issues.

Explore disparities in the datasets and plan corrective actions.

Note: No final data transformations were applied in OpenRefine. The actual cleaning and reproducible transformations were implemented later using Python scripts (found in the python_cleaning_scripts folder).

## Purpose of This Folder

This folder provides a transparent view of the data quality challenges encountered during initial exploration. It captures:

How variables were assessed and prioritized for cleaning.

Thought processes and observations during the OpenRefine exploration.

Semi-cleaned output that guided further Python-based cleaning.

It supports transparency and reproducibility in the project workflow.

## Contents:

## Analysis Files

## IMDB_OpenRefine_Analysis.md & TMDB_OpenRefine_Analysis.md

Overview of steps taken to analyze raw IMDb and TMDB datasets in OpenRefine.

Summarizes observed disparities and highlights action items for Python-based cleaning.

Provides a clear view of the decision-making process for cleaning.

## History Files

## IMDB_OpenRefine_History.json & TMDB_OpenRefine_History.json

JSON logs showing the analysis and transformations performed in OpenRefine.

Useful for reviewing experimental cleaning steps.

Refer to the Analysis.md files for a comprehensive interpretation of these actions.

## Semi-Clean CSVs

IMDB_OpenRefine_Semi_Clean.csv & TMDB_OpenRefine_Semi_Clean.csv

Contains intermediate outputs after initial transformations in OpenRefine.

Showcases pre-cleaned data while preserving the integrity of original variables.

Serves as a reference for testing transformations before applying final cleaning in Python.

## How to Use This Folder

Review the analysis files to understand the observed data issues.

Inspect the history JSON files for the exact steps applied in OpenRefine.

Reference the semi-clean CSVs to see preliminary transformations and outputs.

Use the information to understand how Python cleaning scripts were designed for reproducible integration and analysis.
