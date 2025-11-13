#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install recordlinkage rapidfuzz')


# In[18]:


import pandas as pd
import numpy as np
import json
import os
from pathlib import Path

# First I will try to import recordlinkage, if not, it the funtion should fallback to rapidfuzz
USE_RECORDLINKAGE = False
try:
    import recordlinkage as rl
    USE_RECORDLINKAGE = True
except Exception:
    try:
        from rapidfuzz import fuzz, process
    except Exception:
        raise RuntimeError("Please install either 'recordlinkage' or 'rapidfuzz' to run fuzzy linking.")

IMDB_PATH = "imdb_cleaned.csv"
TMDB_PATH = "tmdb_cleaned.csv"

OUTPUT_DIR = "integration_output"
Path(OUTPUT_DIR).mkdir(exist_ok=True)

MERGED_CSV = Path(OUTPUT_DIR) / "merged_movies.csv"
LOG_JSON = Path(OUTPUT_DIR) / "merge_log.json"

# These will be the Mapping rules (which columns to keep & which hold precedence/priority over other columns)
# I will keep all imdb columns, and add tmdb-specific columns that imdb does not have to aid in our project endeavors.
IMDB_KEEP = ["title", "director", "release_year", "genre", "rating", "metascore", "runtime_in_minutes", "gross_in_millions"]
TMDB_KEEP = ["budget_in_millions", "popularity", "revenue_in_millions", "runtime_in_minutes", "vote_average", "vote_count", "genre", "release_year"]

# Precedence rules I will enforce in the python code below:
# If imdb and tmdb both provide a value for a shared column:
# - For ratings: prefer IMDb 'rating' as they are generally used more often, and also preserve TMDB 'vote_average' as separate column
# - For runtime/release_year/genre: if they disagree, keep both columns (runtime_imdb, runtime_tmdb) so downstream analysis can decide (I may also use the average of both for a better representation, during analysis i will revisit this)
# - For budget/revenue/popularity prefer TMDB (IMDb often lacks budget/revenue for older movies, TMDB is more up-to-date)
# - Title matching uses normalized title + release_year. If release_year missing, block less strictly but prefer exact title.

def load_and_preview(imdb_path=IMDB_PATH, tmdb_path=TMDB_PATH):
    imdb = pd.read_csv(imdb_path).convert_dtypes()
    tmdb = pd.read_csv(tmdb_path).convert_dtypes()

    # Remove any duplicate columns, this ensures a clean schema before merging, as I ran into issues when columns were named the same
    imdb = imdb.loc[:, ~imdb.columns.duplicated()]
    tmdb = tmdb.loc[:, ~tmdb.columns.duplicated()]

    return imdb, tmdb

def normalize_columns(imdb, tmdb):
    imdb = imdb.rename(columns=lambda c: c.strip())
    tmdb = tmdb.rename(columns=lambda c: c.strip())

    imdb = imdb.loc[:, ~imdb.columns.duplicated()]
    tmdb = tmdb.loc[:, ~tmdb.columns.duplicated()]

    imdb = make_unique_cols(imdb)
    tmdb = make_unique_cols(tmdb)

    # Standardize column names (relitively simple since my cleaning addressed these)
    imdb = imdb.rename(columns={
        "title": "title",
        "director": "director",
        "release_year": "release_year",
        "genre": "genre",
        "rating": "rating",
        "metascore": "metascore",
        "runtime_in_minutes": "runtime_in_minutes",
        "gross_in_millions": "gross_in_millions"
    })

    tmdb = tmdb.rename(columns={
        "budget_in_millions": "budget_in_millions",
        "popularity": "popularity",
        "revenue_in_millions": "revenue_in_millions",
        "runtime_in_minutes": "runtime_in_minutes",
        "title": "title",
        "vote_average": "vote_average",
        "vote_count": "vote_count",
        "genre": "genre",
        "release_year": "release_year"
    })

    # Normalize types: ensure numeric columns are numeric and ensure years are read in as integers
    for col in ["release_year", "runtime_in_minutes"]:
        if col in imdb.columns:
            imdb[col] = pd.to_numeric(imdb[col], errors="coerce").astype("Int64")
        if col in tmdb.columns:
            tmdb[col] = pd.to_numeric(tmdb[col], errors="coerce").astype("Int64")

    for col in ["rating", "metascore", "gross_in_millions", "budget_in_millions", "popularity", "revenue_in_millions", "vote_average", "vote_count"]:
        if col in imdb.columns:
            imdb[col] = pd.to_numeric(imdb[col], errors="coerce")
        if col in tmdb.columns:
            tmdb[col] = pd.to_numeric(tmdb[col], errors="coerce")

    # Here I Normalize title strings by using strip, lower, and remove extra whitespace
    def norm_title(s):
        if pd.isna(s):
            return ""
        return " ".join(str(s).strip().lower().split())

    imdb["title_norm"] = imdb["title"].apply(norm_title)
    tmdb["title_norm"] = tmdb["title"].apply(norm_title)

    # Now I'll also create genre_norm for matching (lower & strip)
    imdb["genre_norm"] = imdb["genre"].fillna("").astype(str).str.lower().str.strip()
    tmdb["genre_norm"] = tmdb["genre"].fillna("").astype(str).str.lower().str.strip()

    return imdb, tmdb

