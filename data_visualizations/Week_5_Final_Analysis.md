## Week 5 – Final Visualization Analysis (Brianna)

This document summarizes the main findings from the Week 5 visualizations and ties them back to our research questions. All plots were generated from the integrated dataset integration_output/merged_movies.csv and the simplified genre variable genre_simple created in the Week 5 notebook.
Throughout, I focus on what the graphs show, why I built them in this way, and what the patterns might mean, while keeping in mind that our sample is the IMDb Top 1000 (so almost all movies are already highly rated).

## Research Question 1
What factors (genre, budget, runtime, or release year) most strongly influence a movie’s popularity and ratings?

### Genre and Audience Response

## What I did

The original genre columns were messy and often contained combinations like "Action, Crime, Drama" or "Drama, Romance, War".

To avoid having dozens of tiny categories, I created a simplified genre variable genre_simple with broader labels such as Drama, Action, Comedy, Sci-Fi, Thriller, etc.

### Then I did the following:

Drew boxplots of rating_imdb by genre_simple.

Drew boxplots of TMDB popularity by genre_simple.

Calculated genre-level summaries (mean, median, count) for both rating and popularity.

## What the visuals showed:

### Ratings by genre (IMDb):

Most genres have median ratings clustered between about 7.8 and 8.2.

Genres like Drama, Thriller, and Sci-Fi often appear with slightly higher medians and more high-end outliers.

Comedy and Action still perform well (this is a top-1000 list after all), but their distributions are a bit more spread out with more mid-range points.

### Popularity by genre (TMDB):

Popularity is more uneven across genres than ratings.

Action, Sci-Fi, and some other franchise-heavy genres tend to show higher median popularity, even when their IMDb ratings are not the absolute highest.

Drama, although strongly represented in counts and with high ratings, does not always dominate popularity in the same way.

## Interpretation

In this dataset, genre matters more for popularity than for rating:

Ratings are tightly packed because all films are strong performers, but popularity varies more by genre.

Action and Sci-Fi appear good at drawing attention and engagement (high popularity), while Drama and Crime often deliver slightly higher critical appreciation.

This suggests that studios may favor action-oriented or franchise genres when they care about visibility and audience buzz, whereas drama-heavy films may appeal slightly more to critics and dedicated viewers.

### Budget, Revenue, and ROI

## What I did

Budgets and revenues in the dataset range from very small to multi-billion numbers. This produced strong right skew, with a few huge blockbusters.
To make relationships easier to see, I did the following:

Computed log10 transforms of budget_in_millions and revenue_in_millions.

Plotted log(budget) vs log(revenue), colored by simplified genre.

Calculated the correlation between budget and revenue (on the original scale).

Created ROI (return on investment) as revenue_in_millions / budget_in_millions.

### Drew scatter plots of:

IMDb rating vs log(budget)

TMDB popularity vs log(budget)

IMDb rating vs ROI

TMDB popularity vs ROI

### Why logs? Well taking logs does the following:

Compresses extreme values, so huge outliers do not dominate the plot.

Helps reveal patterns that are multiplicative (“doubling the budget often doubles revenue”) as more linear trends.

## What the visuals showed

### Log(Budget) vs Log(Revenue):

Points form a tight upward-sloping cloud, with correlation around 0.77 between budget and revenue.

This suggests a strong, roughly proportional correlation, meaning bigger budgets usually lead to bigger revenues.

The pattern holds across genres, though some outliers appear above or below the main band (exceptionally efficient or inefficient movies).

### IMDb Rating vs Log(Budget):

Points are more scattered, with no strong trend. High and mid-range ratings appear at both low and high budgets.

This indicates that spending more does not guarantee a higher rating.

### TMDB Popularity vs Log(Budget):

Here we see a clearer upward trend. Higher-budget movies tend to have higher popularity scores, especially blockbusters.

This makes sense because bigger films usually receive more marketing, wider releases, and more online engagement.

### IMDb Rating vs ROI:

ROI values span a wide range. Some films earn many times their budget, while others barely break even.

Ratings are spread fairly evenly across ROI, with no obvious pattern that “higher ROI = better rating.”

