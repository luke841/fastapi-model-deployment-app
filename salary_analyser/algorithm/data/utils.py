import csv
from copy import deepcopy
from pathlib import Path

from dataclasses import asdict


def read_csv(path) -> list[dict]:
    with open(path, "r") as fp:
        reader = csv.DictReader(fp, delimiter=',', skipinitialspace=True)
        census_values = list(reader)
    return census_values


def write_dataclasses_to_csv(csv_file: str, dataclass_list: list):
    fieldnames = dataclass_list[0].__annotations__.keys()
    
    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in dataclass_list:
            writer.writerow(asdict(record))

def dicts_to_dataclass(records: list[dict], DataClass):
    return list(map(lambda record: DataClass(**record), records))


def replace_string_in_dict_keys(records: list[dict], search_string, update_string) -> list[dict]:
    records = deepcopy(records)
    for record in records:
        updated_record = { k.replace(search_string, update_string): v for k, v in record.items()}
        record.clear()
        record.update(updated_record)
        
    return records
