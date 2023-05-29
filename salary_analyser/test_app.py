# TODO: get this to run in the tests/ folder


import json

from fastapi.testclient import TestClient

from salary_analyser.main import app

client = TestClient(app)


def test_index():
    r = client.get("/")
    print(r.json())
    assert r.json() == {"greetings": "pass the inference request to '/inference'"}

def test_inference():
    record = {
        'age': 39,
        'workclass': 'State-gov',
        'fnlgt': 77516,
        'education': 'Bachelors',
        'education-num': 13,
        'marital-status': 'Never-married',
        'occupation': 'Adm-clerical',
        'relationship': 'Not-in-family',
        'race': 'White',
        'sex': 'Male',
        'capital-gain': 2174,
        'capital-loss': 0,
        'hours-per-week': 40,
        'native-country': 'United-States',
 }
    
    data = json.dumps(record)
    r = client.post("/inference", data=data)
    assert r.json() == {'salary': '<=50K'}
