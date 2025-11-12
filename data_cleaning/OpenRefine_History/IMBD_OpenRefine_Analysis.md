## OpenRefine: Analyzing the IMDb Data

For this project, I decided to use both Python and OpenRefine to clean the data. OpenRefine provides a clear visual representation of the dataset and allows collapsing rows to efficiently analyze subsets of data, which I specifically used to visualize the data and locate what needs to be changed. This makes it especially useful for quickly identifying potential errors, as it is faster and more efficient than performing these checks solely in Python, where significant code is often required to detect even a single disparity. The actual cleaning and data transformations were carried out in Python scripts, which was derived by the insights gained from OpenRefine.


In this analysis, I focused on the IMDb dataset and systematically examined each column relevant to our project goals, ensuring that all rows are accurately represented and that there are no skews, outliers, or other data concerns. Our project aims to explore the relationship between movie characteristics, such as genre, budget, runtime, release year, and audience ratings and popularity. Therefore, it is essential that these variables are clean, consistent, and interpretable.


## Duplicates and Titles

Upon opening the dataset in OpenRefine, I first wanted to ensure that each movie was uniquely represented. Using the Text Facet function, I identified six movies that appeared twice:

•	All Quiet on the Western Front

•	Beauty and the Beast

•	Drishyam

•	Drishyam 2

•	Scarface

•	A Girl with the Dragon Tattoo

At first, this was concerning as potential duplicates could skew analyses. After further inspection and verification via Google, I confirmed that these were either remakes or distinct movies with the same name but different release years and directors, indicating they were not true duplicates.

## Directors

Next, I examined the Director column for misspellings that could affect analysis. I expected multiple entries per director due to multiple movies. Using Text Facet and the Clustering feature with different methods, including the Levenshtein distance/closest neighbor and key collision, no misspellings or unusual clusters were found. This confirmed the director data is consistent.

## Release Year

The Release Year column initially presented disparities. Using the Number Facet produced no results because the column was read as a string due to parentheses surrounding each year. Further inspection with a Text Facet revealed additional inconsistencies, such as (I), (II), or (III) appended to certain years. I used OpenRefine transformations to remove these characters and parentheses and ensured the values could be interpreted as integers. This pre-cleaning step gives a clear roadmap for the Python cleaning workflow.

## Runtime

The Runtime column had a similar issue. It was read as a string because of the "min" text following each number. Using Text Facet, I verified this disparity and applied transformations to remove the text, convert values to integers, and rename the column to runtime_in_minutes. This ensures consistency and clarity for later analysis, and gives me clear steps as to what I need to do in Python.

## Genre

The Genre column was straightforward to inspect. Using Text Facet and Clustering, I confirmed consistent formatting and found no misspellings or transposed entries. Similar or multi-word genres were correctly recognized as distinct by OpenRefine.

## Ratings

The Rating column was initially read as text due to the presence of decimals. I used transformations to ensure this column could be read as a numeric type without any issues, and it gave me a clear roadmap as to how to approach the cleaning in Python, as I would need to change the variable type (float or int64) to allow proper quantitative analysis.

## Metascore

The Metascore represents the critics consensus on a movie, scored from 0–100, with higher values indicating more positive reviews. This column was also read as text and required conversion to an integer. Metadata indicated that missing values were represented as 0, and these should be treated as NA in Python to avoid skewing the analysis. This provided clear steps and ample time to plan for marking 0’s as NA and applying the dropna() function in python.

## Gross

The Gross column contained dollar signs and the letter "M" for millions, causing it to be read as text. I removed these characters, renamed the column to gross_in_millions, and ensured numeric formatting by using transformations to ensure that it can be done without affecting other columns. Similar to the metascore, zero values indicate missing data and will be dropped in Python.
 
## Summary of OpenRefine Findings

Using OpenRefine, I visually inspected the IMDb dataset and identified key areas needing cleaning. The main operations used were facets (text and number), transformations, and clustering. This exploration allowed me to do the following:

•	Identify duplicates and verify that repeated titles were valid

•	Ensure director names are consistent with no misspellings

•	Recognize disparities in release year formatting

•	Confirm runtime and rating values are properly formatted for numerical analysis

•	Validate genre consistency

•	Mark missing or null values for metascore and gross

I will utilize this analysis as a pre-cleaning step, giving a clear guide for systematic cleaning in Python to ensure accuracy and reproducibility.
 
## My Next Action Items for Python Cleaning

1.	Year: Remove parentheses, whitespace, and (I), (II), (III) annotations; convert to integer.

2.	Runtime: Rename to runtime_in_minutes, remove "min", strip whitespace, and convert to integer.

3.	Rating: Convert from text to numeric type (int64 or float).

4.	Metascore: Replace 0 values with NA and convert to integer; drop missing values.

5.	Gross: Remove $ and M, convert to numeric, rename column to gross_in_millions, and drop zeros as missing data.

6.	Overall: Verify that the data is clean (explore potential discrepancies such as whitespaces)

My combined approach of OpenRefine for exploration and Python for actual cleaning provides a robust, transparent, and reproducible workflow.
