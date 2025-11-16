## Status Report (Weeks 1-4 completely done, subject to updates after midterm report feedback)

**Project Overview (from Project Plan):** Our project explores the relationship between movie characteristics such as genre, budget, release year, and their audience ratings and popularity. By integrating and analyzing two large movie datasets from IMDb and TMDB, we aim to identify trends that influence how well a movie performs. Our project will follow a complete data lifecycle, including acquisition, storage, cleaning, integration, analysis, and documentation, while emphasizing ethical handling, reproducibility, and transparency.

**Overview:** This status report aims to give a progress update on all of the tasks that we had detailed in our project plan, giving an updated timeline for the tasks that we have yet to complete, and an explanation of any changes we made to our project plan with the feedback that we were given.

**Task Updates:**

## Week 1 — Dataset Acquisition & Ethical Review - Diya

###  Status: Completed ✅

I acquired both the IMDb Top 1000 and TMDb Movie Metadata datasets from Kaggle and began reviewing their ethical, licensing, and provenance implications. Because both datasets are from Kaggle rather than being official releases, their licensing is not explicitly stated, which raises reproducibility and compliance concerns. The IMDb dataset was scraped by the uploader, Arthur Chong, using Scrapy and is not an officially issued IMDb dataset, and since IMDb’s data is under restrictive terms, this version should be treated as only for academic and personal use and may not permit redistribution. The TMDb dataset was generated using the TMDb API but is not officially certified by TMDb, and although TMDb data is generally available for non-commercial use, the lack of a clear license on Kaggle means redistribution of the modified dataset may also be restricted. To address these concerns, I am documenting the provenance of both datasets, clearly noting that our use is limited to personal and academic purposes, and planning to include attribution and usage constraints in our README.

## Week 2 Data Cleaning (Missing Values, Duplicates, Outliers) - Brianna

### Status: Completed ✅

## Work Completed in Main Folder (data_cleaning):

## Subfolder 1: OpenRefine_History/

### Includes:

IMDB_TMDB_OpenRefine_Analysis.md

IMDB_OpenRefine_History.json

TMDB_OpenRefine_History.json

IMDB_OpenRefine_Semi_Clean.csv

TMDB_OpenRefine_Semi_Clean.csv

### Summary:

OpenRefine was used for exploratory analysis, spotting missing values, duplicates, formatting inconsistencies, and structural issues.

### Critical notes:

No transformations from OpenRefine were final.

The goal was to understand issues and translate that knowledge into reproducible Python code.

The analysis files document the reasoning behind each cleaning decision.

## Subfolder 2: python_cleaning_scripts/

### Includes:

Week_2_Cleaning_IMDB_Data.ipynb

Week_2_Cleaning_TMDB_Data.ipynb

Week_2_Cleaning_IMDB_Data.py

Week_2_Cleaning_TMDB_Data.py

### Summary:

These Python scripts apply all final data cleaning operations in a reproducible way, including:

 - standardizing text formats

 - parsing runtimes and years

 - handling missing values

 - removing duplicates

 - resolving discrepancies found in OpenRefine

 - The notebooks contain explanations and visual output checks.

 - The .py scripts contain the exact logic for automation and workflow reproducibility.

## Subfolder 3: Cleaned_Data/

### Includes:

imdb_cleaned.csv

tmdb_cleaned.csv

These are the fully cleaned datasets derived from the python scripts while utilizing out findings from the OpenRefine exploration, these sets are ready for Week 3 integration.

## Week 3 IMDb & TMDB Integration - Brianna

### Status - Completed 

## Work Completed in Main Folder (data_integration):

### Includes:

IMDB_TMDB_Analysis.md

Week_3_IMDB_TMDB_Integration.ipynb

Week_3_IMDB_TMDB_Integration.py

## Subfolder: integration_output/

### Contains:

merged_movies.csv

merge_log.json

### Summary:

This week involved building the complete integration pipeline. Major steps:

1. Standardizing Columns & Keys

- created title_norm

- normalized release years

- aligned IMDb/TMDB schemas

2. Exact Merge

- Performed on (title_norm, release_year).

3. Fuzzy Matching for Unmatched Titles

- used token_sort_ratio

- applied thresholds to reduce false positives

