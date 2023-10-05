from fastapi import FastAPI
import uvicorn

<<<<<<< HEAD

app = FastAPI(
	title='my first API',
	description=""" description détaillée 
					de l'application""")
					

@app.get('/square')

def square(n:str=None):
	if n == None:return "Please enter a number"
	else:return int(n)*int(n)
	
if __name__=='__main__':
	uvicorn.run(app, host='127.0.0.1', port=8000)
=======
app = FastAPI(
    title="Page qui pousse"
)



@app.get("/square")
def square(n: str=None):
    if n == None:  
        return "Please enter a number"
    n = int(n)
    return int(n*n)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
>>>>>>> 5dfca4b7fbea75ee256a1ae0fa7a9adbfa767376
