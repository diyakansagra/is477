# Integrating IMDb & TMDB: Exploring Movie Ratings, Popularity, and Reproducible Data Pipelines

## Contributors
•	Brianna Marroquin

•	Diya Kansagra

## Box Link:

https://uofi.box.com/s/uty10bvkkz2qsl6hmhiut9f157g3blfu

## Summary:

This project examines how different movie characteristics relate to audience reception by integrating and analyzing data from two widely used movie information platforms, IMDb and TMDB. The goal is to understand what factors most strongly influence how successful a movie is, while also demonstrating how a transparent and reproducible data pipeline can be built when working with real-world datasets from multiple sources.

Modern data science projects increasingly rely on external datasets that are not designed to work together. These datasets often differ in structure, terminology, coverage, and completeness, which makes even basic analysis challenging. At the same time, reproducibility and ethical considerations are becoming central expectations in both academic and professional settings. This project addresses both of these by combining analysis of movie success metrics with a carefully documented data management workflow.

The analytical motivation for this project comes from common questions people ask about movies. Viewers often wonder whether higher budgets actually lead to better movies, whether popular movies are also well-rated, and whether certain genres systematically perform better than others. By integrating IMDb’s audience ratings with TMDB’s popularity scores, we are able to compare two different perspectives on movie success and explore how they align or diverge.

The project is driven by three research questions. First, what factors such as genre, budget, runtime, and release year most strongly influence a movie’s popularity and ratings? Second, how do IMDb ratings compare to TMDB popularity scores for the same films, and what does any similarity or difference reveal about audience behavior? Third, how can an end-to-end, reproducible data pipeline be designed to ethically collect, clean, integrate, and analyze datasets that originate from different platforms?

To answer these questions, we built a multi-stage workflow that follows the data lifecycle taught in IS477. This included exploratory inspection of raw data, systematic cleaning using reproducible scripts, careful dataset integration using both exact and fuzzy matching techniques, exploratory data analysis, and final visualization and interpretation. At each stage, we emphasized transparency by documenting decisions, preserving intermediate outputs, and maintaining both notebook-based and script-based versions of the analysis.

A major takeaway from the analytical component of the project is that popularity and ratings are related but distinct concepts. Movies with large budgets tend to generate more revenue and attract greater attention, but they do not consistently achieve higher ratings. Genre also plays a meaningful role, with action-driven genres often dominating popularity measures while drama-oriented genres tend to show stronger rating performance. These findings reinforce the idea that visibility, marketing, and audience engagement influence popularity differently than perceived quality.

This project demonstrates how reproducibility can be achieved even when working with imperfect data. Instead of hiding missing values or forcing artificial consistency, we documented gaps, explained why they exist, and used them carefully during analysis. All transformations were implemented in code, every dataset version was saved intentionally, and written explanations accompany each major component of the workflow.

Overall, this project integrates substantive analysis with methodological rigor. It shows how thoughtful data management enables meaningful insights while supporting accountability, transparency, and ethical responsibility in applied data science work.

## Data Profile:

For this project, we used two movie-related datasets sourced from Kaggle: the IMDb Top 1000 Movies dataset and the TMDb Movie Metadata dataset. Although both datasets are widely used for exploratory data analysis, they come with important considerations related to licensing, provenance, and ethical use. Because neither dataset is an official release from its original data provider, it was important to evaluate their origins carefully and clarify the limitations under which they can be used.
The IMDb Top 1000 dataset was uploaded to Kaggle by Arthur Chong, who states that he collected the data by scraping IMDb using Scrapy. This means the dataset is not provided, endorsed, or licensed by IMDb itself. IMDb maintains strict control over its proprietary data, and its published Terms of Service explicitly prohibit redistribution and use of its content outside limited personal or academic contexts. Since the Kaggle version lacks a defined license, such as Creative Commons or another open-data license, the legal assumption is that the original rights remain with IMDb. This creates restrictions on what can be done with the dataset. Any form of redistribution, public hosting, commercial use, or integration into an openly available project would likely violate IMDb’s rights. Even transforming or modifying the dataset and then sharing the resulting version would not be allowed. Because of these constraints, I am treating this dataset as suitable only for strictly academic analysis conducted in a private environment. It is not appropriate to publish the dataset, share code that republishes the data, or claim that the dataset is openly licensed. Additionally, because scraping raises ethical concerns, such as bypassing explicit terms of use, I am making sure to use the dataset only in a way that respects intellectual property rules and avoids redistribution.

