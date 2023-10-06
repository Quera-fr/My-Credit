import pandas as pd
from pydantic import BaseModel
# source app_heroku/bin/activate

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

input_data = {
    "age": 30,
    "job": "admin.",
    "marital": "married",
    "education": "secondary",
    "default": "no",
    "housing": "yes",
    "balance": 5000.0,
    "previous": 2,
    "loan": "no",
    "contact": "cellular",
    "day": 15,
    "month": "may",
    "duration": 180,
    "campaign": 3,
    "pdays": 15,
    "poutcome": "success"
}

def dictionnaire(input_data:LoanRequest):
    data = dict(input_data)
    df = pd.DataFrame(data, index=[0])
    
    return df

print(dictionnaire(input_data))


