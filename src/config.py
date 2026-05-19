from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
NOTEBOOKS = PROJECT_ROOT / "notebooks"
OUTPUTS = PROJECT_ROOT / "outputs"
DOCS = PROJECT_ROOT / "docs"

START_YEAR = 2015
END_YEAR = 2024
COUNTRY_OF_ORIGIN = "Cameroon"