The TMDb Movie Metadata dataset raises similar but slightly less restrictive questions. Although TMDb’s data is generally more open and is accessible through its public API, the version available on Kaggle is not an official release by TMDb. Instead, it is a collection generated through the API by a Kaggle user. TMDb’s API terms allow non-commercial use, provided that “Powered by TMDb” is included and users do not imply official endorsement. However, even though TMDb is more permissive than IMDb, the dataset on Kaggle again lacks a clearly stated license. Without an explicit license granting redistribution rights, any dataset posted by a user must be treated as a redistributed copy of the original API data, and that redistribution may or may not align with TMDb’s guidelines. To respect this, I am using the dataset only within the context of this course project and not redistributing it or uploading modified forms elsewhere. I am also including the “Powered by TMDb” statement to acknowledge TMDb as the underlying data provider and clarifying in the documentation that the dataset is unofficial and should not be viewed as formally authorized.

Given these conditions, I have taken several steps to ensure that the use of both datasets remains ethical, transparent, and legally compliant. First, I am documenting the provenance of each dataset clearly, including who uploaded it, how it was obtained, and whether it is an official release. This is an important part of addressing potential reproducibility issues, since unofficial datasets can change, be removed, or vary in quality and completeness. Second, I am explicitly limiting usage to academic purposes. This project is non-commercial and will not involve any form of redistribution or public release of raw data. Third, I am including credit and attribution in my README so that both the Kaggle contributors and the original data providers (IMDb and TMDb) are acknowledged. Finally, I am clarifying the risks and limitations associated with using datasets that lack explicit licensing, especially in contexts that require compliance with intellectual property law or data-sharing policies.

In summary, while the IMDb Top 1000 and TMDb Movie Metadata datasets offer valuable insight and are fitting for exploratory analysis, their unofficial nature requires careful handling. By thoroughly documenting their origin, respecting licensing and usage constraints, and restricting the project to private academic use, I ensure that the project follows responsible data governance practices. This approach maintains transparency, protects intellectual property rights, and aligns with ethical standards for working with externally sourced datasets.


## Data Quality:

Assessing and addressing data quality was a central component of this project, particularly because the two datasets used, IMDb and TMDB, were not originally designed to be integrated or analyzed together. Both datasets are widely used and informative, but they differ substantially in structure, coverage, and purpose. As a result, potential data quality issues arise not only from missing or inconsistent values within each dataset, but also from the challenges involved in aligning two separate sources in a meaningful and transparent way. Rather than attempting to eliminate these issues entirely, the approach throughout this project focused on identifying, documenting, and responsibly managing data quality limitations in a way that supports reproducibility and honest interpretation.

The data quality workflow unfolded in two major phases. The first phase involved exploratory inspection using OpenRefine. This step was intentionally separated from final cleaning to allow for an open-ended review of the raw datasets without immediately committing to irreversible transformations. Within OpenRefine, both datasets were profiled to examine patterns of missing values, inconsistent formatting, duplicate entries, and categorical irregularities. For example, text-based fields such as titles and genres showed inconsistent capitalization, spacing, and punctuation, while numeric fields such as runtime or financial values contained nulls and mixed representations.

OpenRefine was not used to perform final cleaning or correction. Instead, it functioned as an exploratory tool for diagnosing issues and documenting potential risks. The OpenRefine analysis files and history logs provide a transparent record of these observations, including which variables were prioritized for cleaning and which inconsistencies were deemed acceptable limitations of the source data. This distinction ensures that the project avoids “hidden cleaning,” where undocumented decisions could undermine reproducibility.
The second phase of data quality work involved implementing all final cleaning and preprocessing steps using Python. This shift from exploration to execution ensured that every transformation applied to the data could be re-run, audited, and validated. Python scripts and notebooks were used to standardize text fields, parse runtimes into numeric values, extract and normalize release years, remove duplicate records based on explicit criteria, and quantify missingness across variables. Throughout this phase, care was taken to preserve original data semantics rather than overcorrecting or imputing values without justification.

