from pathlib import Path
import unicodedata
import warnings

import pandas as pd

from config import COUNTRY_OF_ORIGIN, DATA_PROCESSED


CLEANED_DIR = DATA_PROCESSED / "cleaned"
STANDARDIZED_DIR = DATA_PROCESSED / "standardized"


OUTPUT_FILES = {
    "undesa_destinations_cleaned.csv": "undesa_destinations_standardized.csv",
    "eurostat_first_permits_cleaned.csv": "eurostat_first_permits_standardized.csv",
    "eurostat_long_term_residents_cleaned.csv": "eurostat_long_term_residents_standardized.csv",
    "eurostat_status_changes_cleaned.csv": "eurostat_status_changes_standardized.csv",
    "eurostat_citizenship_acquisition_cleaned.csv": "eurostat_citizenship_acquisition_standardized.csv",
    "oecd_migration_cleaned.csv": "oecd_migration_standardized.csv",
}


OECD_NATURE_TO_MEASURE_TYPE = {
    "Inflows of foreign population by nationality": "inflow",
    "Outflows of foreign population by nationality": "outflow",
    "Inflows of asylum seekers by nationality": "asylum_inflow",
    "Stock of foreign-born population by country of birth": "stock_birth",
    "Stock of foreign population by nationality": "stock_nationality",
    "Acquisition of nationality by country of former nationality": "citizenship_acquisition",
    "Inflows of foreign workers by nationality": "worker_inflow",
    "Inflows of seasonal foreign workers by nationality": "seasonal_worker_inflow",
}


OECD_MEASURE_TYPES = set(OECD_NATURE_TO_MEASURE_TYPE.values())


OECD_REASON_MAPPING = {
    "worker_inflow": "work",
    "seasonal_worker_inflow": "work",
    "asylum_inflow": "other",
    "inflow": "unknown",
    "outflow": "not_applicable",
    "stock_birth": "not_applicable",
    "stock_nationality": "not_applicable",
    "citizenship_acquisition": "not_applicable",
}


OECD_SUB_REASON_MAPPING = {
    "asylum_inflow": "asylum",
    "worker_inflow": "work",
    "seasonal_worker_inflow": "seasonal_work",
}


OECD_ANALYSIS_QUESTION_MAPPING = {
    "inflow": "Q1_destinations",
    "stock_birth": "Q1_destinations",
    "stock_nationality": "Q1_destinations",
    "asylum_inflow": "Q2_entry_reasons",
    "worker_inflow": "Q2_entry_reasons",
    "seasonal_worker_inflow": "Q2_entry_reasons",
    "citizenship_acquisition": "Q3_post_arrival_trajectories",
    "outflow": "secondary_outflow",
}


FIRST_PERMIT_REASON_MAPPING = {
    "famille": "family",
    "education": "education",
    "etude": "education",
    "professionnel": "work",
    "travail": "work",
    "autre": "other",
}


COUNTRY_NAME_MAPPING = {
    "belgique": "Belgium",
    "allemagne": "Germany",
    "autriche": "Austria",
    "bulgarie": "Bulgaria",
    "chypre": "Cyprus",
    "croatie": "Croatia",
    "danemark": "Denmark",
    "espagne": "Spain",
    "estonie": "Estonia",
    "finlande": "Finland",
    "france": "France",
    "grece": "Greece",
    "hongrie": "Hungary",
    "irlande": "Ireland",
    "islande": "Iceland",
    "italie": "Italy",
    "lettonie": "Latvia",
    "liechtenstein": "Liechtenstein",
    "lituanie": "Lithuania",
    "luxembourg": "Luxembourg",
    "malte": "Malta",
    "norvege": "Norway",
    "pays-bas": "Netherlands",
    "pologne": "Poland",
    "portugal": "Portugal",
    "roumanie": "Romania",
    "serbie": "Serbia",
    "slovaquie": "Slovakia",
    "slovenie": "Slovenia",
    "suisse": "Switzerland",
    "suede": "Sweden",
    "tchequie": "Czechia",
    "united kingdom": "United Kingdom",
}


TEXT_COLUMNS = [
    "destination_country",
    "origin_country",
    "source",
    "dataset",
    "measure_type",
    "period",
    "analysis_question",
    "reason",
    "sub_reason",
    "nature",
]


