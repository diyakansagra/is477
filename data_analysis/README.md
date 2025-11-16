## Week 4 (Initial Graphs & Exploratory Analysis)

This folder contains all initial Exploratory Data Analysis (EDA) done with our integration set. We revisit our researach questions and conduct analysis to draw tangible conclusions from the dataset.

## Goal:

Understand distributions, correlations, and relationships in the integrated dataset. Identify any trends, anomalies, or insights that can guide Week 5’s visualizations and interpretations.

## Dataset used:

data_integration/integration_output/merged_movies.csv (integrated IMDb + TMDB dataset)

## Tasks for Brianna

### Variable Analysis

- Plot distributions of numeric variables: budget_in_millions, revenue_in_millions, popularity, rating_imdb, vote_average_tmdb, runtime_imdb, runtime_tmdb.

- Plot categorical variables: genre_imdb, genre_tmdb, release_year (histogram or bar charts).

- Compute basic descriptive statistics: mean, median, standard deviation, min/max, and missing values per column.

### Correlation Analysis

- Compute correlations among numeric variables (budget, revenue, ratings, popularity) 

- Create a correlation heatmap for numeric columns to identify potential interesting relationships.

### Preliminary Scatter Plots

- Budget vs revenue

- Rating vs popularity

- Runtime vs rating

- Color-code by genre to identify patterns (can be rough/initial plots, polished plots will come in Week 5).
Document observations

- Take notes on interesting trends, outliers, or unexpected results. These notes will feed into Week 5 interpretation.

## Tasks for Diya

### Categorical Comparisons

- Explore relationships between genres and ratings/popularity.

- Create pivot tables or grouped summaries (e.g., average IMDb rating by genre, average popularity by genre, counts of movies per genre per decade).

### Temporal Trends

Analyze trends over time:

- Ratings vs release year

- Popularity vs release year

- Budget and revenue over time

- Identify decades or years with unusual spikes or drops in ratings/popularity.

### Missing Data & Quality Checks

- Check for missing or inconsistent values that may have been introduced during integration.

- Document which variables still have blanks and whether Week 5 visualizations will require handling missing data.

### EDA Summary Document

Start drafting a Week 4 EDA summary Markdown file (Week_4_EDA.md) describing:

- Which columns were analyzed

- Key observations from distributions, correlations, and trends

- Initial ideas for Week 5 visualizations

### Important Note: Week 5 will be for final polished visualizations and interpretation. Week 4 is about exploration and insight generation.

## Deliverables for Week 4

- Week_4_EDA.md – Markdown summary of exploratory analysis

- Plots folder with preliminary figures (Week_4_EDA/plots/)

- Tables folder with grouped summaries and pivot tables (Week_4_EDA/tables/)