A key principle guiding these decisions was that missing data is not inherently a flaw but a characteristic that must be understood in context. For example, IMDb consistently provides audience ratings and runtime information but often lacks budget and revenue data, particularly for older films. In an opposite manner, TMDB provides popularity metrics and financial information but does not track IMDb-style ratings or metascores. These structural differences mean that missing values persist in the integrated dataset even after cleaning. Rather than filling or discarding the values, the project documents these gaps and approaches them selectively during analysis.

Title and runtime inconsistencies posed some of the most significant data quality challenges. The IMDb dataset included multiple possible runtime representations across columns, while TMDB stored runtime under a single but differently named field. Additionally, movie titles across platforms often differed slightly due to punctuation, alternate phrasing, or formatting conventions. These discrepancies prevented simple one-to-one matching and required deliberate normalization steps. Titles were standardized by lowercasing, trimming whitespace, and removing extraneous formatting, while runtime values were inferred using a priority-based approach that selected the most reliable available field.

Data integration itself became a central component of overall data quality. Although both datasets describe the same domain, there is no shared unique identifier linking IMDb and TMDB entries. This lack of a universal key introduces ambiguity that must be carefully handled to avoid incorrect matches. The integration process began with schema alignment, standardizing column names to clarify provenance and reduce confusion in downstream analysis. Exact matching was then performed using normalized titles and release years, producing a set of high-confidence matches.

However, many valid matches remained unmatched due to minor textual differences. To address this, a fuzzy matching approach was added using conservative similarity thresholds. Fuzzy matching was applied only to records that failed exact matching and was limited to pairs that exceeded a predefined similarity score. This approach reduces the risk of false positives while improving coverage. Every fuzzy match outcome was logged in a merge report that records how many rows were matched exactly, how many were matched fuzzily, and how many remained unmatched.

Once matches were established, a data fusion step combined variables from both sources according to explicitly defined rules. Variables that represent different concepts, such as IMDb ratings and TMDB popularity scores, were preserved separately rather than collapsed into a single measure. When overlapping concepts existed, such as runtime, values were selected based on availability and consistency rather than overwritten. This approach maintains information while minimizing distortion.

The final integrated dataset therefore contains some missing values by design. This missingness reflects the reality of combining two datasets with different scopes and priorities, not a failure of cleaning or integration. During analysis, rows are filtered selectively depending on the research question being addressed. For instance, analyses involving popularity exclude rows without popularity scores, while rating-focused analyses rely on IMDb entries, which provide nearly complete coverage for that variable. This context-aware filtering ensures that conclusions are based on relevant and appropriate subsets of the data.

By documenting all data quality decisions, limitations, and transformations, the project avoids overstating confidence in the results and enables others to evaluate the strength of the conclusions. The emphasis on transparency over forced completeness aligns with best practices in reproducible research. Overall, the data quality component of this project demonstrates that responsible data analysis is not about creating a perfect dataset, but about making imperfections visible, understandable, and manageable so that findings can be interpreted honestly and reused thoughtfully.

## Findings:

The final stage of analysis focused on translating exploratory patterns from Week 4 into clear, well-supported findings that directly address the project’s research questions. Using polished visualizations and carefully selected transformations, the analysis highlights how budget, genre, runtime, and release year relate to popularity and ratings, while clarifying how IMDb ratings and TMDB popularity measure different aspects of audience reception.

One of the clearest findings is the strong positive relationship between movie budget and revenue. When plotted using a logarithmic scale, budget and revenue show a clear upward trend, supported by a high positive correlation observed earlier in the project. The use of logarithmic scaling was necessary because both budget and revenue span several orders of magnitude, and raw plots obscure meaningful differences among lower and mid-budget films. After transformation, the relationship becomes clearer and more interpretable, revealing that while higher-budget movies generally earn higher revenues, the relationship is not perfectly proportional. Several films with very large budgets cluster below expected revenue levels, indicating diminishing returns at the upper end of spending.

Budget also shows a moderately positive relationship with popularity, though this relationship is weaker than the budget–revenue connection. This suggests that higher budgets likely contribute to visibility and audience reach, possibly through marketing and distribution advantages. However, budget shows little to no strong relationship with IMDb ratings. This finding is important because it highlights that financial investment alone does not guarantee higher perceived quality among viewers.

