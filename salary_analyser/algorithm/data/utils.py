import csv

from fastapi.encoders import jsonable_encoder
from pathlib import Path
import pandas as pd
from pydantic import BaseModel


def read_csv(path) -> list[dict]:
    with open(path, "r") as fp:
        reader = csv.DictReader(fp, delimiter=',', skipinitialspace=True)
        records = list(reader)
    return records


def write_dataclasses_to_csv(csv_file: str, dataclass_list: list):
    fieldnames = dataclass_list[0].dict(by_alias=True).keys()
    
    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in dataclass_list:
            writer.writerow(record.dict(by_alias=True))

def dicts_to_dataclass(records: list[dict], DataClass):
    return list(map(lambda record: DataClass(**record), records))


def dataclasses_to_dataframe(dataclasses: list[BaseModel], by_alias: bool=False) -> pd.DataFrame:
    return pd.DataFrame(jsonable_encoder(dataclasses, by_alias=by_alias) )
