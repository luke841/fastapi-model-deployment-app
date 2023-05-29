from pathlib import Path 

PACKAGE_TOP = Path(__file__).parent.parent.parent.parent

MODEL_CATEGORICAL_COLUMNS = [
    "workclass",
    "education",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native_country",
]

MODEL_LABEL_COLUMN = "salary"

DEFAULT_MODEL_PATH = PACKAGE_TOP / "files" / "model" / "census_model.pkl"