- matched previously unmatched IMDb/TMDB rows

4. Data Fusion

- Filled missing IMDb fields using TMDB (and vice versa).

- Some missingness remains by design, because:

- IMDb tracks metascore + gross revenue → TMDB does not

- TMDB tracks popularity + vote averages → IMDb does not

5. Conflict Resolution

### Rules included:

- prefer IMDb for original titles

- prefer TMDB for popularity/ratings

- use longest overview text

- infer runtime columns from different naming conventions (runtime_imdb, runtime_in_minutes, etc.)

6. Output Generation

- merged_movies.csv = final dataset

- merge_log.json = transparent report of match counts, fuzzy matches, exact matches, and unmatched rows

- A full conceptual workflow diagram and written explanation exist in IMDB_TMDB_Analysis.md.

## Week 4 Exploratory Data Analysis (Brianna & Diya)

## Status: Completed ✅














## Changes to the Project Plan

1. Added Fuzzy Matching Step

- Originally planned only exact matching.

- Because of title inconsistencies, fuzzy matching became essential.

2. Expanded Cleaning Pipeline

- OpenRefine → Python workflow became more detailed to ensure reproducibility and transparency.

3. Additional Documentation Artifacts

### We added:

- integration workflow diagram

- extended analysis files

- .py versions of notebooks

- merge log reporting

- These were not in the initial plan but significantly strengthen clarity and transparency.

4. Clarified Division of Labor

- More explicit responsibilities for Weeks 5–7.

## Challenges & How We Addressed Them

1. Title Format Inconsistencies

- Resolved through aggressive normalization + fuzzy matching.

2. Schema Mismatch Between IMDb & TMDB

- Some fields exist only in one source.

- Documented this clearly in IMDB_TMDB_Analysis.md.

3. Runtime Column Variation

- IMDb had multiple runtime column names; TMDB had different ones.

- We solved this with inference logic to detect whichever runtime field was present.

4. Persistent Missing Data

- Expected and documented — not an error, but a property of combining two fundamentally different sources.

6. Contribution Statements

## Diya

- Completed all dataset acquisition and ethics review

- Wrote notes on data licensing

- Explored raw datasets in Week 1

- Helped outline Exploration plan for Week 4

- Will lead workflow automation + documentation in Week 6

## Brianna

- Completed all Week 2 data cleaning: OpenRefine exploration, Python scripts, final cleaned CSVs

- Built entire Week 3 integration pipeline

- Wrote IMDB_TMDB_Analysis.md in full

- Created workflow diagrams and integration README

- Generated merged_movies.csv + merge_log.json

- Completed assigned section of Week 4 EDA preparations

- Will complete Week 5 visualizations on time
  
### Both members will collaborate on the final polishing stages.

## Final Summary

We completed Weeks 1–4 exactly on schedule and produced a fully cleaned and integrated movie dataset with transparent documentation at every stage. The project is progressing smoothly, the workflow is reproducible, and we have a clear path for completing analysis, visualization, and reporting before the final deadline.

## Updated Project Timeline

| Week | Task | Responsible | Status / Notes | Deliverable |
|------|------|-------------|----------------|------------|
| 1    | Acquire and explore datasets, review ethical guidelines | Diya | Completed ✅ | Raw data & notes on licensing |
| 2    | Data cleaning (missing values, outliers, duplicates) | Brianna | Completed ✅ | Cleaned datasets (imdb_cleaned.csv, tmdb_cleaned.csv), OpenRefine analysis & history files, Python cleaning scripts & notebooks |
| 3    | Integrate IMDb & TMDB datasets using common keys (titles/IDs) | Brianna | Completed ✅ | Integrated dataset and merge log from Jupyter notebook & Python scripts, as well as an analysis document |
| 4    | Conduct exploratory data analysis | Both | Completed ✅ | Initial graphs & descriptive stats/initial analysis |
| 5    | Create visualizations & interpret findings | Brianna | Planned (to be completed by Sunday, Nov 23) | Visualizations (correlation heatmap, trends) |
| 6    | Automate workflow & finalize documentation | Diya | Planned for first week of December | Reproducible pipeline & README |
| 7    | Submit final GitHub release | Both | Planned Dec 6–9 for final checks, submission Dec 10 | Final project submission |
