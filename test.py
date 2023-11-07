from fastapi.testclient import TestClient
from app import app
from fastapi import status

data = {
    "age": 20,  
    "job": "student",
    "marital": "single",
    "education": "secondary",
    "default": "no",
    "housing": "no",
    "balance": 502, 
    "previous": 0,  
    "loan": "no",
    "contact": "cellular",
    "day": 30,
    "month": "apr",
    "duration": 261,  
    "campaign": 1,
    "pdays": -1,  
    "poutcome": "unknown"
}

client=TestClient(app=app)

def test_index_returns_correct():
    response = client.post("/predict_loan", json=data), 
    assert response.status_code == status.HTTP_201_CREATED
    print(response.json())