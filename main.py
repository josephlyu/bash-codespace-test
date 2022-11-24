from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/add/{num1}/{num2}')
async def add(num1: int, num2: int) -> int:
    '''Add two numbers together.'''
    return {'total': num1+num2}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

