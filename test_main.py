from fastapi.testclient import TestClient
from main import app
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

# def test_index():
#     response = client.get("/")

#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {"message":"Hello world"}

def test_index_returns_correct():
    response = client.post("/predict_loan", json=data), 
    assert response[0].status_code == status.HTTP_200_OK