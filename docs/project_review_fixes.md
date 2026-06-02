# Project Review Fixes

## Scope

This document summarizes the main corrections applied to improve the structure, consistency and methodological quality of the project.

The project is aligned with the following theme:

**Cameroonian International Migration Trends (2015-2024): Destinations, Entry Reasons and Post-Arrival Trajectories Across Available Reference Years**

The objective of these corrections was to make the project cleaner, more coherent and suitable for a GitHub-ready Data Analyst portfolio project.

## Corrections Completed

### Repository Cleanup

- Removed local Python and Jupyter cache files from project folders.
- Removed generated files such as `__pycache__/`, `.pyc` files and Jupyter checkpoints.
- Kept virtual environments ignored instead of versioning their internal package files.
- Verified that local or temporary files are not required for the analytical workflow.

### `.gitignore` Update

- Added ignore rules for:
  - `.venv/`
  - `.venv-1/`
  - Python cache files
  - Jupyter checkpoints
  - `.env`
  - operating system files
  - temporary lock files
  - `.codex`

- Replaced the broad `outputs/` ignore rule with more specific rules:
  - `outputs/temp/`
  - `outputs/cache/`

This allows `outputs/tables/` and `outputs/figures/` to remain publishable as portfolio outputs.

### Country Name Harmonization

- Added reusable country name harmonization in `src/standardize_cleaned_files.py`.
- Removed UN DESA footnote stars from destination country names.
- Added a French-to-English destination country mapping for Eurostat-style country names when needed.

This improves consistency across sources and avoids duplicated country names caused by language or formatting differences.

### `entry_reasons_master` `sub_reason` Correction

- Updated the standardization pipeline so Eurostat first permits explicitly receive `sub_reason = not_applicable`.
- Updated notebook `09_build_analytical_tables.ipynb` so `entry_reasons_master.csv` keeps the `sub_reason` column.
- Preserved OECD complementary sub-reasons such as:
  - `asylum`
  - `work`
  - `seasonal_work`

This makes the Q2 analytical table more explicit and prevents the loss of useful OECD classification details.

### Q3 Eurostat/OECD Methodological Separation

- Updated notebook `10_exploratory_data_analysis.ipynb` so main Q3 aggregations use Eurostat only.
- Kept OECD post-arrival indicators in a separate complementary section.
- Exported `oecd_post_arrival_indicators_summary.csv`.

This correction is important because Eurostat and OECD may not cover the same countries, years or administrative definitions. OECD indicators are therefore used as complementary evidence and are not merged into Eurostat post-arrival totals.

### README Rewrite

- Rewrote `README.md` in professional English.
- Aligned the README with the current project theme based on available reference years.
- Removed the old framing centered mainly on Covid-19.
- Clarified that the project does not aim to measure the causal effect of Covid-19.
- Clarified that UN DESA measures migrant stock, not arrivals.
- Added a reproducibility note explaining that `data/raw/` is not included in the repository.
- Removed the outdated "Phase 3 completed" status.

### Analytical Framing Update

- Repositioned the project around the 2015-2024 available reference period.
- Replaced the previous framing centered on Covid-19 with a more robust reference-year approach.
- Treated 2020 as a contextual point when relevant, not as a causal variable.

This makes the project more methodologically accurate because some indicators are available only for selected years or partial annual ranges.

### Visualization Notebook Creation

- Created `notebooks/11_visualization_and_reporting.ipynb`.
- The notebook generates final PNG charts in `outputs/figures/`.
- Q3 charts use Eurostat only for the main visualizations.
- OECD remains complementary for post-arrival indicators.

### Output Figures Creation

The visualization notebook is designed to create final charts for:

- Q1 destination analysis
- Q2 entry reason analysis
- Q3 Eurostat post-arrival trajectory analysis

Current expected figures include:

- `q1_top_10_destinations_2024.png`
- `q1_destination_evolution_2015_2020_2024.png`
- `q1_fastest_growing_destinations_2015_2024.png`
- `q2_entry_reasons_yearly_evolution.png`
- `q2_entry_reasons_share_by_period.png`
- `q3_post_arrival_indicators_by_year_eurostat.png`
- `q3_post_arrival_indicators_by_period_eurostat.png`
- `q3_citizenship_acquisition_by_country_eurostat.png`

### Q1 Visualization Improvement

- Replaced the previous strongest-increase chart because it was visually too similar to the destination evolution chart.
- Added a new percentage-growth chart:
  - `q1_fastest_growing_destinations_2015_2024.png`

This improves analytical diversity in the Q1 visual outputs.

## Remaining Limitations

- Raw data files are not included in the repository.
- Users who want to reproduce the full raw-to-cleaned pipeline must download the original official files and place them in the expected `data/raw/` structure.
- Some explored sources such as Canada, USA, Japan and UNHCR are documented but not included in the analytical pipeline.
- Source definitions differ across organizations, so `measure_type` must always be interpreted before comparing values.
- UN DESA migrant stock should not be interpreted as migration inflow or number of arrivals.
- OECD indicators are complementary and should not be merged into Eurostat totals without distinction.

## Final Review Note

The project is now more coherent, reproducible and suitable for portfolio review.

The main analytical pipeline is structured around three final tables:

- `destinations_master.csv`
- `entry_reasons_master.csv`
- `post_arrival_master.csv`

These tables support the three main analytical questions on destination countries, entry reasons and post-arrival trajectories across the available 2015-2024 reference period.
