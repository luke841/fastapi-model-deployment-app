import joblib 
from sklearn.ensemble import RandomForestClassifier
from salary_analyser.algorithm.data import process_data
from salary_analyser.algorithm.settings.settings import (
    MODEL_CATEGORICAL_COLUMNS, 
    MODEL_LABEL_COLUMN,
)


def save_model(model, path):
    joblib.dump(model, path)


def load_model(path):
    return joblib.load(path)


class RandomForestModel:
    def __init__(
        self, 
        categorical_features=MODEL_CATEGORICAL_COLUMNS, 
        label=MODEL_LABEL_COLUMN,
    ):
        self._model = RandomForestClassifier()
        self._encoder = None
        self._lb = None
        self.categorical_features = categorical_features
        self.label = label

    def fit(self, features):
        X_train, y_train, self._encoder, self._lb = process_data(
            features, 
            categorical_features=self.categorical_features, 
            label=self.label, 
            training=True
        )
        self._model.fit(X_train, y_train)

    def predict(self, features):
        X_train, _, _, _ = process_data(
            features, 
            categorical_features=self.categorical_features, 
            label=self.label, 
            encoder=self._encoder,
            lb=self._lb,
            training=False,
        )
        return self._model.predict(X_train)
