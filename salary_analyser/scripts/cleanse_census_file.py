from argparse import ArgumentParser
from pathlib import Path

from salary_analyser.algorithm.data import (
    clean_census_records,
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
    
    # Replace the - for _ int the census keys so they can be validated.
    cleansed_records = clean_census_records(census_record_list) 
    
    # Convert into dataclasses and validate
    cleansed_records_dataclasses = dicts_to_dataclass(cleansed_records, CensusRecord)

    # Output cleansed file to csv
    write_dataclasses_to_csv(output_file, cleansed_records_dataclasses)


if __name__ == "__main__":
    args = handle_inputs()
    cleanse_census_csv(args.src_file, args.output_file)



# from pathlib import Path

# from .census_record import CensusRecord
# from .utils import (
#     clean_census_records,
#     dicts_to_dataclass, 
#     read_csv, 
#     write_dataclasses_to_csv,
# )


# def handle_inputs():
#     parser = ArgumentParser("cleanses the census records and saves to disk")

#     parser.add_argument(
#         "--src_file",
#         type=Path,
#         required=True,
#         help="Path to the source csv with raw census data",
#     )
#     parser.add_argument(
#         "--output_file",
#         type=Path,
#         required=True,
#         help="Path to save the cleansed census csv",
#     )
#     return parser.parse_args()


# def cleanse_census_csv(src_file: Path, output_file: Path):
#     """
    
#     """
#     # Read in the csv and format to dictionaries
#     census_record_list = read_csv(src_file)
    
#     # Replace the - for _ int the census keys so they can be validated.
#     cleansed_records = clean_census_records(census_record_list) 
    
#     # Convert into dataclasses and validate
#     cleansed_records_dataclasses = dicts_to_dataclass(cleansed_records, CensusRecord)

#     # Output cleansed file to csv
#     write_dataclasses_to_csv(output_file, cleansed_records_dataclasses)


# if __name__ == "__main__":
#     args = handle_inputs()
#     cleanse_census_csv(args.src_file, args.output_file)
