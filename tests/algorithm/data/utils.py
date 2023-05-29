import csv
from pathlib import Path
import tempfile

from pydantic import BaseModel, Field

from salary_analyser.algorithm.data.utils import dicts_to_dataclass, read_csv, write_dataclasses_to_csv


class MockDataclass(BaseModel):
    value: int
    alias_field: int = Field(alias='alias-field', default=1)


def test_read_csv():
    example_data = [dict(value1='1', value2='2'), dict(value1='10', value2='11')]

    # write the example data to csv and load back with the read_csv function
    with tempfile.TemporaryDirectory() as tmpdirname:
        csv_path = Path(tmpdirname) / "test.csv"
            
        # write example recoprds to csv
        with open(csv_path, "w") as fp:
            writer = csv.DictWriter(fp, fieldnames=["value1", "value2"])
            writer.writeheader()
            for record in example_data:
                writer.writerow(record)

        # load back the example values
        returned_csv_records = read_csv(csv_path)

    # assert example values equate

    assert example_data == returned_csv_records


def test_dicts_to_dataclass():
    dicts = [dict(value=10), dict(value=20)]
    dataclasses = dicts_to_dataclass(dicts, MockDataclass)

    assert isinstance(dataclasses[0], MockDataclass)
    assert isinstance(dataclasses[1], MockDataclass)
    assert dataclasses[0].value == 10
    assert dataclasses[1].value == 20


def test_write_dataclasses_to_csv():
    dataclasses = [MockDataclass(value=10), MockDataclass(value=20)]

    with tempfile.TemporaryDirectory() as tmpdirname:
        csv_path = Path(tmpdirname) / "test.csv"

        #ensure csv is created
        assert not csv_path.exists()
        write_dataclasses_to_csv(csv_path, dataclasses)
        assert csv_path.exists()

        # read in the csv rows
        with open(csv_path, "r") as fp:
            reader = csv.reader(fp, delimiter=',')
            csv_data = list(reader)

        # check csv values are correct
        assert csv_data[0] == ["value", "alias-field"]
        assert csv_data[1] == ["10", "1"]
        assert csv_data[2] == ["20", "1"]
