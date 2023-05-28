from pathlib import Path
import pytest
import tempfile

import pandas as pd
from salary_analyser.algorithm.models import load_model, save_model, RandomForestModel


@pytest.fixture
def train_features():
    train_features = pd.DataFrame([
        dict(label="medium", career="mechanic", age=25),
        dict(label="medium", career="mechanic", age=28),
        dict(label="high", career="pilot", age=40),
        dict(label="high", career="pilot", age=43),
    ])
    return train_features


@pytest.fixture
def test_features():
    test_features = pd.DataFrame([
        dict(career="mechanic", age=30),
        dict(career="pilot", age=40),
    ])
    return test_features


class MockModel:
    def __init__(self, variable: int):
        self.variable = variable

        
def test_save_model():
    test_variable = 10
    mock_model = MockModel(test_variable)
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        model_path = Path(tmpdirname) / "model.pkl"
        save_model(mock_model, model_path)
        assert model_path.exists()


def test_load_model():
    test_variable = 10
    mock_model = MockModel(test_variable)
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        model_path = Path(tmpdirname) / "model.pkl"
        save_model(mock_model, model_path)
        reloaded_model = load_model(model_path)
        assert reloaded_model.variable == test_variable


def test_model_fit(train_features):
    model = RandomForestModel(
        categorical_features=["career"],
        label="label"
    )

    assert model._encoder is None
    assert model._lb is None
    model.fit(train_features)
    assert model._encoder is not None
    assert model._lb is not None


def test_model_predict(train_features, test_features):
    model = RandomForestModel(
        categorical_features=["career"],
        label="label"
    )

    model.fit(train_features)
    labels = model.predict(test_features)
    assert (labels == ["medium", "high"]).all()
