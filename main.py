# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/Testing")
def read_root():
    return {"message": "Hello, FastAPI from Windows!"}
