from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class User(BaseModel):
  name: str
  string : str
  nation:str
  lang:str

@app.get("/user/{name}")
def user(name,string:Annotated[str,Query(min_length=10)],nation="India",lang=None):
  if lang is not None:
    return {
      "name" : name,
      "nation" : nation,
      "lang" : lang,
      "str" : string
    }
  return {
    "name" : name,
    "nation" : nation,
    "str" : string
  }