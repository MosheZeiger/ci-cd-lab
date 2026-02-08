from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Status": "OK"}

@app.get("/hello")
def hello():
    return {"Hello": "World"}

@app.get("/health")
def health():
    return {"Health": "Healthy"}
