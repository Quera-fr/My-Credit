import unittest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

class TestMyModule(unittest.TestCase):

    def test_predict_loan_accepted(self):
        # Test if the prediction result for an accepted loan is as expected
        input_data = {
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
        response = client.post('/predict_loan', json=input_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"prediction": "Prêt Accordé"})

    def test_predict_loan_rejected(self):
        # Test if the prediction result for a rejected loan is as expected
        input_data = {
            "age": 20,  
            "job": "student",
            "marital": "single",
            "education": "secondary",
            "default": "no",
            "housing": "no",
            "balance": 20, 
            "previous": 2,  
            "loan": "no",
            "contact": "cellular",
            "day": 20,
            "month": "apr",
            "duration": 115,  
            "campaign": 1,
            "pdays": 1,  
            "poutcome": "unknown"
        }
        response = client.post('/predict_loan', json=input_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"prediction": "Prêt Réfusé"})

    # You can add more test functions as needed

if __name__ == '__main__':
    unittest.main()
