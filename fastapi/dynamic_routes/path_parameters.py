from fastapi import FastAPI,Path
from typing import Annotated

app = FastAPI()

@app.get("/")
def home():
  return {"message":"Home Page"}

@app.get("/user/{user_id}{age}")
def user(user_id:int,age:Annotated[int,Path(title="Age Required", gt=0 , le=150)]):
  return {"user":user_id , "age" : age}