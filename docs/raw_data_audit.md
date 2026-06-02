# Raw Data Audit - Cameroonian International Migration Trends (2015-2024)

Audit date: 2026-04-21

## Analytical Objective

This audit reviews the raw data sources collected for the project:

**Cameroonian International Migration Trends (2015-2024): Destinations, Entry Reasons and Post-Arrival Trajectories Across Available Reference Years**

The objective is to assess whether each source can support the analysis of Cameroonian international migration trends across the latest comparable data period, with a focus on:

- destination countries of migrants originating from Cameroon
- observable reasons for entry in key host countries
- post-arrival trajectory indicators such as long-term residence, status change and citizenship acquisition

Because some migration indicators are available only for selected reference years or partial annual ranges, the analysis focuses on comparable reference points and trend patterns rather than a complete annual causal analysis for every indicator.

The project does not aim to measure the causal effect of Covid-19. The year 2020 may appear as an important contextual point in some datasets, but it is not treated as the main explanatory factor.

## Executive Summary

The strongest sources for the final analytical pipeline are:

- **UN DESA**: useful for global migrant stock by origin and destination country. For the project window, it provides reference points for 2015, 2020 and 2024.
- **Eurostat**: strong source for European administrative indicators between 2015 and 2024, especially first permits, long-term residence, citizenship acquisition and status changes.
- **OECD**: useful complementary source for selected OECD countries and indicators, but its indicators must be interpreted separately by `measure_type`.

Sources explored but not retained in the final analytical pipeline:

- **Canada IRCC**: rich data source, but complex and highly country-specific.
- **USA DHS / Refugees**: useful for the United States, but coverage differs by dataset and does not fully align with the final comparative pipeline.
- **UNHCR**: useful for refugees and asylum-related analysis, but the local files mostly stop around 2016 or 2017.
- **Japan**: limited relevance for the 2015-2024 analytical period because some files stop before or near the start of the project window.
- **StatCan census**: useful as a contextual point, but not as an annual migration series.
- **Cameroon demographic context files**: useful for background context, but not for measuring international migration flows.

The final analytical pipeline prioritizes sources that provide broader comparability across destination countries, entry reasons and post-arrival indicators.

## Source Inventory and Diagnostic

### UN DESA

- File: `data/raw/global/undesa_cameroon_global_destination.csv`
- Coverage: 1990-2024
- Relevant reference years for this project: 2015, 2020 and 2024
- Status: retained as the main source for global destination analysis
- Main analytical use: Q1 - destination countries
- Indicator type: migrant stock

Cleaning requirements:

- Filter `Origin == Cameroon`
- Convert numeric values stored with spaces or formatting issues
- Keep relevant columns such as `Total`, `Male` and `Female`
- Remove aggregate rows when the analysis focuses on individual destination countries
- Standardize country names
- Remove special characters such as `*` from country names when needed

Analytical note:

UN DESA measures migrant stock, not migration inflows. It identifies countries with the largest estimated number of migrants originating from Cameroon at a reference year, but it should not be interpreted as the number of arrivals during the period.

### Eurostat - First Permits

- File: `data/raw/europe/eurostat_first_permits_cameroon.xlsx`
- Coverage: 2015-2024
- Status: retained as the main source for entry reason analysis in Europe
- Main analytical use: Q2 - observable reasons for entry
- Indicator type: first permits

Cleaning requirements:

- Extract the relevant sheets corresponding to entry reasons
- Remove metadata rows
- Transform the data from wide format to long format
- Manage Eurostat flags such as `:`, `b`, `e` and `p`
- Standardize destination country names
- Create harmonized reason categories such as `family`, `education`, `work` and `other`

Analytical note:

Eurostat first permits provide a direct breakdown of entry reasons, which makes this source the most suitable source for Q2.

### Eurostat - Long-Term Residents

- File: `data/raw/europe/eurostat_long_term_residents_cameroon.xlsx`
- Coverage: 2015-2024
- Status: retained for post-arrival trajectory analysis
- Main analytical use: Q3 - long-term residence
- Indicator type: long-term resident status

Cleaning requirements:

- Extract data by legal framework when relevant
- Transform the data into long format
- Keep destination country, year, legal framework and value
- Standardize country names and indicator labels

Analytical note:

This source helps analyze durable settlement indicators among Cameroonian migrants in European destination countries.

### Eurostat - Status Changes

- File: `data/raw/europe/eurostat_status_changes_cameroon.xlsx`
- Coverage: 2020-2024
- Status: retained as a complementary Eurostat post-arrival indicator
- Main analytical use: Q3 - administrative status changes
- Indicator type: status change

Cleaning requirements:

- Manage multiple sheets by age and sex
- Start with total aggregates for portfolio analysis
- Transform data into a consistent long format
- Standardize measure types and country names

Analytical note:

This source does not cover the entire 2015-2024 period, but it provides useful information on administrative transitions after arrival.

### Eurostat - Citizenship Acquisition

- File: `data/raw/europe/eurostat_citizenship_acquisition_cameroon.xlsx`
- Coverage: 2015-2024
- Status: retained for post-arrival trajectory analysis
- Main analytical use: Q3 - citizenship acquisition
- Indicator type: citizenship acquisition

Cleaning requirements:

- Filter `Age = Total` and `Sex = Total`
- Reduce the number of sheets used
- Transform data into long format
- Standardize country names and measure types

Analytical note:

Citizenship acquisition is interpreted as a more advanced stage of legal and civic integration in the destination country.

### OECD Migration Database

- File: `data/raw/global/oecd_migration_database_raw.csv`
- Coverage: 1995-2022
- Relevant Cameroon coverage: mainly 2015-2022
- Status: retained as a complementary source
- Main analytical use: Q1, Q2 and Q3 complementary indicators
- Indicator types: migrant stock, inflows, worker inflows, asylum inflows and citizenship acquisition depending on the selected OECD variable

Cleaning requirements:

- Filter `CO2 == CMR`
- Select relevant OECD variables
- Standardize variable names and measure types
- Avoid double counting
- Keep OECD indicators separate from UN DESA and Eurostat when definitions differ

Analytical note:

OECD is useful as complementary evidence, but its indicators should not be directly merged with UN DESA or Eurostat totals without distinction.

## Explored but Not Retained in the Final Analytical Pipeline

### Canada IRCC

- File pattern: `data/raw/canada/ircc_*.xlsx`
- Coverage: 2015-2026
- Status: explored but not retained in the final analytical pipeline
- Potential use: Canada-specific admissions, study permits and temporary-to-permanent resident transitions

Main reason for exclusion: the data is rich but highly specific to Canada and requires a dedicated cleaning logic. The final project prioritizes broader comparability across multiple destinations and data sources.

### Statistics Canada

- File: `data/raw/canada/statcan_cameroon_immigrant_status.csv`
- Coverage: 2021 census
- Status: explored as contextual information
- Potential use: contextual snapshot of the Cameroonian diaspora in Canada

Main reason for exclusion: the source provides a contextual point rather than a comparable annual or reference-year migration series.

### USA DHS Sources

- File examples: `data/raw/usa/usa_lawful_permanent_residents_cameroon.xlsx`, `data/raw/usa/usa_refugee_arrivals_cameroon.xlsx`
- Coverage: varies by source
- Status: explored but not retained in the final analytical pipeline
- Potential use: USA-specific permanent residence or refugee analysis

Main reason for exclusion: the sources are useful for a United States extension, but they use fiscal years and source-specific definitions that do not align cleanly with the final comparative pipeline.

### USA ACS

- File: `data/raw/usa/usa_acs_selected_population_cameroon.xlsx`
- Coverage: 2024
- Status: explored as contextual information
- Potential use: snapshot of the Cameroon-born population in the United States

Main reason for exclusion: the source provides a contextual snapshot, not a comparable migration trend series.

### UNHCR

- File pattern: `data/raw/unhcr/*.csv`
- Coverage: mostly up to 2016 or 2017 in the local files
- Status: explored but not retained in the final analytical pipeline
- Potential use: refugees and asylum-related analysis

Main reason for exclusion: the available local files do not cover the recent 2015-2024 period sufficiently for the project's final analytical scope.

### Japan

