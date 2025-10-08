ProjectPlan.md

Overview

Our project explores the relationship between movie characteristics such as genre, budget, release year, and their audience ratings and popularity. By integrating and analyzing two large movie datasets from IMDb and TMDB, we aim to identify trends that influence how well a movie performs. Our project will follow a complete data lifecycle, including acquisition, storage, cleaning, integration, analysis, and documentation, while emphasizing ethical handling, reproducibility, and transparency.

---

Research Questions

1.	What factors (genre, budget, runtime, or release year) most strongly influence a movie’s popularity and ratings?
2.	How do audience ratings on IMDb compare to TMDB’s popularity scores for the same films?
3.	How can an end-to-end, reproducible data pipeline be designed to ethically collect, integrate, clean, and analyze movie datasets from multiple sources of data?

---

Team Members:

•	Brianna Marroquin: Lead on data visualization, cleaning, and analysis.

•	Diya Kansagra: Lead on data collection, documentation, and automation.

---

Roles & Responsibilities:

•	Brianna:

o	Integrate IMDb and TMDB datasets using Python/Pandas.

o	Conduct data cleaning, quality, and reproducibility analysis.

o	Create visualizations and support final report preparation.

•	Diya:

o	Acquire datasets and verify licenses and terms of use.

o	Document metadata, ethical considerations, and privacy/copyright issues.

o	Automate workflow and ensure project meets reproducibility standards.

---

Datasets

1.	IMDb Movies Dataset (via Kaggle)
   
o	Source: https://www.kaggle.com/datasets/arthurchongg/imdb-top-1000-movies

o	Description: Contains information on top 1000 IMDb movies, including title, genre, director, IMDb rating, metascore, gross earnings, and runtime.

o	Format: CSV

o	Access: Direct download from Kaggle (no API needed)

2.	TMDB Movies Dataset (via Kaggle)
   
o	Source: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

o	Description: Includes movie titles, release dates, genres, popularity scores, and budget/revenue data from The Movie Database (TMDB).

o	Format: CSV

o	Access: Direct download or TMDB public API (no key required for CSV)

---

Timeline:

| Week   | Task                                                          | Responsible | Deliverable                                 |
|--------|---------------------------------------------------------------|--------------|---------------------------------------------|
| Week 1 | Acquire and explore datasets, review ethical guidelines       | Diya         | Raw data & notes on licensing               |
| Week 2 | Data cleaning (missing values, outliers, duplicates)          | Brianna      | Cleaned datasets                            |
| Week 3 | Integrate IMDb & TMDB datasets using common keys (titles/IDs) | Brianna      | Integrated dataset                          |
| Week 4 | Conduct exploratory data analysis                        | Both         | Initial graphs & descriptive stats          |
| Week 5 | Create visualizations & interpret findings                    | Brianna      | Visualizations (correlation heatmap, trends)|
| Week 6 | Automate workflow & finalize documentation                    | Diya         | Reproducible pipeline & README              |
| Week 7 | Submit final GitHub release                                   | Both         | Final project submission                    |

---

Constraints:

•	Data Matching: Titles between IMDb and TMDB may not align perfectly (different variable names).

•	Missing Data: Some older movies may lack budget or revenue details.

•	Time: Project limited to the semester timeline, so analysis depth will be scoped accordingly.

---

Gaps:

•	Need to determine the best key for integrating the two datasets.

•	May require manual verification for mismatched entries/variables.

•	Plan to explore additional datasets (like Rotten Tomatoes) to fit into our current datasets.

---

Storage & Organization:

•	Datasets will be stored in CSV format within a structured GitHub folder.

•	Each dataset will correspond to a table within GitHub with clear titles.

•	Metadata files and README documentation will support discovery, understandability, and reproducibility.

---

Data Lifecycle, Cleaning, & Integration:

•	Data will be acquired, cleaned, and integrated using Python/Pandas, and possibly SQL.

•	Cleaning will handle missing values, outliers, and duplicates.

•	Integration will link datasets using a consistent key and verify the accuracy of variables.

•	Enrichment will likely be limited since we want to ensure workflow remains reproducible and ethical.

---

Workflow Automation & Reproducibility:

•	Full end-to-end workflow from acquisition to visualization will be automated.

•	All code and documentation will be controlled via Git/GitHub, which supports transparency and reproducibility.

•	Project documentation will include clear instructions to reproduce analyses and visualizations.

---

Ethical Considerations:

•	Both datasets are publicly available with open data licenses for academic use.

•	No personally identifiable information (PII) will be used.

•	Proper attribution/references to Kaggle, IMDb, and TMDB will be included.

•	Workflow and analysis will be transparent and reproducible to adhere to responsible/ethical data handling.

---

Requirements Checklist:

•	Data lifecycle: Overview and overall Plan describes acquisition, storage, cleaning, integration, analysis, and documentation.

•	Ethical data handling: Licensing, privacy, PII, attribution, and copyright is addressed in multiple sections.

•	Data collection & acquisition: Two distinct datasets (IMDb, TMDB) acquired from different sources/formats.

•	Storage & organization: We mention that we will be using CSV storage, folder structure, metadata, and README.

•	Extraction & enrichment: Python/Pandas will be used. Cleaning, integration, and limited enrichment are described in our Lifecycle portion of the plan.

•	Data integration: In our timeline and gaps, we mention that we will Integrate IMDb and TMDB datasets by using common keys.

•	Data quality: We will be cleaning missing values, outliers, duplicates, and verifying variable accuracy.

•	Data cleaning: Explicit methods mentioned (missing values, outliers, duplicates).

•	Workflow automation & provenance: End-to-end automated workflow described, as well as the reproducible via Git.

•	Reproducibility & transparency: Clear instructions, automated pipeline, and documentation are described in the plan.

•	Metadata & data documentation: We mention that we will be using README and metadata files to support discovery and reuse.
