from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Page qui pousse"
)

def r(n):
    return (n/2)

@app.get("/square")
def square(n: str=None):
    if n == None:  
        return "Please enter a number"
    n = int(n)
    return int(n*n)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
