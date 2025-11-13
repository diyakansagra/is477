## OpenRefine: Analyzing the TMDB Data

For this project, I decided to use both Python and OpenRefine to clean the data. OpenRefine provides a clear visual representation of the dataset and allows collapsing rows to efficiently analyze subsets of data, which I specifically used to visualize the data and locate what needs to be changed. This makes it especially useful for quickly identifying potential errors, as it is faster and more efficient than performing these checks solely in Python, where significant code is often required to detect even a single disparity. The actual cleaning and data transformations were carried out in Python scripts, which were derived from the insights gained from OpenRefine.


In this analysis, I focused on the TMDB dataset and systematically examined each column relevant to our project goals, ensuring that all rows are accurately represented and that there are no skews, outliers, or other data concerns. Our project aims to explore the relationship between movie characteristics, such as genre, budget, runtime, release year, and audience ratings and popularity. Therefore, it is essential that these variables are clean, consistent, and interpretable.
 
## Columns Dropped

When opening the file in OpenRefine, I immediately took note of the large number of columns within this dataset, as it was much more extensive than the IMDb dataset. Based on the fact that this dataset had 20 columns, I decided to drop unnecessary columns, as the scope of the project revolves around characteristics such as genre, budget, runtime, release year, and audience ratings and popularity, and cleaning unnecessary columns would not be beneficial. The columns I removed include homepage, id, keywords, original_language, overview, production_companies, production_countries, spoken_languages, status, tagline, and original_title. These columns do not add to the project goals in any way.
 
## Budget

The budget column was read as text rather than numeric. I ensured the values were read as numbers and used OpenRefine transformations to convert the values into millions. I also used the Text Facet to note rows where the budget was zero. These zeros were not placeholders or errors, but rather corresponded to movies that have not been released yet, according to the metadata. These 0 values also correlated to the dropped column of “released”, as if it a movie isn’t released yet, we presumably do not have the budget information readily available. These rows will be removed later in Python to maintain consistency and analytical integrity.
 
## Genre

The genre column was presented in TMDB differently than IMDb, containing IDs, parentheses, and additional syntax. I cleaned this column by removing unnecessary information and organized the genres in alphabetical order, separated by commas to match the IMDb cleaned dataset. I completed this using the transformation function. Using the Text Facet, I found 28 blank rows, which will be dropped later in Python as they are critical to the analysis.
 
## Popularity

The popularity column was initially read as text and was converted to numeric values. There was only one row where popularity was zero. During our analysis, this row contained many missing or incomplete values, indicating it is an outlier. This row, corresponding to the movie “America Is Still the Place,” will be removed during Python cleaning.
 
## Release Date

The release_date column contained the year, month, and day. I renamed this column to release_year and extracted only the year portion using transformations to ensure it was read as a number. This transformation allows for smoother integration with the IMDb dataset.
 
## Revenue

The revenue column was read as text, despite containing full numeric values. I converted the values to numeric format and transformed them to be in millions. I observed 1,427 rows with zero revenue, corresponding to unreleased movies. These rows will be removed in Python to prevent skewing the dataset.
 
## Runtime

The runtime column needed to be read as numeric. I renamed it runtime_in_minutes and flagged rows with zero or blank entries for removal, as these values are implausible and could bias the analysis.
 
## Title

The title column was checked for duplicates using the Text Facet. No duplicates were found. Clustering techniques including Levenshtein distance confirmed that no misspellings existed, ensuring the data’s integrity.
 
## Vote Average

The vote_average column was initially read as text. Conversion to numeric was necessary. Rows with zero values were flagged as implausible and will be removed during Python cleaning.
 
## Vote Count

The vote_count column was also read as text and required conversion to numeric format. Rows with values of ten or less were flagged for removal, as they could compromise the reliability of vote_average scores, as a small sample size is easily biased/skewed, and they are not fully generalizable/representative. 
 
## Next Steps in Python

1.	Change budget to budget_in_millions. Ensure it is read as a number and not a string. Divide each output by 10,000 to ensure it is correctly in millions, and remove any whitespace as a precaution.

2.	Clean genre to reflect the IMDb dataset. Remove unnecessary items such as parentheses and quotes, ensure each genre is separated by a comma, and order them alphabetically. Drop blank rows using dropna().

3.	Convert the popularity column to numeric. Aside from one outlier row with a value of 0.0, the column has no null values. Remove the outlier row as it contains incomplete data.

4.	Change release_date to release_year. Extract only the year from the date (2009-12-10 → 2009) and ensure it is read as a number, not text. The exact date is not needed in this case, and the year will make integration smoother. 

5.	Change the revenue column to revenue_in_millions. Convert to numeric format, divide by one million, and remove rows with zero revenue, as these are outliers.

6.	Rename runtime to runtime_in_minutes. Ensure numeric type and remove rows with zero or blank values, as these are not accurate representations of movie runtime.

7.	Drop zero values in vote_average and ensure numeric type.

8.	In vote_count, remove rows with values of ten or less to ensure data quality, and ensure the column is read as numeric.
