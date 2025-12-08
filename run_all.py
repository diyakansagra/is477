#!/usr/bin/env python3
"""
run_all.py

Automates the full workflow for the project:
1. Data cleaning
2. Data integration
3. Week 4 EDA analysis
4. Week 5 Final Visualizations
"""

import subprocess

# 1. Data Cleaning
print("Step 1: Cleaning IMDb and TMDb datasets...")
subprocess.run(["python", "data_cleaning/python_cleaning_scripts/Week_2_Cleaning_IMDB_Data.py"])
subprocess.run(["python", "data_cleaning/python_cleaning_scripts/Week_2_Cleaning_TMDB_Data.py"])
print("Data cleaning completed.\n")

# 2. Data Integration
print("Step 2: Integrating datasets...")
subprocess.run(["python", "data_integration/Week_3_IMDB_TMDB_Integration.py"])
print("Data integration completed.\n")

# 3. Week 4 EDA Analysis
print("Step 3: Running Week 4 EDA analysis...")
subprocess.run(["python", "data_analysis/Week_4_Brianna's_EDA.py"])
subprocess.run(["python", "data_analysis/Week_4_Comparisons_and_Trends.py"])
print("Week 4 EDA completed.\n")

# 4. Week 5 Final Visualizations
print("Step 4: Generating Week 5 final visualizations...")
subprocess.run(["python", "data_visualizations/Week_5_Final_Visualizations.py"])
print("Week 5 analysis completed.\n")

print("All steps completed! Check results folders for outputs.")
