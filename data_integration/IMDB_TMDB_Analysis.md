## Data Integration Documentation: IMDb + TMDB

## Overview

The goal of this integration is to create a unified movie dataset by combining data from IMDb and TMDB. The final dataset will provide a comprehensive view of each movie, including information like:

•	Title, release year, director, and genre.

•	Ratings and votes (IMDb rating and TMDB vote_average).

•	Runtime and financial metrics (budget, revenue, gross, popularity).

•	Provenance information to indicate how each record was merged.

This unified dataset allows for consistent analysis of movies and allows us to properly address our research questions while combining the strengths of both sources while handling missing or conflicting data.
 
## Data Sources:

### IMDb:

Contains columns such as title, director, release_year, genre, rating, metascore, runtime_in_minutes, and gross_in_millions.

Offers reliable ratings and data, but often lacks budget and revenue information for older movies.

### TMDB:

Contains title, budget_in_millions, popularity, revenue_in_millions, runtime_in_minutes, vote_average, vote_count, genre, and release_year.

TMDB provides more up-to-date financial information but ratings are less standardized.

### Key differences:

IMDb has more trusted ratings and complete director information.

TMDB has financial and popularity data missing from IMDb.
 
## Integration Strategy (Schema Mapping & Column Precedence):

### Shared columns:

Ratings: Use IMDb rating as primary, keep TMDB vote_average separately so theres no confusion.

Runtime, release year, genre: Keep both IMDb and TMDB values as separate columns (runtime_imdb, runtime_tmdb, etc.) to allow downstream analysis.

TMDB-specific columns: Budget, revenue, and popularity. Prefer TMDB values because IMDb is often missing them.

Title matching: Normalize titles (strip whitespace, lowercase, remove extra spaces). Exact match on title_norm + release_year (Some titles have the same name, so adding release_year will ensure it’s the same movie).

### Data Normalization:

Strip column names and remove duplicates.

Ensure numeric columns are numeric (with appropriate Int64 or float types).

### Normalize strings:

title_norm: lowercase, stripped, whitespace-normalized.

genre_norm: lowercase, stripped.

## Merging Methods used

### Step 1: Exact Merge

•	Merge IMDb and TMDB datasets on title_norm and release_year using a left join.

•	Add _merge indicator:

•	both → matched in TMDB exactly.

•	left_only → unmatched in TMDB.

### Step 2: Fuzzy Matching

•	For rows with _merge == left_only, I attempted to match using fuzzy string comparison.

#### Tools used:

•	recordlinkage with Levenshtein distance (threshold = 0.8) to ensure wanted linkage rate (0.8 is a safe standard)

•	Otherwise fallback to rapidfuzz with token_sort_ratio (threshold = 0.9).

•	Blocking by release_year reduces false positives.

•	Fuzzy matches update _merge to "fuzzy".

### Step 3: Data Fusion

•	For matched rows (fuzzy or exact), fill in missing TMDB columns in the merged dataset.

•	Skip shared string columns like title and genre (keep IMDb and TMDB separately to avoid discrepancies).

•	Resolve any conflicts or inconsistencies in numeric or categorical fields where both sources provide values (Many errors arose from having the same column titles, I had to fix this in the code by trial and error a few times).

• IMDb columns remain untouched because IMDb is treated as the primary source. TMDB only fills missing numerical/financial fields.

•	Create final columns with clear provenance: runtime_imdb, runtime_tmdb, genre_imdb, genre_tmdb, etc.

•	_merge_status column preserves provenance: "both", "fuzzy", "left_only".
 
## Conceptual Model / Integration Schema

### Overview of the mapping done in the Integration:

| Final Column        | Source(s)   | Notes                                  |
|--------------------|------------|----------------------------------------|
| title              | IMDb       | Normalized string                       |
| release_year       | IMDb/TMDB  | Both provide values; conflicts resolved by preference for exact match |
| director           | IMDb       | Preserved from IMDb                     |
| genre_imdb         | IMDb       | Original IMDb genre                     |
| genre_tmdb         | TMDB       | Original TMDB genre                     |
| rating_imdb        | IMDb       | Main rating for analysis                |
| vote_average_tmdb  | TMDB       | Separate column for comparison          |
| vote_count_tmdb    | TMDB       | TMDB votes                              |
| budget_in_millions | TMDB       | Preferred over IMDb                     |
| revenue_in_millions| TMDB       | Preferred over IMDb                     |
| gross_in_millions  | IMDb       | Preserved                               |
| popularity         | TMDB       | Added from TMDB                         |
| runtime_imdb       | IMDb       | Preserved                               |
| runtime_tmdb       | TMDB       | Preserved                               |
| metascore          | IMDb       | Preserved                               |
| _merge_status      | Both       | Provenance: exact/fuzzy/unmatched      |

##  Workflow Diagram (Conceptual thoughts written out in diagram form followed by a short summary for transparency):


          Load CSVs → Normalize Columns → Exact Merge (title_norm + release_year)
                     
                     ↓
            
            Unmatched Rows → Fuzzy Match → Fill Missing TMDB Columns
                   
                     ↓
        
         Resolve Conflicts → Generate Final Dataset → Save CSV + Merge Log
### Workflow Summary:

First I loaded the IMDb and TMDB datasets and cleaned up the column names and data types. Next, I performed an exact merge using normalized movie titles and release years to match records that line up perfectly. Any IMDb rows that don’t find a match go through a fuzzy matching step to find the closest TMDB record based on title similarity. For these matches, I fill missing TMDB values using the matched TMDB row. IMDb values are used directly and never overwritten. Finally, I resolved conflicts (like differences in runtimes or genres), created clear final columns, and saved the merged dataset along with a log summarizing the merging results.

## Integration Steps

### Load and clean data:

Read CSVs with pandas.

Remove duplicate columns, normalize column names. Refer to OpenRefine to visualize any inconsistencies.

### Normalize fields:

Numeric types for financials, ratings, runtimes.

String normalization for titles and genres.

### Exact merge:

Left join IMDb to TMDB on title_norm + release_year.

_merge indicator added.

### Fuzzy matching for remaining rows:

Block by release_year to reduce false positives.

Use recordlinkage or rapidfuzz to score title similarity.

Update _merge to "fuzzy" for successful matches.

### Data fusion:

Fill missing TMDB values in merged dataset by taking values from the matched TMDB rows for fields that are empty (NaN) in the merged dataset after the exact merge. 

This ensures each movie has as much data as possible, while still preserving the source of the data.

Keep both IMDb and TMDB values for conflicting fields.

Create final standardized columns.

### Output:

merged_movies.csv → final unified dataset.

merge_log.json → summary counts of exact, fuzzy, and unmatched rows.
 
## Outputs and Deliverables

### Merged CSV (merged_movies.csv)

Contains complete information for each movie with clear provenance (_merge_status).

### JSON Log (merge_log.json)

Tracks counts of:

Total IMDb and TMBD rows

Exact matches

Fuzzy matches

Unmatched IMDb rows

Final merged row count 


