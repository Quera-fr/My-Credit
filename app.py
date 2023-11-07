from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import numpy as np
import pandas as pd
import requests as request

app = FastAPI()

class LoanRequest(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    housing: str 
    balance: int
    previous: int
    loan: str  
    contact: str
    day: int
    month: str
    duration: int
    campaign: int
    pdays: int
    poutcome: str

class LoanResponse(BaseModel):
    prediction: str

# Load the trained model
model = joblib.load('./pipe.sav')

@app.post('/predict_loan')
async def predict_loan(input_data: LoanRequest):
    # Prepare the input data for prediction

    input_data = dict(input_data)
    df = pd.DataFrame(input_data, index=[0])
    
    # Make predictions using the trained model
    prediction = model.predict(df)[0]
    
    # Map prediction to loan status
    prediction_result = "Prêt Accordé" if prediction == "yes" else "Prêt Réfusé"
    
    return {"prediction": prediction_result}

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=4000)