Genre-level analysis further distinguishes popularity from ratings. Simplifying genre categories allowed clearer patterns to emerge. Action, adventure, and science fiction genres consistently show higher popularity levels, even when their median ratings are not the highest. In contrast, drama-oriented genres tend to have higher median IMDb ratings but lower overall popularity. This pattern supports the idea that popularity reflects attention and engagement rather than purely evaluative judgment. Movies that are widely watched or discussed are not always those that audiences rate most favorably.

The comparison between IMDb ratings and TMDB popularity provides additional insight. A scatterplot of rating versus popularity shows a moderate positive relationship, indicating that higher-rated films are often more popular, but the spread is wide. There are many highly rated films with modest popularity and many highly popular films with only average ratings. This reinforces the conclusion that popularity and ratings capture different dimensions of success. Ratings reflect how viewers evaluate a movie after watching it, while popularity reflects how many people engage with it in the first place.

Runtime shows only a mild relationship with ratings and popularity. Most highly rated films fall within a typical feature-length runtime range. Extremely short and extremely long films are less common and do not consistently achieve higher ratings or popularity. This suggests that runtime alone is not a strong driver of success, but rather a contextual factor that interacts with genre and audience expectations.

Release year analysis shows that popularity increases for more recent films, while ratings remain relatively stable across time. This likely reflects changes in platform usage and audience behavior rather than shifts in film quality. Newer films benefit from greater online engagement, marketing infrastructure, and platform growth, which increases popularity metrics without necessarily affecting ratings.

Overall, these findings demonstrate that movie success is multi-dimensional. Financial investment, genre, and recency strongly influence popularity, while ratings are more stable and influenced by narrative and artistic factors. Treating popularity and ratings as distinct but related outcomes allows for a more nuanced understanding of audience behavior.

## Future Work:

This project highlights both the strengths and the natural limitations of working with integrated, real-world datasets, and it opens several meaningful directions for future research and methodological refinement. One of the most important lessons learned is that the value of an analysis depends heavily on how success is defined and measured. Throughout this project, popularity and ratings were treated as distinct but related outcomes, and the results made clear that they capture different dimensions of a movie’s performance. Future work could build on this by explicitly modeling popularity and ratings as separate dependent variables rather than comparing them only descriptively. Doing so would allow clearer differentiation between factors that drive attention and visibility versus those that influence perceived quality or audience evaluation.

A particularly strong avenue for future work lies in deeper genre-based analysis. In this project, genres were simplified into broader categories to improve interpretability and avoid overcrowded visualizations. While effective for high-level comparisons, this simplification inevitably masks finer distinctions across subgenres. Future research could explore more granular genre groupings, like distinguishing between historical drama, crime drama, romance, or psychological thrillers, to identify patterns that are not visible at a higher, general level. This would likely require more advanced text parsing or the incorporation of external genre classification resources, but could uncover more nuanced relationships between genre, audience reception, and financial performance.

Another natural extension of this work would be the inclusion of additional datasets to triangulate findings across multiple platforms. Bringing in sources such as Rotten Tomatoes or Metacritic would allow comparison between critic scores and audience-driven metrics, providing a more comprehensive view of how different communities evaluate films. Integrating additional platforms would also serve as a stress test for the existing integration pipeline, further validating its flexibility and robustness. However, doing so would require careful consideration of licensing, access constraints, and ethical use, reinforcing one of the central lessons of this project: reproducibility and integrity are inseparable from ethical data handling.

From a methodological perspective, future work could move beyond exploratory analysis into more formal statistical modeling, provided assumptions are clearly stated and tested. This project intentionally emphasized descriptive and visual analysis to avoid overstating causal relationships or masking uncertainty. With additional validation, regression models could be introduced to estimate how variables such as budget, runtime, genre, and release year jointly influence popularity or ratings. Similarly, clustering techniques could be used to identify groups of movies with similar profiles, potentially revealing patterns not easily seen through pairwise comparisons. Any modeling would need to be clearly documented and interpreted cautiously to avoid the pitfalls of overfitting or misrepresentation of the data.

Another key lesson from this project concerns missing data. Rather than treating missing values as defects to be eliminated, they were documented and handled contextually, depending on the analysis being performed. Future work could systematically compare how different missing-data strategies affect results. For example, analyses could be run using only complete cases and then repeated using various imputation strategies to assess the missing data sensitivity. This would deepen understanding of how data completeness influences conclusions and further strengthen the transparency of the analytical process.