- File pattern: `data/raw/japan/*.csv`
- Coverage: 2009-2017 for visa-related Cameroon data, older for inbound/outbound files
- Status: explored but not retained
- Potential use: Japan-specific migration or visa analysis

Main reason for exclusion: the available files do not provide sufficient coverage for the 2015-2024 analytical period.

### Cyprus

- File: `data/raw/europe/cyprus_migration_foreign_born_population.xls`
- Coverage: to be confirmed
- Status: low priority
- Potential use: country-specific contextual information

Main reason for exclusion: the source was not prioritized because the final pipeline already uses broader Eurostat coverage for European indicators.

### Cameroon Context Files

- File pattern: `data/raw/context/*.csv`
- Coverage: variable, often up to 2017
- Status: context only
- Potential use: demographic background or normalization

Main reason for exclusion: these files are useful for background context but do not directly measure international migration destinations, entry reasons or post-arrival trajectories.

## Key Analytical Themes

### 1. Destination Countries

Main source: UN DESA.

UN DESA provides a global view of migrant stock by origin and destination country. For this project, the relevant reference years are 2015, 2020 and 2024.

The project can compare the estimated stock of migrants originating from Cameroon across these reference years. It can identify the countries with the largest estimated stock in 2024 and the countries where the stock changed the most between 2015 and 2024.

### 2. Entry Reasons

Main source: Eurostat first permits.

Eurostat first permits provide a structured breakdown of entry reasons, especially:

- family
- education
- work
- other

OECD worker inflows, seasonal worker inflows and asylum-related inflows can be used as complementary evidence, but not as direct equivalents of Eurostat first permits.

### 3. Post-Arrival Trajectories

Main source: Eurostat.

The main Eurostat post-arrival indicators are:

- long-term residence
- status changes
- citizenship acquisition

These indicators describe different dimensions of migrant trajectories after arrival. They should be analyzed separately because they do not measure the same process.

## Data Quality Issues and Risks

### 1. Incomplete Time Coverage

Several sources do not cover the full 2015-2024 period. Missing recent years should not be interpreted as a migration decline if the source simply stops earlier.

### 2. Difference Between Stocks and Flows

UN DESA measures migrant stock, while Eurostat, OECD, IRCC and DHS often measure administrative flows, permits or statuses. These indicators should not be added together.

### 3. Calendar Years vs Fiscal Years

USA DHS data uses fiscal years. If these data are used later, they must be clearly marked as fiscal year data.

### 4. Wide Formats and Metadata

Many Excel files contain title rows, metadata, multiple sheets, flags and notes. The cleaning process must explicitly extract the tabular data.

### 5. Special Values

Different sources use special values:

- Eurostat uses `:` for unavailable values and flags such as `b`, `e` and `p`
- Canada uses `--`
- USA may use `D` for suppressed values

These values must be handled before numerical analysis.

### 6. Encoding Issues

Some Japan files may require CP932 or Shift-JIS encoding instead of UTF-8.

### 7. Temporary Files

Files such as `.~lock*` are temporary lock files and should be ignored.

## Recommended Cleaning Framework

The recommended long-format analytical structure includes:

- `source`
- `dataset`
- `indicator`
- `origin_country`
- `destination_country`
- `year`
- `reference_group` or `period`
- `measure_type`
- `reason`
- `sub_reason`
- `sex`
- `age_group`
- `value`
- `unit`
- `flag`
- `year_type`
- `notes`

Recommended standardized values for `measure_type` include:

- `stock`
- `inflow`
- `permit`
- `long_term_resident`
- `status_change`
- `citizenship_acquisition`
- `asylum_inflow`
- `worker_inflow`
- `seasonal_worker_inflow`

## Priority Order for the Final Pipeline

The final pipeline should prioritize:

1. UN DESA for global destination stock analysis.
2. Eurostat first permits for observable entry reasons.
3. Eurostat long-term residents, status changes and citizenship acquisition for post-arrival trajectory indicators.
4. OECD as complementary evidence for selected OECD indicators.

Canada, USA, Japan, UNHCR and contextual files should remain documented as explored sources, but not included in the final analytical pipeline unless the project is expanded later.
