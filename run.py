from fastapi import FastAPI
import uvicorn


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