A modest cluster of well-rated, high-ROI films exists, but it is not dominant.

### TMDB Popularity vs ROI:

Popularity does not increase consistently with ROI.

Some movies that are very profitable are not especially popular on TMDB, and some highly popular films do not have extreme ROI.

## Interpretation

### Budget and revenue:

Our results support the intuitive idea that high-budget films are more likely to earn high revenues, at least among already successful movies.

However, this relationship describes financial scale, not quality.

### Budget and ratings/popularity:

Budget has a weak relationship with rating, meaning audiences can give high ratings to both indie and blockbuster films.

Budget has a stronger relationship with popularity than with rating, suggesting that marketing and exposure play a major role in how often people engage with a film, regardless of its critical quality.

### ROI:

High ROI does not guarantee high ratings or high popularity.

Some small, efficient films quietly earn back many times their budgets without becoming widely known, while some large films are very visible but relatively inefficient financially.

From an industry perspective, this highlights a tradeoff of financial efficiency vs visibility and hype.

### Runtime:

## What I did

I focused on runtime_imdb and:

Plotted runtime vs IMDb rating with points colored by genre.

Plotted runtime vs TMDB popularity.

Calculated correlations between runtime, rating, and popularity.

## What the visuals showed:

Most movies fall into a typical feature range of about 90–150 minutes.

In the runtime vs rating plot, the highest ratings are scattered across this mid-range, with only a light trend listed below:

Very short and very long movies are less common.

The correlation between runtime and rating is small but positive (around 0.29).

In the runtime vs popularity plot, the relationship is even weaker, popularity is spread broadly across runtimes.

## Interpretation

Runtime does not appear to be a strong driver of either rating or popularity in this dataset.

There might be a slight 'sweet spot' in the standard feature length range, but we cannot conclusively say that “longer = better”.

This suggests that other factors (story, cast, marketing, genre) matter more than runtime itself.

### Release Year

## What I did

I computed average IMDb rating and average TMDB popularity per release_year.

I plotted these two time series on the same graph, with release year on the x-axis.

## What the visuals showed:

Average IMDb rating over time stays relatively stable, mostly between about 7.5 and 8.5 out of 10.

Average TMDB popularity over time shows a clear upward trend, especially for films released after about 2000, with spikes for the most recent years.

## Interpretation:

The rating stability suggests that, within the top-1000 set, older and newer films can both be highly rated.

The rise in popularity scores for recent films is likely driven by:

Growth of TMDB as a platform.

Increased streaming and online engagement.

Recency effects (new films are talked about more and receive more marketing).

This means that recency has a stronger effect on popularity than on rating, and any comparison of popularity across decades must be interpreted with caution.

## Research Question 2

How do audience ratings on IMDb compare to TMDB’s popularity scores for the same films?

## What I did

I plotted a scatterplot of IMDb rating vs TMDB popularity with a regression line.

I computed the overall correlation between rating and popularity (~0.29, which is a very mild correlation).

I also calculated correlations within each simplified genre to see if the relationship changes by genre.

## What the visuals showed:

The main scatterplot shows a group of points with a slight upward slope.

Higher IMDb ratings are usually associated with higher TMDB popularity.

However, for any given rating, popularity can range from very low to extremely high.

The correlation tables by genre reveal the following:

Some genres (like Drama and Sci-Fi) show higher rating–popularity correlations, suggesting that in those genres, better-rated films tend to also attract more attention.

Other genres show weaker or inconsistent relationships, likely due to smaller sample sizes or different audience behaviors.

## Interpretation

Ratings and popularity are related but not interchangeable.

Popularity reflects engagement and visibility (how many people interact with or search for a movie).

Ratings reflect perceived quality among those who watched the movie.

### The results suggest that:

Many highly rated movies do become popular, but there are important exceptions.

Some films are critically loved but less popular, as they sitting at high ratings but mid-range popularity.

Others are extremely popular despite only average ratings, especially in highly marketed or franchise-driven genres.

For anyone using TMDB popularity as a substitute for how good a movie is, its vital to note that a popular movie isn’t always a highly rated one, and vice versa.