BASE_COLUMN_ORDER = [
    "destination_country",
    "origin_country",
    "year",
    "value",
    "source",
    "dataset",
    "measure_type",
    "period",
    "analysis_question",
    "reason",
    "sub_reason",
    "nature",
    "total_migrants",
    "male_migrants",
    "female_migrants",
    "destination_code",
    "origin_code",
]


def assign_period(year):
    """Assign the operational reference period used in the migration analysis."""
    if pd.isna(year):
        return "outside_scope"

    try:
        year = int(year)
    except (TypeError, ValueError):
        return "outside_scope"

    if 2015 <= year <= 2019:
        return "pre_covid"
    if 2020 <= year <= 2021:
        return "covid"
    if 2022 <= year <= 2024:
        return "post_covid"
    return "outside_scope"


def warn_missing_columns(file_name, df, expected_columns):
    missing_columns = [column for column in expected_columns if column not in df.columns]
    if missing_columns:
        warnings.warn(
            f"{file_name}: missing expected column(s): {', '.join(missing_columns)}",
            stacklevel=2,
        )


def read_cleaned_csv(file_name):
    path = CLEANED_DIR / file_name
    if not path.exists():
        warnings.warn(f"{file_name}: file not found in {CLEANED_DIR}", stacklevel=2)
        return None
    return pd.read_csv(path)


def rename_standard_columns(df):
    rename_columns = {
        "permits": "value",
        "covid_period": "period",
        "entry_reasons": "reason",
    }
    return df.rename(
        columns={old: new for old, new in rename_columns.items() if old in df.columns}
    )


def normalize_reason_value(value):
    if pd.isna(value):
        return pd.NA

    normalized = str(value).strip().lower()
    normalized = unicodedata.normalize("NFKD", normalized)
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))

    return FIRST_PERMIT_REASON_MAPPING.get(normalized, normalized)


def normalize_country_key(value):
    normalized = unicodedata.normalize("NFKD", value)
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    return normalized.lower()


def normalize_destination_country(value):
    """Standardize destination names before analytical tables are built."""
    if pd.isna(value):
        return pd.NA

    # UN DESA sometimes marks destination names with footnote stars.
    cleaned = str(value).replace("*", "").strip()
    cleaned = " ".join(cleaned.split())

    if not cleaned:
        return pd.NA

    return COUNTRY_NAME_MAPPING.get(normalize_country_key(cleaned), cleaned)


def add_origin_country(df):
    if "origin_country" not in df.columns:
        df["origin_country"] = COUNTRY_OF_ORIGIN
    else:
        df["origin_country"] = df["origin_country"].fillna(COUNTRY_OF_ORIGIN)
        df.loc[df["origin_country"].astype("string").str.strip() == "", "origin_country"] = (
            COUNTRY_OF_ORIGIN
        )
    return df


def ensure_period(df):
    if "period" not in df.columns:
        df["period"] = df["year"].apply(assign_period) if "year" in df.columns else "outside_scope"
        return df

    if "year" in df.columns:
        missing_period = df["period"].isna() | (df["period"].astype("string").str.strip() == "")
        df.loc[missing_period, "period"] = df.loc[missing_period, "year"].apply(assign_period)

    return df


def clean_required_rows(df):
    if "year" not in df.columns:
        df["year"] = pd.NA
    if "destination_country" not in df.columns:
        df["destination_country"] = pd.NA

    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["destination_country"] = df["destination_country"].astype("string").str.strip()
    df["destination_country"] = (
        df["destination_country"].apply(normalize_destination_country).astype("string")
    )

    valid_rows = df["year"].notna() & df["destination_country"].notna()
    valid_rows &= df["destination_country"] != ""

    return df.loc[valid_rows].copy()


def harmonize_types(df):
    df = clean_required_rows(df)

    df["year"] = df["year"].astype("Int64")

    if "value" not in df.columns:
        df["value"] = pd.NA
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    df = ensure_period(df)
    df = add_origin_country(df)

    for column in TEXT_COLUMNS:
        if column in df.columns:
            df[column] = df[column].astype("string")

    return df


def order_columns(df):
    ordered_columns = [column for column in BASE_COLUMN_ORDER if column in df.columns]
    remaining_columns = [column for column in df.columns if column not in ordered_columns]
    return df[ordered_columns + remaining_columns]