Workflow automation also represents an important opportunity for growth. While the current project already emphasizes reproducibility through scripts, notebooks, and clear documentation, future iterations could consolidate the entire workflow into a single automated pipeline. Tools such as workflow managers could be used to formalize dependencies between stages, from data acquisition through final visualization. This would further align the project with professional data science practices, where pipelines must be reliable, repeatable, and scalable over time.

Finally, future work could focus on enhancing dissemination and reuse of the project’s outputs. Developing a more comprehensive data dictionary, adopting a formal metadata standard, or packaging results as a reusable research object would make the work more accessible to other researchers. These steps would not only support replicability, but also encourage reuse and extension of the analysis beyond its original scope.

Overall, this project demonstrates that reproducible data analysis is not a fixed endpoint but an iterative process. Each stage revealed new questions, limitations, and opportunities for refinement. The structure, documentation, and analytical decisions developed here provide a strong foundation for deeper inquiry, more advanced modeling, and continued emphasis on ethical, transparent, and reproducible data science practices.

## Reproducing: 

This project was intentionally designed to be reproducible from start to finish using widely available tools, clear folder organization, and extensive documentation. The goal of reproducibility in this context is not only to allow someone else to rerun the code, but also to understand why each step exists, how data flows through the pipeline, and where key decisions were made. The steps below describe how another researcher or reviewer can reproduce the workflow, outputs, and findings presented in this project.

To begin, clone the project repository from GitHub to a local machine. The repository contains all scripts, notebooks, documentation, and directory structures required to run the analysis. It is recommended to use a machine with Python installed, preferably version 3.9 or later, as the analysis relies on common Python data science libraries. Although this is not required, creating and activating a virtual environment is strongly encouraged to isolate dependencies and avoid conflicts with other projects that could be open.

Next, install the required Python dependencies. The scripts and notebooks in this project rely on standard libraries including pandas, numpy, matplotlib, seaborn, and fuzzy string-matching tools (such as rapidfuzz). The necessary packages can be inferred directly from the import statements at the top of the Python scripts and notebooks. This approach ensures flexibility while still providing transparency into the computational environment used.

The raw IMDb and TMDB datasets requires acquiring the original data independently from Kaggle, or a third party resource identified in the Data_Documentation Folder. Detailed instructions are provided in the repository documentation explaining how to obtain the datasets from Kaggle. Users should download the IMDb Top 1000 Movies dataset and the TMDB Movie Metadata dataset from their respective Kaggle pages and place the CSV files into the designated raw data directory specified in the project structure. It is important that file names and paths match those expected by the cleaning scripts to ensure seamless execution.

Once the raw data is in place, the data cleaning stage can be reproduced. Navigate to the data_cleaning directory and run the Python scripts or Jupyter notebooks provided for IMDb and TMDB cleaning. These scripts perform all final, reproducible transformations, including standardizing text fields, parsing runtimes and release years, removing duplicates, and handling missing values where appropriate. The outputs of this stage are the cleaned datasets saved in the Cleaned_Data folder (One should compare both sets to ensure everything looks correct). The OpenRefine analysis documents and history JSON files in the OpenRefine_History folder are included for transparency and context but do not need to be executed to reproduce the pipeline.

After cleaning, the data integration step can be reproduced by running the integration script or notebook located in the data_integration folder. This step applies schema alignment, exact matching on normalized titles and release years, conservative fuzzy matching for unmatched records, and data fusion rules that preserve source-specific variables. Running this stage produces two key outputs in the integration_output folder: merged_movies.csv, which serves as the integrated dataset used for all analysis, and merge_log.json, which documents how rows were matched (exact, fuzzy, or unmatched). These files provide both the data required for analysis and the provenance needed to assess integration quality.

With the integrated dataset generated, exploratory analysis can be reproduced by opening the Week 4 EDA notebook or Python script in the data_analysis/Week_4_EDA_plots folder. Executing this notebook recreates the distribution plots, descriptive statistics, correlation matrices, and preliminary scatterplots used to identify trends, outliers, and relationships. Extensive inline comments explain what is being plotted, why it matters, and how the observed patterns informed later analytical decisions. This step is critical for understanding how the project moved from exploration to focused interpretation.

