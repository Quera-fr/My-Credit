from fastapi import FastAPI
import uvicorn
import pandas as pd
import joblib
from pydantic import BaseModel

transformer = joblib.load("transformer.pkl")
foret = joblib.load("foret.sav")

app = FastAPI(
    title="Page qui pousse"
)

@app.get("/")
def racine():
    return "Bonjour monde"

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}

class InputData(BaseModel):
    n: int

@app.get("/d")
def r(n):
    n = int(n)
    return (n/2)

@app.post("/di")
def r(s: InputData):
    return (s.n/2)

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


@app.post("/prediction")
def prediction(dictionnaire: LoanRequest):
    df = pd.DataFrame(dictionnaire, index=[0])
    df = transformer.transform(df)
    pred = foret.predict(df)
    return {"prediction": pred}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)