def exact_merge(imdb, tmdb):
    """
    Exact matching on normalized title + release_year
    Keep all imdb rows (left join), bring tmdb columns.
    Ensures no duplicate columns appear in the merge.
    """
    left = imdb.copy()
    right = tmdb.copy()

    # Columns to bring from TMDB (exclude title, title_norm, genre_norm, release_year to avoid duplicates)
    tmdb_cols_to_add = [
        c for c in right.columns 
        if c not in ["title", "title_norm", "genre_norm", "release_year"]
    ]

    right_for_merge = right[["title_norm", "release_year"] + tmdb_cols_to_add]

    # Merge left (IMDb) with right (TMDB)
    merged_exact = pd.merge(
        left,
        right_for_merge,
        how="left",
        on=["title_norm", "release_year"],
        suffixes=("_imdb", "_tmdb"),
        indicator=True
    )

    return merged_exact

def fuzzy_link_remaining(merged_exact, tmdb):
    """
    For rows where _merge == 'left_only', try to fuzzy match with tmdb candidates
    Block by release_year when possible to reduce false positives.
    Uses recordlinkage if available; otherwise uses rapidfuzz as fallback.
    """

    left_only = merged_exact[merged_exact["_merge"] == "left_only"].copy()
    left_only = left_only.reset_index().rename(columns={"index": "imdb_index"})

    # Candidate TMDB set is all tmdb rows not already used by exact merge matches
    # Now I'll Determine the different tmdb rows that matched in exact merge:
    
    matched_tmdb_rows = merged_exact[merged_exact["_merge"] == "both"]["title_norm"].astype(str).tolist()
    tmdb_candidates = tmdb.copy().reset_index().rename(columns={"index": "tmdb_index"})

    # I'll block by release_year where available and only compare rows with same release_year
    matches = [] 

    if USE_RECORDLINKAGE:
        # Use recordlinkage package for a blocked comparison by year
        indexer = rl.Index()
        indexer.block(left_on="release_year", right_on="release_year")
        # Then I will prepare dataframes with a normalized title
        left_df = left_only.set_index("imdb_index")[["title_norm", "release_year"]]
        right_df = tmdb_candidates.set_index("tmdb_index")[["title_norm", "release_year"]]
        pairs = indexer.index(left_df, right_df)
        compare = rl.Compare()
        compare.string("title_norm", "title_norm", method="levenshtein", threshold=0.80, label="title_sim")
        features = compare.compute(pairs, left_df, right_df)
        # Now I will filter strong matches
        strong = features[features["title_sim"] == 1.0]  # exact by threshold
        for (im_i, tm_i) in strong.index:
            matches.append((im_i, tm_i, 1.0))
        # If none of the matches are exact at the threshold given, you can optionally relax/lower the threshold, this is not implemented here but its something to keep in mind
    else:
        # Use rapidfuzz `fuzz.ratio` for pairwise scoring for the rows with the same year
        from rapidfuzz import fuzz
        # Now I will build the index by year for tmdb candidates
        tmdb_by_year = {}
        for _, r in tmdb_candidates.iterrows():
            yr = r["release_year"]
            tmdb_by_year.setdefault(int(yr) if not pd.isna(yr) else None, []).append(r)

        for _, lm in left_only.iterrows():
            yr = lm["release_year"]
            candidates = tmdb_by_year.get(int(yr) if not pd.isna(yr) else None, [])
            best_score = 0
            best_idx = None
            for cand in candidates:
                score = fuzz.token_sort_ratio(lm["title_norm"], cand["title_norm"]) / 100.0
                if score > best_score:
                    best_score = score
                    best_idx = cand["tmdb_index"]
            # Now I will accept matches with a score of >= 0.90 to ensure optimal accuracy, this can also be altered if needed
            if best_score >= 0.90 and best_idx is not None:
                matches.append((lm["imdb_index"], best_idx, best_score))

    # Now I'll Build the DataFrame of matches
    match_rows = []
    for imdb_idx, tmdb_idx, score in matches:
        match_rows.append({"imdb_index": imdb_idx, "tmdb_index": tmdb_idx, "score": score})
    matches_df = pd.DataFrame(match_rows)

    return matches_df

