import pandas as pd
from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.preprocessing import LabelBinarizer

from salary_analyser.algorithm.models.model import RandomForestModel


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels.
    preds : np.array
        Predicted labels.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    lb = LabelBinarizer()
    y_true_binary = lb.fit_transform(y)
    y_pred_binary = lb.transform(preds)

    fbeta = fbeta_score(y_true_binary, y_pred_binary, beta=1, zero_division=1)
    precision = precision_score(y_true_binary, y_pred_binary, zero_division=1)
    recall = recall_score(y_true_binary, y_pred_binary, zero_division=1)
    return precision, recall, fbeta


def slice_analysis(
    model: RandomForestModel, 
    dataframe: pd.DataFrame, 
    feature_name: str
    ) -> pd.DataFrame:
    """
    Segments the dataframe by each unique value in the feature_name and 
    calcualtes the precision, recall and fbeta

    Parameters
    ----------

    Returns
    -------
    
    """
    results_dict = dict()
    for cls in dataframe[feature_name].unique():
        df_temp = dataframe[dataframe[feature_name] == cls]
    
        y_true = df_temp["salary"]
        test = df_temp.drop("salary", axis=1)
        
        y_pred = model.predict(test)
        precision, recall, fbeta = compute_model_metrics(y_true.values, y_pred)
    
        results_dict[cls] = dict(precision=precision, recall=recall, fbeta=fbeta)
    
    df_results = pd.DataFrame.from_dict(results_dict, orient="index").sort_values("fbeta")

    return df_results.round(2)