The final analytical results can be reproduced by running the Week_5_Final_Visualizations notebook or Python script. This stage generates all polished figures used in the final Findings section, including refined scatter plots, genre-based comparisons, log-scaled relationships, and summary visualizations aligned directly with the research questions. The code includes comments explaining visualization choices, such as the use of logarithmic scales to manage skewed distributions, genre simplification to improve interpretability, and selective filtering to handle missing data appropriately.

To reproduce the full project workflow from data acquisition to final analysis, you can use the provided run_all.py script. This script automates all steps in the correct order and ensures that all outputs are generated as intended. After cloning the repository and placing the raw datasets (IMDb Top 1000 Movies and TMDb Movie Metadata) in the designated folders as described in the documentation, you can run run_all.py to automatically clean the raw datasets, integrate them, perform exploratory analysis, and generate the final visualizations. This script replaces the need for a Snakemake workflow, allowing the entire project to be reproduced from start to finish in a straightforward and transparent manner.

In addition to visual outputs, the repository includes a dedicated markdown analysis file for Week 5 that provides full written interpretation of the results. This document explains what each visualization shows, how quantitative relationships should be interpreted, and how the findings relate back to the project’s research questions. Reviewing this file alongside the notebook ensures that another reader can understand not only how the results were generated, but also how conclusions were drawn.

All file paths, inputs, and outputs are explicitly documented within the repository, and each major stage of the workflow is separated into clearly labeled folders. By following the steps in order, from data acquisition to cleaning, integration, exploratory analysis, and final visualization, another researcher can reproduce the full analytical pipeline while respecting data-use constraints and maintaining transparency. The combination of scripts, notebooks, logs, and narrative documentation makes this project reproducible not just in practice, but also in principle, allowing others to audit, adapt, and build upon the work with confidence.

## References:

IMDb Top 1000 Movies Dataset
Chong, A. (2021). IMDb Top 1000 Movies [Dataset]. Kaggle. https://www.kaggle.com/datasets/arthurchongg/imdb-top-1000-movies/data

TMDb Movie Metadata Dataset
The Movie Database (TMDb). (2017). TMDb Movie Metadata [Dataset]. Kaggle. https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Visual Studio Code
Microsoft. (2024). Visual Studio Code (Version 1.xx) [Software]. https://code.visualstudio.com/

Jupyter Notebook
Kluyver, T., Ragan-Kelley, B., Pérez, F., Granger, B. E., & Jupyter Development Team. (2016). Jupyter Notebook [Software]. https://jupyter.org/

## Contribution Statement - Brianna Marroquin:

I served as the primary contributor for data cleaning, data integration, exploratory analysis, final visualization, and analytical interpretation throughout this project. My contributions span Weeks 2 through 5 and include the design and implementation of reproducible workflows, in-depth documentation, and final analytical outputs. A detailed breakdown of my work is provided below.

## Data Cleaning & Quality Assessment (Week 2)

I led the data cleaning efforts for both the IMDb and TMDB datasets, focusing on identifying, documenting, and resolving data quality issues in a reproducible manner.

### Artifacts created and maintained:

### Folder: data_cleaning/

### Subfolder: OpenRefine_History/

IMDB_OpenRefine_Analysis.md

TMDB_OpenRefine_Analysis.md

IMDB_OpenRefine_History.json

TMDB_OpenRefine_History.json

IMDB_OpenRefine_Semi_Clean.csv

TMDB_OpenRefine_Semi_Clean.csv

### Responsibilities and work performed:

Conducted exploratory data profiling in OpenRefine to identify missing values, duplicate records, inconsistent text formatting, and schema irregularities.
Documented all observed data quality issues and reasoning for later cleaning decisions.

Explicitly separated exploratory inspection from final transformations to ensure reproducibility and auditability.

Verified that no irreversible or undocumented transformations were applied at the OpenRefine stage.

### Python-based reproducible cleaning:

### Subfolder: python_cleaning_scripts/

Week_2_Cleaning_IMDB_Data.ipynb

Week_2_Cleaning_TMDB_Data.ipynb

Week_2_Cleaning_IMDB_Data.py

