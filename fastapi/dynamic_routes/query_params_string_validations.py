from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  name: str
  age: int
  nation:str
  lang:str

@app.get("/user/{name}")
def user(name,age:int,nation="India",lang:str|None = None):
  if lang is not None:
    return {
      "name" : name,
      "nation" : nation,
      "lang" : lang,
      "age" : age
    }
  return {
    "name" : name,
    "nation" : nation,
    "age" : age
  }