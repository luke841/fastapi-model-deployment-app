# Script to train machine learning model.
from argparse import ArgumentParser
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from salary_analyser.algorithm.data import CensusRecord, read_csv, dataclasses_to_dataframe, dicts_to_dataclass
from salary_analyser.algorithm.models import RandomForestModel, save_model, slice_analysis


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

    model_path = args.model_output_path / "census_model.pkl"
    slice_analysis_folder = args.model_output_path / "slice_analysis"
    slice_analysis_folder.mkdir(exist_ok=True, parents=True)
    
    csv_list = read_csv(args.data_csv_path)
    data = dicts_to_dataclass(csv_list, CensusRecord)
    df_census = dataclasses_to_dataframe(data)

    train, test = train_test_split(df_census, test_size=0.20)

    model = RandomForestModel()
    model.fit(train)
    save_model(model, model_path)

    categorical_dtypes = test.select_dtypes(include=['object']).columns
    for feature_name in categorical_dtypes:
        analysis_df = slice_analysis(model, dataframe=test, feature_name=feature_name)
        analysis_df.to_csv(slice_analysis_folder / f"{feature_name}_slice_analysis.csv")
