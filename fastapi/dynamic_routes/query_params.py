from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  name:str
  age:int

@app.get('/')
def home():
  return {"message":"Home Page"}

# @app.post('/user')
# def user(name:str, age:int):
#   return {
#     "name" : name,
#     "age" : age
#   }

@app.post('/user')
def user(user:User):
  return {
    "message" : "User Data Created",
    "data" : user
  }