def standardize_common(df, file_name, expected_columns):
    warn_missing_columns(file_name, df, expected_columns)
    df = rename_standard_columns(df)
    df = harmonize_types(df)
    return order_columns(df)


def standardize_undesa():
    file_name = "undesa_destinations_cleaned.csv"
    df = read_cleaned_csv(file_name)
    if df is None:
        return None

    warn_missing_columns(file_name, df, ["destination_country", "year", "total_migrants", "source"])
    df = rename_standard_columns(df)

    if "total_migrants" in df.columns:
        df["value"] = df["total_migrants"]
    else:
        df["value"] = pd.NA

    df["dataset"] = "undesa_destinations"
    df["source"] = "undesa"
    df["measure_type"] = "stock"
    df["analysis_question"] = "Q1_destinations"

    df = harmonize_types(df)
    return order_columns(df)


def standardize_eurostat_first_permits():
    file_name = "eurostat_first_permits_cleaned.csv"
    df = read_cleaned_csv(file_name)
    if df is None:
        return None

    df = standardize_common(
        df,
        file_name,
        ["destination_country", "entry_reasons", "year", "permits", "source"],
    )

    if "reason" in df.columns:
        df["reason"] = df["reason"].apply(normalize_reason_value).astype("string")
        unknown_reasons = sorted(
            reason
            for reason in df["reason"].dropna().unique()
            if reason not in {"family", "education", "work", "other"}
        )
        if unknown_reasons:
            warnings.warn(
                f"{file_name}: unmapped reason value(s): {', '.join(unknown_reasons)}",
                stacklevel=2,
            )
    else:
        df["reason"] = pd.NA

    df["dataset"] = "eurostat_first_permits"
    df["source"] = "eurostat"
    df["measure_type"] = "permit"
    df["analysis_question"] = "Q2_entry_reasons"

    # Eurostat first permits have a main reason only. The explicit value keeps
    # the Q2 analytical table compatible with OECD sub-indicators.
    if "sub_reason" not in df.columns:
        df["sub_reason"] = "not_applicable"
    else:
        missing_sub_reason = df["sub_reason"].isna() | (
            df["sub_reason"].astype("string").str.strip() == ""
        )
        df.loc[missing_sub_reason, "sub_reason"] = "not_applicable"

    df = ensure_period(df)
    df = harmonize_types(df)
    return order_columns(df)


def standardize_eurostat_long_term_residents():
    file_name = "eurostat_long_term_residents_cleaned.csv"
    df = read_cleaned_csv(file_name)
    if df is None:
        return None

    df = standardize_common(
        df,
        file_name,
        ["destination_country", "year", "permits", "source", "covid_period"],
    )

    df["dataset"] = "eurostat_long_term_residents"
    df["source"] = "eurostat"
    df["measure_type"] = "long_term_resident"
    df["analysis_question"] = "Q3_post_arrival_trajectories"

    if "nature" in df.columns:
        nature_matches_measure_type = df["nature"].fillna("long_term_resident").eq(
            "long_term_resident"
        )
        if nature_matches_measure_type.all():
            df = df.drop(columns=["nature"])

    df = harmonize_types(df)
    return order_columns(df)


def standardize_eurostat_status_changes():
    file_name = "eurostat_status_changes_cleaned.csv"
    df = read_cleaned_csv(file_name)
    if df is None:
        return None

    df = standardize_common(
        df,
        file_name,
        ["destination_country", "year", "permits", "source", "covid_period"],
    )

    df["dataset"] = "eurostat_status_changes"
    df["source"] = "eurostat"
    df["measure_type"] = "status_change"
    df["analysis_question"] = "Q3_post_arrival_trajectories"

    if "nature" in df.columns and df["nature"].fillna("status_change").eq("status_change").all():
        df = df.drop(columns=["nature"])

    df = harmonize_types(df)
    return order_columns(df)


def standardize_eurostat_citizenship_acquisition():
    file_name = "eurostat_citizenship_acquisition_cleaned.csv"
    df = read_cleaned_csv(file_name)
    if df is None:
        return None

    df = standardize_common(
        df,
        file_name,
        ["destination_country", "year", "permits", "source", "covid_period"],
    )

    if "nature" in df.columns:
        df["nature"] = "citizenship_acquisition"

    df["dataset"] = "eurostat_citizenship_acquisition"
    df["source"] = "eurostat"
    df["measure_type"] = "citizenship_acquisition"
    df["analysis_question"] = "Q3_post_arrival_trajectories"

    if "nature" in df.columns and df["nature"].fillna("citizenship_acquisition").eq(
        "citizenship_acquisition"
    ).all():
        df = df.drop(columns=["nature"])

    df = harmonize_types(df)
    return order_columns(df)


