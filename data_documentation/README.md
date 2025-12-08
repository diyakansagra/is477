This folder contains all the raw data, licensing documentation, governance, and data notes.

## Licensing, Governance, and Data Notes

### Licensing:

The IMDb raw dataset used in this project was obtained from a publicly available Kaggle upload. Because it is not an official dataset released by IMDb, its licensing terms are not explicitly stated. IMDb’s data is normally covered by restrictive Terms of Service, so this dataset should be treated as informational and non-commercial. No redistribution or commercial use is intended.

### Data Governance:

The dataset is stored in the data_integration and data_cleaning folders and is version-controlled through GitHub. Any transformations, cleaning steps, or merges are documented in the project’s workflow, allowing full reproducibility. Only cleaned and processed versions of the data are used in analysis notebooks to maintain consistency throughout the project.

### Data Notes:

The raw data contains inconsistencies (e.g., formatting differences in runtime, quoted fields, missing values, and mixed units). These issues are addressed through cleaning scripts before analysis. Since the dataset is user-uploaded and scraped, there may be deviations from official IMDb records. All insights and visualizations should therefore be interpreted with these limitations in mind.

Please see the finalREADME.md for most detailed information on licensing documentation, governance, and data notes.
