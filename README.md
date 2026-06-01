# Cameroonian International Migration Trends (2015-2024)

## Destinations, Entry Reasons and Post-Arrival Trajectories Across Available Reference Years

## Project Overview

This project analyzes Cameroonian international migration trends over the 2015-2024 reference period.

The objective is to understand how migration patterns evolved across the latest comparable years available in selected international data sources, with a focus on three analytical dimensions:

- main destination countries of Cameroonian migrants
- observable reasons for entry in key host countries
- post-arrival trajectories such as long-term residence, status change and citizenship acquisition

## Research Questions

### Q1 - Destination Countries

How did the main destination countries of Cameroonian migrants evolve across the 2015-2024 reference period?

### Q2 - Entry Reasons

How did the main observable entry reasons among Cameroonian migrants evolve across the available data period?

### Q3 - Post-Arrival Trajectories

How did post-arrival trajectory indicators evolve across the available 2015-2024 data period?

## Analytical Scope

The study covers the 2015-2024 period, which represents the latest comparable period available across the selected international sources.

The project does not aim to measure the causal effect of Covid-19. The year 2020 is treated as a contextual reference point when relevant, while the analysis focuses on trends across available reference years.

## Data Sources

The analytical pipeline uses data from:

- UN DESA: global migrant stock by destination country
- Eurostat: first permits, long-term residence, status changes and citizenship acquisition
- OECD: complementary migration indicators for OECD countries

Other sources such as Canada, USA, Japan and UNHCR were explored during the data inventory phase, but they were not retained in the analytical pipeline.

## Repository Structure

```text
cameroonian-migration-analysis/
|-- data/
|   `-- processed/
|       |-- cleaned/
|       |-- standardized/
|       `-- analytical/
|-- docs/
|   |-- data_catalog.md
|   |-- raw_data_audit.md
|   `-- project_review_fixes.md
|-- notebooks/
|   |-- 02_data_audit.ipynb
|   |-- 03_cleaning_undesa.ipynb
|   |-- 04_cleaning_eurostat_first_permits_cameroon.ipynb
|   |-- 05_eurostat_long_term_residents_cameroon.ipynb
|   |-- 06_eurostat_status_changes_cameroon.ipynb
|   |-- 07_eurostat_citizenship_acquisition.ipynb
|   |-- 08_oecd_migration_database_raw.ipynb
|   |-- 09_build_analytical_tables.ipynb
|   |-- 10_exploratory_data_analysis.ipynb
|   `-- 11_visualization_and_reporting.ipynb
|-- outputs/
|   |-- tables/
|   `-- figures/
|-- src/
|   |-- config.py
|   `-- standardize_cleaned_files.py
|-- README.md
|-- requirements.txt
`-- .gitignore
```

## Data Pipeline

The project follows a structured data pipeline:

```text
data audit -> cleaning -> standardization -> analytical tables -> exploratory analysis -> visual outputs
```

### 1. Cleaned Data

The `data/processed/cleaned/` folder contains cleaned datasets produced from each original source.

### 2. Standardized Data

The `data/processed/standardized/` folder contains harmonized datasets with common columns, consistent country names, comparable year formats and standardized indicator types.

### 3. Analytical Tables

The `data/processed/analytical/` folder contains the three final analytical tables used for the analysis.

### 4. Exploratory Analysis

The `outputs/tables/` folder contains summary tables generated from the exploratory analysis.

### 5. Visual Outputs

The `outputs/figures/` folder contains the final charts created from the analytical tables and summary outputs.

## Main Outputs

### Summary Tables

The `outputs/tables/` folder contains summary tables created during the exploratory analysis, including:

- top destination countries
- strongest destination increases
- entry reasons by available year or operational reference period
- entry reason shares
- post-arrival indicators by year and indicator type
- complementary OECD summaries

### Figures

The `outputs/figures/` folder contains final charts, including:

```text
q1_top_10_destinations_2024.png
q1_destination_evolution_2015_2020_2024.png
q1_fastest_growing_destinations_2015_2024.png
q2_entry_reasons_yearly_evolution.png
q2_entry_reasons_share_by_period.png
q3_post_arrival_indicators_by_year_eurostat.png
q3_post_arrival_indicators_by_period_eurostat.png
q3_citizenship_acquisition_by_country_eurostat.png
```

## Methodological Notes

This project combines several international data sources. These sources do not always measure the same phenomenon.

For this reason:

- migrant stocks are not added to inflows
- first permits are not added to citizenship acquisitions
- Eurostat and OECD indicators are not merged without distinction
- each `measure_type` is interpreted according to its own definition
- OECD data is used as complementary evidence when it does not match Eurostat's scope directly
- the analysis does not claim to provide a causal explanation of migration changes

For Q1, UN DESA is used as the main source because it provides a global view of migrant stock by destination country.

For Q2, Eurostat first permits are used as the main source because they provide a direct breakdown of entry reasons.

For Q3, Eurostat is used as the main source for post-arrival trajectories. OECD is used as complementary evidence only and is not merged into Eurostat post-arrival totals.

## Reproducibility Note

Raw files are not included in this repository.

The repository includes cleaned, standardized and analytical datasets used for the portfolio analysis.

The absence of `data/raw/` does not prevent reviewing the analytical pipeline, outputs and portfolio results, because the processed datasets and analytical tables are included.

## How to Run the Project

### 1. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Execution Options

### Option 1 - Portfolio Analysis Reproduction

This option is recommended for reviewing the project as a portfolio case study.

It uses the processed and analytical datasets already included in the repository.

Run the notebooks in this order:

```text
09_build_analytical_tables.ipynb
10_exploratory_data_analysis.ipynb
11_visualization_and_reporting.ipynb
```

This reproduces the main analytical tables, exploratory outputs and final visualizations.

### Option 2 - Full Raw-to-Cleaned Pipeline Reproduction

To reproduce the entire pipeline from the original raw files, users must first download the official source files from UN DESA, Eurostat and OECD, then place them in the expected `data/raw/` folder structure.

After that, run the notebooks in this order:

```text
02_data_audit.ipynb
03_cleaning_undesa.ipynb
04_cleaning_eurostat_first_permits_cameroon.ipynb
05_eurostat_long_term_residents_cameroon.ipynb
06_eurostat_status_changes_cameroon.ipynb
07_eurostat_citizenship_acquisition.ipynb
08_oecd_migration_database_raw.ipynb
09_build_analytical_tables.ipynb
10_exploratory_data_analysis.ipynb
11_visualization_and_reporting.ipynb
```

## Project Status

Project status: completed for portfolio review. Further improvements may include additional sources, dashboard development and deeper storytelling.