def apply_matches_and_fuse(merged_exact, matches_df, imdb, tmdb):
    # merged_exact currently contains left imdb rows, and _merge indicator. We'll add fuzzy matches there to ensure there are matches in the data, even if they arent as strong
    result = merged_exact.copy()

    result["_merge"] = result["_merge"].astype(str)

    # Now, I'll prepare the tmdb map by index
    tmdb_map = tmdb.reset_index().rename(columns={"index": "tmdb_index"}).set_index("tmdb_index")

    # For each fuzzy match, the below code will fill missing tmdb columns into the result row by matching the imdb index
    for _, r in matches_df.iterrows():
        imdb_idx = r["imdb_index"]
        tmdb_idx = r["tmdb_index"]
        score = r["score"]

        # Find row in result where original row index == imdb_idx
        mask = result.index == imdb_idx
        if mask.sum() == 0:
            continue

        # For columns coming from tmdb, I will fill in a variable when merged_exact has NaN/Na for the column
        for col in tmdb.columns:
            if col in ["title", "title_norm", "genre", "genre_norm"]:
                continue
            tm_col = col
            target_col = tm_col if tm_col in result.columns else tm_col + "_tmdb"
            val = tmdb_map.loc[tmdb_idx].get(tm_col)
            if target_col in result.columns:
                if pd.isna(result.loc[imdb_idx, target_col]):
                    result.loc[imdb_idx, target_col] = val
            else:
                result.loc[imdb_idx, target_col] = val

        result.loc[imdb_idx, "_merge"] = "fuzzy"

    # Now we can standardize ou output column set and resolve any conflicts that arise
    # I'll create final columns with clear names to avoid any confusion:
    # Title, release_year, director (from imdb), genre_imdb, genre_tmdb, rating_imdb, vote_average_tmdb, budget_in_millions, revenue_in_millions, popularity, vote_count, runtime_imdb, runtime_tmdb, metascore, gross_in_millions
    final = pd.DataFrame()
    final["title"] = result["title"]
    final["release_year"] = result["release_year"]

    final["director"] = result.get("director", pd.Series(index=result.index, dtype="string"))
    final["genre_imdb"] = result.get("genre", pd.Series(index=result.index, dtype="string"))
    final["genre_tmdb"] = result.get("genre_tmdb", result.get("genre_tmdb", pd.Series(index=result.index, dtype="string")))

    final["rating_imdb"] = result.get("rating", pd.Series(index=result.index, dtype="float"))
    final["vote_average_tmdb"] = result.get("vote_average", result.get("vote_average_tmdb", pd.Series(index=result.index, dtype="float")))
    final["vote_count_tmdb"] = result.get("vote_count", result.get("vote_count_tmdb", pd.Series(index=result.index, dtype="Int64")))

    # Final numbers
    final["gross_in_millions"] = result.get("gross_in_millions", pd.Series(index=result.index, dtype="float"))
    final["budget_in_millions"] = result.get("budget_in_millions", pd.Series(index=result.index, dtype="float"))
    final["revenue_in_millions"] = result.get("revenue_in_millions", pd.Series(index=result.index, dtype="float"))
    final["popularity"] = result.get("popularity", pd.Series(index=result.index, dtype="float"))

    # Final runtimes
    final["runtime_imdb"] = result.get("runtime_in_minutes", pd.Series(index=result.index, dtype="Int64"))
    final["runtime_tmdb"] = result.get("runtime_in_minutes_tmdb", result.get("runtime_in_minutes_tmdb", pd.Series(index=result.index, dtype="Int64")))

    # Final metascore
    final["metascore"] = result.get("metascore", pd.Series(index=result.index, dtype="float"))

    # Final provenance
    final["_merge_status"] = result["_merge"]

    # Here, I reposition columns for readability and also clarity 
    cols = [
        "title", "release_year", "director",
        "genre_imdb", "genre_tmdb",
        "rating_imdb", "vote_average_tmdb", "vote_count_tmdb",
        "budget_in_millions", "revenue_in_millions", "gross_in_millions", "popularity",
        "runtime_imdb", "runtime_tmdb",
        "metascore", "_merge_status"
    ]
    final = final[cols]

    return final
    
