import csv
from pathlib import Path

from pydantic import BaseModel


def read_csv(path: Path) -> list[dict]:
    with open(path, "r") as fp:
        reader = csv.DictReader(fp, delimiter=',', skipinitialspace=True)
        census_values = list(reader)
    return census_values


def write_dataclasses_to_csv(csv_file: Path, dataclass_list: list[BaseModel]):
    fieldnames = dataclass_list[0].dict(by_alias=True).keys()
    
    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in dataclass_list:
            writer.writerow(record.dict(by_alias=True))

def dicts_to_dataclass(records: list[dict], dataclass: BaseModel):
    return list(map(lambda record: dataclass(**record), records))