## Research Question 3

How can an end-to-end, reproducible data pipeline be designed to ethically collect, integrate, clean, and analyze movie datasets from multiple sources of data?
Our third question is less about patterns in the movies and more about how we built the project itself. The visualizations in Week 5 rely on an entire pipeline designed to be transparent and reproducible.

### Ethical Acquisition

We obtained both datasets from Kaggle, not directly from IMDb or TMDB.

Due to this, my teammate and I:

Treated both datasets as usable for academic and personal purposes only.

Documented IMDb and TMDB restrictions on redistribution.

Recorded the sources and links in our project documentation and clearly state data-use limitations in the final report and README.

### Transparent Cleaning

Week 2 cleaning used a two-step strategy:

OpenRefine exploration to find problems: missing values, inconsistent formats, duplicated entries, and strange runtimes/years.

Python scripts (Week_2_Cleaning_IMDB_Data.py, Week_2_Cleaning_TMDB_Data.py) to apply all final cleaning reproducibly.

We deliberately did not rely on manual OpenRefine edits for the final datasets. Instead, I:

Logged observations in IMDB_TMDB_OpenRefine_Analysis.md.

Translated decisions into code so others can see and repeat them.

### Documented Integration

Week 3 integration combined IMDb and TMDB into a single merged_movies.csv using the following:

A normalized key title_norm plus release_year for exact matches.

Fuzzy matching for titles that were similar but not identical, with thresholds tuned to avoid poor matches.

I recorded integration details in:

IMDB_TMDB_Analysis.md.

merge_log.json, which counts exact matches, fuzzy matches, and unmatched rows and documents how many records came from each step.

I kept distinct columns such as runtime_imdb and runtime_tmdb, and I described how conflicts were resolved (which source was trusted for which field).

## Organized Analysis and Reproducible Artifacts

The repository is structured by weeks and tasks:

data_documentation/ for week 1 data provenance.

data_cleaning/ for Week 2 scripts and outputs.

data_integration/ for Week 3 work and the merged dataset.

data_analysis/ for initial exploration.

data_analysis/Week_5_Final_Visualizations/ for final plots and this analysis.

data_workflow/ for week 6 Snakemake model.

For each major step, we provide:

A Jupyter notebook (.ipynb) with narrative comments and figures.

A matching Python script (.py) for users who prefer scripts or want to run the pipeline non-interactively.

Markdown files like this one that explain the reasoning and interpretation in plain language.

### Handling Missing Data Transparently

Some variables (especially budget, revenue, and TMDB-specific fields) have missing values because the two sources track different things.

Instead of silently filling or guessing these values, I did the following:

Quantified missingness in Week 4.

For each analysis in Week 5, filtered to rows that had the necessary fields (only rows with both budget and revenue when computing ROI).

Noted in the documentation that results are based on subsets of the data, and explained why that is reasonable.

This approach avoids introducing artificial data and keeps our conclusions grounded in actual recorded values.

### Environment and Licensing

We followed the course guidance on documenting our computational environment by:

Using a consistent Python environment and noting key libraries (pandas, seaborn, matplotlib) in our project materials.

Planning to include a requirements.txt file so others can recreate the environment.

For our own code and documentation, we plan to use appropriate open licenses (MIT for code, CC-BY for text), while still respecting the more restricted licenses of IMDb and TMDB data.

Overall, this pipeline shows one way to design an end-to-end, transparent, and reproducible data science project that uses real-world, imperfect data while still respecting ethical and licensing constraints.

## Conclusion

Week 5 takes the patterns hinted at in Week 4 and turns them into clear stories:

Genre and budget influence how visible a movie becomes (popularity) more than how it is rated.

Ratings and popularity are linked but represent different aspects of success—quality versus attention.

Runtime and release year play more subtle roles, with runtime having limited impact and recency mostly boosting popularity, not ratings.

Behind all of this is a well-documented pipeline that makes it possible for someone else to understand, rerun, and critique our choices.

Together, the final visualizations and this analysis lay the groundwork for our final project report and for anyone who wants to reuse our methods for a different movie dataset in the future.
