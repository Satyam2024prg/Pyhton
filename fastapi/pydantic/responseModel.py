from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  name : str
  age : int
  password : int

class ResponseModel(BaseModel):
  name : str
  age : int

@app.get("/users",response_model=ResponseModel)
def users():
  return{
    "name" : "Shyam",
    "age" : 24,
    "password" : 1234
  }