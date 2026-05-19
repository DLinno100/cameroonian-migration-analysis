# Data Catalog

See also: [raw_data_audit.md](raw_data_audit.md)

## Core datasets

### UN DESA
- Role: Global destinations of Cameroonian migrants
- Coverage: 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024
- Main use: Q1
- Raw file: `data/raw/global/undesa_cameroon_global_destinations.csv`
- Cleaning note: filter `Origin == Cameroon`; use 2015, 2020 and 2024 for the study period.

### Eurostat migr_resfirst
- Role: First permits by reason for Cameroonian citizens in Europe
- Coverage: 2015–2024
- Main use: Q2
- Raw file: `data/raw/europe/eurostat_first_permits_cameroon.xlsx`
- Cleaning note: one sheet per reason; reshape year columns to long format and preserve Eurostat flags.

### Eurostat migr_reslong
- Role: Long-term residents
- Coverage: 2015–2024
- Main use: Q3
- Raw file: `data/raw/europe/eurostat_long_term_residents_cameroon.xlsx`
- Cleaning note: one sheet per legal framework; start with total framework.

### Eurostat migr_acq
- Role: Citizenship acquisition / naturalisation
- Coverage: 2015–2024
- Main use: Q3
- Raw file: `data/raw/europe/eurostat_citizenship_acquisition_cameroon.xlsx`
- Cleaning note: many age/sex sheets; start with total age and total sex.

### Eurostat migr_reschst
- Role: Changes of immigration status
- Coverage: 2020–2024
- Main use: Q3, Covid and post-Covid only
- Raw file: `data/raw/europe/eurostat_status_changes_cameroon.xlsx`

### Canada IRCC
- Role: Permanent residents, study permits, and temporary-to-permanent transitions
- Coverage: 2015–2026 in raw files; use 2015–2024 for analysis
- Main use: Q2 and Q3
- Raw files: `data/raw/canada/ircc_*.xlsx`
- Cleaning note: multi-row headers, monthly/quarterly columns, category hierarchy, and suppressed values `--`.

### USA DHS / Census
- Role: US lawful permanent residents, refugee arrivals, and 2024 diaspora profile
- Coverage: LPR 2015–2022, refugees 2015–2024, ACS 2024
- Main use: Q1 and Q3
- Raw files: `data/raw/usa/*.xlsx`
- Cleaning note: DHS uses fiscal years; ACS is a point-in-time context table with margins of error.

### OECD migration database
- Role: OECD complementary flows/stocks for Cameroon-origin or Cameroon-nationality migration
- Coverage: 1995–2022
- Main use: Q1 and cross-checks
- Raw file: `data/raw/global/oecd_migration_database_raw.csv`
- Cleaning note: large file; filter `CO2 == CMR` before analysis.

## Secondary / context datasets

### UNHCR
- Role: Asylum seekers, refugees, resettlement and persons of concern
- Coverage: mostly up to 2016 or 2017 in current raw files
- Main use: historical/context only unless refreshed
- Raw files: `data/raw/unhcr/*.csv`

### Japan
- Role: Japan migration/visa context
- Coverage: visa rows for Cameroon 2009–2017; inbound/outbound files stop in 2005
- Main use: limited historical/context use
- Raw files: `data/raw/japan/*.csv`
- Cleaning note: `japan_translation_mapping.csv` needs CP932/Shift-JIS encoding.

### Cameroon demographic context
- Role: demographic denominators and migration context
- Coverage: varies by file, often up to 2017
- Main use: contextualization and normalization only
- Raw files: `data/raw/context/*.csv`
