# Script to train machine learning model.
from argparse import ArgumentParser
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from salary_analyser.algorithm.data import CensusRecord, read_csv, dicts_to_dataclass
from salary_analyser.algorithm.models import RandomForestModel, save_model


def handle_training_inputs():
    parser = ArgumentParser("trains the model on the dataset")

    parser.add_argument(
        "--data_csv_path",
        type=Path,
        required=True,
        help="Path to the source csv with the census data",
    )
    parser.add_argument(
        "--model_output_path",
        type=Path,
        required=True,
        help="Path to save the model once trained",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = handle_training_inputs()
    
    csv_list = read_csv(args.data_csv_path)
    data = dicts_to_dataclass(csv_list, CensusRecord)
    df_census = pd.DataFrame(data)

    train, test = train_test_split(df_census, test_size=0.20)

    model = RandomForestModel()
    model.fit(train)
    model.predict(test)
    save_model(model, args.model_output_path)
