# Data Catalog

## Purpose

This catalog summarizes the datasets explored for the project:

Cameroonian International Migration Trends (2015-2024): Destinations, Entry Reasons and Post-Arrival Trajectories Across Available Reference Years

The final analytical pipeline prioritizes sources that provide broad comparability across destination countries, entry reasons and post-arrival indicators.

The retained sources are:

- UN DESA
- Eurostat
- OECD

Canada, USA, Japan, UNHCR and contextual Cameroon datasets were explored during the data inventory phase. They are documented here but are not part of the final V1 analytical pipeline because they are more country-specific, context-specific or less comparable across the 2015-2024 project scope.

## Main Datasets Retained in the Analytical Pipeline

### UN DESA

- Role: global destination countries of migrants originating from Cameroon
- Coverage: 1990, 1995, 2000, 2005, 2010, 2015, 2020 and 2024
- Main use: Q1 - destination countries
- Raw file: `data/raw/global/undesa_cameroon_global_destinations.csv`
- Indicator type: migrant stock
- Cleaning note: filter `Origin == Cameroon`; use 2015, 2020 and 2024 as available reference years for the project period.

UN DESA measures migrant stock, not migration inflows. It can identify destination countries with the largest estimated number of migrants originating from Cameroon at a reference year, but it should not be interpreted as the number of arrivals during the period.

### Eurostat `migr_resfirst`

- Role: first permits by reason for Cameroonian citizens in Europe
- Coverage: 2015-2024
- Main use: Q2 - observable entry reasons
- Raw file: `data/raw/europe/eurostat_first_permits_cameroon.xlsx`
- Indicator type: first permits
- Cleaning note: one sheet per reason; reshape year columns into long format; preserve Eurostat flags when relevant.

This source supports the analysis of observable entry reasons such as family, education, work and other reasons.

### Eurostat `migr_reslong`

- Role: long-term residents
- Coverage: 2015-2024
- Main use: Q3 - post-arrival trajectories
- Raw file: `data/raw/europe/eurostat_long_term_residents_cameroon.xlsx`
- Indicator type: long-term resident status
- Cleaning note: one sheet per legal framework; start with the total legal framework when applicable.

This source helps analyze durable settlement indicators among Cameroonian migrants in European destination countries.

### Eurostat `migr_acq`

- Role: citizenship acquisition / naturalization
- Coverage: 2015-2024
- Main use: Q3 - post-arrival trajectories
- Raw file: `data/raw/europe/eurostat_citizenship_acquisition_cameroon.xlsx`
- Indicator type: citizenship acquisition
- Cleaning note: several sheets by age and sex; start with total age and total sex.

Citizenship acquisition is interpreted as a more advanced stage of legal and civic integration in the destination country.

### Eurostat `migr_reschst`

- Role: immigration status changes
- Coverage: 2020-2024
- Main use: Q3 - post-arrival trajectories
- Raw file: `data/raw/europe/eurostat_status_changes_cameroon.xlsx`
- Indicator type: status change
- Cleaning note: transform the data into long format and keep total aggregates when relevant.

This source does not cover the full 2015-2024 period, but it provides useful information on administrative transitions after arrival.

### OECD Migration Database

- Role: complementary migration stocks, inflows and administrative indicators related to Cameroon
- Coverage: 1995-2022
- Main use: complementary evidence for Q1, Q2 and Q3
- Raw file: `data/raw/global/oecd_migration_database_raw.csv`
- Indicator types: migrant stock, inflows, worker inflows, seasonal worker inflows, asylum inflows and citizenship acquisition depending on the OECD variable
- Cleaning note: large file; filter `CO2 == CMR` before analysis.

OECD indicators are useful as complementary evidence, but they should not be directly merged with UN DESA or Eurostat totals without distinction. Each OECD indicator must be interpreted according to its own `measure_type`.

## Sources Explored but Not Retained

### Canada IRCC

- Role: permanent residents, study permits and temporary-to-permanent resident transitions
- Coverage: 2015-2026 in the raw files
- Potential use: Canada-specific migration analysis
- Raw files: `data/raw/canada/ircc_*.xlsx`
- Cleaning note: multi-line headers, monthly or quarterly columns, hierarchical categories and masked values such as `--`.

Canada IRCC is a rich source, but it is highly country-specific and requires dedicated cleaning logic. It was not retained because the project prioritizes broader comparability across destination countries, entry reasons and post-arrival indicators.

### USA DHS / Census

- Role: lawful permanent residents in the United States, refugee arrivals and 2024 diaspora profile
- Coverage: LPR 2015-2022, refugees 2015-2024, ACS 2024
- Potential use: USA-specific migration analysis
- Raw files: `data/raw/usa/*.xlsx`
- Cleaning note: DHS uses fiscal years; ACS is a contextual snapshot with margins of error.

These sources are useful for a country-specific extension, but they use different definitions and time structures. They were not retained in the current analytical pipeline to avoid mixing fiscal-year admissions, refugee-specific flows and contextual census snapshots with broader international indicators.

### UNHCR

- Role: asylum seekers, refugees, resettlement and persons of concern
- Coverage: mostly up to 2016 or 2017 in the available local files
- Potential use: refugee and asylum-related analysis
- Raw files: `data/raw/unhcr/*.csv`

UNHCR is relevant for protection-related migration, but the available local files do not sufficiently cover the recent 2015-2024 analytical period. The project is also broader than refugee or asylum migration alone.

### Japan

- Role: Japan-specific migration and visa context
- Coverage: Cameroon visa-related rows from 2009-2017; inbound/outbound files stop around 2005
- Potential use: limited historical or contextual analysis
- Raw files: `data/raw/japan/*.csv`
- Cleaning note: some files may require CP932 or Shift-JIS encoding.

The available Japan files do not provide sufficient coverage for the 2015-2024 project period.

### Cameroon Demographic Context

- Role: demographic denominators and migration context
- Coverage: variable depending on the files, often up to 2017
- Potential use: contextualization and possible normalization
- Raw files: `data/raw/context/*.csv`

These files are useful for background context, but they do not directly measure international destination countries, entry reasons or post-arrival trajectories.

## Analytical Tables Produced

| Analytical Table | Main Question | Description |
|---|---|---|
| `destinations_master.csv` | Q1 | Destination countries of migrants originating from Cameroon |
| `entry_reasons_master.csv` | Q2 | Observable entry reasons |
| `post_arrival_master.csv` | Q3 | Post-arrival trajectory indicators |

These tables are stored in:

```text
data/processed/analytical/
```

## Methodological Caution

The project combines sources with different definitions and coverage. For this reason:

- `stock` is not added to `inflow`
- `permit` is not added to `citizenship_acquisition`
- OECD indicators are treated as complementary when their scope differs from Eurostat or UN DESA
- each `measure_type` must be interpreted according to its own definition
