from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import numpy as np
import pandas as pd

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
model = joblib.load('/home/diaby/IA_EXOS/Appli_Heroku/Prediction_bancaire/foret.sav')

# Load the scaler used during model training
scaler = joblib.load('/home/diaby/IA_EXOS/Appli_Heroku/Prediction_bancaire/transformer.pkl')

@app.post('/predict_loan', response_model=LoanResponse)
async def predict_loan(request: LoanRequest):
    # Prepare the input data for prediction
    input_data = [[request.age, request.job, request.marital, request.education,
                   request.default, request.housing, request.balance, request.previous,
                   request.loan, request.contact, request.day, request.month, request.duration,
                   request.campaign, request.pdays,request.poutcome, request.poutcome]]
    
    # Scale the input data using the loaded scaler       scaled_input_data = 
    scaled_input_data= scaler.transform(pd.DataFrame(input_data, index=[0]))
    print(scaler.transform(input_data)[:-1])
    
    # Make predictions using the trained model
    prediction = model.predict(scaled_input_data)[0]
    
    # Map prediction to loan status
    prediction_result = "Loan Approved" if prediction == 1 else "Loan Denied"
    
    return {"prediction": prediction_result}

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