def standardize_oecd_migration():
    file_name = "oecd_migration_cleaned.csv"
    df = read_cleaned_csv(file_name)
    if df is None:
        return None

    df = standardize_common(
        df,
        file_name,
        ["destination_country", "year", "permits", "source", "nature", "covid_period"],
    )

    if "nature" in df.columns:
        df["measure_type"] = df["nature"].map(OECD_NATURE_TO_MEASURE_TYPE)

        already_standardized = df["nature"].where(df["nature"].isin(OECD_MEASURE_TYPES))
        df["measure_type"] = df["measure_type"].fillna(already_standardized)

        missing_measure_type = df.loc[df["measure_type"].isna(), "nature"].dropna().unique()
        if len(missing_measure_type) > 0:
            warnings.warn(
                f"{file_name}: unmapped OECD nature value(s): "
                f"{', '.join(sorted(missing_measure_type))}",
                stacklevel=2,
            )
    else:
        df["nature"] = pd.NA
        df["measure_type"] = pd.NA

    df["reason"] = df["measure_type"].map(OECD_REASON_MAPPING)
    df["sub_reason"] = df["measure_type"].map(OECD_SUB_REASON_MAPPING).fillna("not_applicable")
    df["analysis_question"] = df["measure_type"].map(OECD_ANALYSIS_QUESTION_MAPPING)
    df["dataset"] = "oecd_migration_database"
    df["source"] = "oecd"

    df = harmonize_types(df)
    return order_columns(df)


def create_report_row(file_name, df):
    return {
        "file_name": file_name,
        "rows": len(df),
        "columns": len(df.columns),
        "missing_year": int(df["year"].isna().sum()) if "year" in df.columns else len(df),
        "missing_destination_country": (
            int(df["destination_country"].isna().sum())
            if "destination_country" in df.columns
            else len(df)
        ),
        "missing_value": int(df["value"].isna().sum()) if "value" in df.columns else len(df),
        "duplicated_rows": int(df.duplicated().sum()),
        "min_year": int(df["year"].min()) if "year" in df.columns and df["year"].notna().any() else pd.NA,
        "max_year": int(df["year"].max()) if "year" in df.columns and df["year"].notna().any() else pd.NA,
        "available_periods": (
            "|".join(sorted(df["period"].dropna().astype(str).unique()))
            if "period" in df.columns
            else ""
        ),
        "available_measure_types": (
            "|".join(sorted(df["measure_type"].dropna().astype(str).unique()))
            if "measure_type" in df.columns
            else ""
        ),
    }


def write_standardized_file(input_file_name, df):
    output_file_name = OUTPUT_FILES[input_file_name]
    output_path = STANDARDIZED_DIR / output_file_name
    df.to_csv(output_path, index=False)
    return output_file_name


def main():
    STANDARDIZED_DIR.mkdir(parents=True, exist_ok=True)

    standardizers = {
        "undesa_destinations_cleaned.csv": standardize_undesa,
        "eurostat_first_permits_cleaned.csv": standardize_eurostat_first_permits,
        "eurostat_long_term_residents_cleaned.csv": standardize_eurostat_long_term_residents,
        "eurostat_status_changes_cleaned.csv": standardize_eurostat_status_changes,
        "eurostat_citizenship_acquisition_cleaned.csv": standardize_eurostat_citizenship_acquisition,
        "oecd_migration_cleaned.csv": standardize_oecd_migration,
    }

    report_rows = []
    for input_file_name, standardizer in standardizers.items():
        standardized_df = standardizer()
        if standardized_df is None:
            continue

        output_file_name = write_standardized_file(input_file_name, standardized_df)
        report_rows.append(create_report_row(output_file_name, standardized_df))

    report = pd.DataFrame(report_rows)
    report.to_csv(STANDARDIZED_DIR / "standardization_report.csv", index=False)

    print("Standardization completed successfully.")


if __name__ == "__main__":
    main()