def make_unique_cols(df):
    """
    Ensure all column names in the DataFrame are unique by appending _1, _2, etc. 
    to duplicates (after the first occurrence).
    """
    cols = pd.Series(df.columns)
    for dup in cols[cols.duplicated()].unique():
        dup_idx = cols[cols == dup].index.values
        cols[dup_idx[1:]] = [f"{dup}_{i}" for i in range(1, len(dup_idx))]
    df.columns = cols
    return df

def main():
    imdb, tmdb = load_and_preview()
    imdb = make_unique_cols(imdb)
    tmdb = make_unique_cols(tmdb)
    imdb, tmdb = normalize_columns(imdb, tmdb)

    # Here are some Basic schema prints for our discretion and documentation of the project
    print("IMDB columns:", imdb.columns.tolist())
    print("TMDB columns:", tmdb.columns.tolist())

    imdb = imdb.loc[:, ~imdb.columns.duplicated()]
    tmdb = tmdb.loc[:, ~tmdb.columns.duplicated()]
    
    merged_exact = exact_merge(imdb, tmdb)

    counts = {
        "imdb_total_rows": len(imdb),
        "tmdb_total_rows": len(tmdb),
        "exact_match_count": int((merged_exact["_merge"] == "both").sum()),
        "left_only_before_fuzzy": int((merged_exact["_merge"] == "left_only").sum())
    }

    # Now I will run fuzzy linkage to match remaining left_only rows
    matches_df = fuzzy_link_remaining(merged_exact, tmdb)

    counts["fuzzy_match_count"] = int(len(matches_df))

    merged_final = apply_matches_and_fuse(merged_exact, matches_df, imdb, tmdb)

    # Finally, I will save the results to use for analysis
    merged_final.to_csv(MERGED_CSV, index=False)

    counts["final_merged_rows"] = len(merged_final)
    counts["exact_matches_saved"] = int((merged_final["_merge_status"] == "both").sum())
    counts["fuzzy_matches_saved"] = int((merged_final["_merge_status"] == "fuzzy").sum())
    counts["unmatched_imdb_saved"] = int((merged_final["_merge_status"] == "left_only").sum())

    with open(LOG_JSON, "w") as f:
        json.dump(counts, f, indent=2)

    print("Integration done. Outputs:")
    print(" -", MERGED_CSV)
    print(" -", LOG_JSON)
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()

