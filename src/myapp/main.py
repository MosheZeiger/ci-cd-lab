from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Status": "OK"}

@app.get("/hello")
def hello():
    return {"Hello": "Worldd"}