Week_2_Cleaning_TMDB_Data.py

### Responsibilities and work performed:

Implemented all final cleaning steps in Python, including:

Standardizing text fields

Parsing runtimes and release years into consistent numeric formats

Removing duplicates based on defined criteria

Identifying and documenting missing values rather than removing them indiscriminately

Produced reproducible scripts and notebooks with step-by-step comments explaining each transformation and its purpose.

### Final cleaned datasets:

### Subfolder: Cleaned_Data/

imdb_cleaned.csv

tmdb_cleaned.csv

## Data Integration & Fusion (Week 3)

I designed and implemented the full IMDb–TMDB integration pipeline, including schema alignment, matching logic, conflict resolution, and provenance tracking.
Artifacts created and maintained:

### Folder: data_integration/

IMDB_TMDB_Analysis.md

Week_3_IMDB_TMDB_Integration.ipynb

Week_3_IMDB_TMDB_Integration.py

### Responsibilities and work performed:

Standardized schemas between IMDb and TMDB to remove ambiguity between overlapping fields.

Designed and implemented normalized matching keys (title_norm, standardized release_year) to support reliable integration.
Implemented an exact matching pass using normalized titles and release years.

Identified remaining unmatched records and introduced a fuzzy matching approach using token-based similarity thresholds.
Tuned fuzzy matching conservatively to avoid false positives and documented all matching outcomes.

### Data fusion and provenance:

### Subfolder: integration_output/

merged_movies.csv

merge_log.json

### Responsibilities and work performed:

Designed conflict-resolution rules for overlapping fields, including:

Preserving IMDb ratings separately from TMDB popularity scores

Retaining both runtime values (runtime_imdb, runtime_tmdb)

Avoided overwriting values when source disagreement existed.

Generated a merge log documenting exact matches, fuzzy matches, and unmatched rows to support downstream transparency.

Wrote a full conceptual workflow explanation and documentation in IMDB_TMDB_Analysis.md.

## Exploratory Data Analysis (Week 4)

I completed the exploratory data analysis required for Week 4, focusing on identifying patterns, relationships, and data limitations that inform Week 5 analysis.

Artifacts created and maintained:

Folder: data_analysis/Week_4_EDA_plots/

Week_4_Brianna's_EDA.ipynb

Week_4_Brianna's_EDA.py

### Responsibilities and work performed:

Conducted variable distribution analysis for numeric fields (budget, revenue, popularity, ratings, runtimes).

Analyzed categorical distributions for genres and release years.

Computed descriptive statistics and missing value summaries.

Generated correlation matrices and heatmaps to identify candidate relationships.

Created preliminary scatter plots for budget vs revenue, rating vs popularity, and runtime vs rating.

Documented all observations directly in code comments, explicitly noting outliers, skewness, and planning implications for Week 5.

Ensured that notebooks and scripts could be run independently for reproducibility.

## Final Visualizations & Interpretation (Week 5)

I completed the final analysis, visualization design, and interpretive writing aligned with the project’s research questions.

### Artifacts created and maintained:

### Folder: data_analysis/Week_5_Final_Visualizations/

Week_5_Final_Visualizations.ipynb

Week_5_Final_Visualizations.py

Week_5_Final_Analysis.md

### Responsibilities and work performed:

Designed polished visualizations (boxplots, scatter plots, trend plots) focusing on:

Genre vs ratings and popularity

Budget vs revenue with logarithmic scaling

Ratings vs popularity comparisons

Runtime and release-year relationships

Justified methodological choices such as logarithmic transformations for skewed financial variables.

Wrote detailed analytical interpretations linking visuals directly to research questions.

Explicitly connected quantitative results to broader implications about popularity versus quality.

Separated exploratory commentary (Week 4) to interpretive conclusions (Week 5) for clarity and rigor.

Maintained Documentation, Structure, and Reproducibility

### Additional responsibilities:

Created and maintained detailed inline comments across all scripts and notebooks explaining not only what the code does, but why each step was taken.

Helped structure the repository into clear folders separating cleaning, integration, EDA, and final analysis.

Contributed equally to the README.md sections and Mideterm report

Ensured that all analysis artifacts I worked on were provided in both .ipynb and .py formats to maximize accessibility and transparency.

## Contribution Statement - Diya Kansagra:





