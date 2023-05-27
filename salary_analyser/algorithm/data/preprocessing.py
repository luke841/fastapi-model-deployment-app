from pathlib import Path

from .census_record import CensusRecord
from .utils import (
    dicts_to_dataclass, 
    read_csv, 
    replace_string_in_dict_keys, 
    write_dataclasses_to_csv,
)


def clean_census_records(census_records: list[dict]):
    return replace_string_in_dict_keys(census_records, "-", "_")


def cleanse_census_csv(src_file: Path, output_file: Path):
    census_record_list = read_csv(src_file)
    cleansed_records = clean_census_records(census_record_list)
    cleansed_records_dataclasses = dicts_to_dataclass(cleansed_records, CensusRecord)
    write_dataclasses_to_csv(output_file, cleansed_records_dataclasses)


