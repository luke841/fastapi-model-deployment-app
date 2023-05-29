from fastapi import FastAPI
import pandas as pd

from salary_analyser.algorithm.data import CensusRecord, InferenceResult
from salary_analyser.algorithm.models import load_model
from salary_analyser.algorithm.settings.settings import DEFAULT_MODEL_PATH


app = FastAPI()
model = load_model(DEFAULT_MODEL_PATH)

@app.get("/")
def index():
    return {"greetings": "pass the inference request to '/inference'"}


@app.post("/inference")
def inference(record: CensusRecord) -> InferenceResult:
    """
    Passes inference to the model

    """
    employment_details = pd.DataFrame([record.dict()])
    employment_details = employment_details.drop("salary", axis=1)
    predicted_salary = model.predict(employment_details)

    if len(predicted_salary) > 1:
        raise RuntimeError(
            "Model prediction returned more "
            f"than {len(predicted_salary)} predictions"
            )
    
    inference_result = InferenceResult(salary=predicted_salary[0])
    return inference_result
