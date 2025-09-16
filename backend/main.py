from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    language: str = "en"   # "en" or "hi"

@app.get("/")
def root():
    return {"message": "Groundwater Chatbot API is running"}
