from argparse import ArgumentParser
from pathlib import Path

from salary_analyser.algorithm.data import (
    CensusRecord,
    dicts_to_dataclass, 
    read_csv, 
    write_dataclasses_to_csv,
)


def handle_inputs():
    parser = ArgumentParser("cleanses the census records and saves to disk")

    parser.add_argument(
        "--src_file",
        type=Path,
        required=True,
        help="Path to the source csv with raw census data",
    )
    parser.add_argument(
        "--output_file",
        type=Path,
        required=True,
        help="Path to save the cleansed census csv",
    )
    return parser.parse_args()


def cleanse_census_csv(src_file: Path, output_file: Path):
    """
    
    """
    # Read in the csv and format to dictionaries
    census_record_list = read_csv(src_file)
    
    # Convert into dataclasses and validate
    census_records = dicts_to_dataclass(census_record_list, CensusRecord)

    # Output cleansed file to csv
    write_dataclasses_to_csv(output_file, census_records)


if __name__ == "__main__":
    args = handle_inputs()
    cleanse_census_csv(args.src_file, args.output_file)
