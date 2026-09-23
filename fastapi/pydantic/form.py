from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class userform(BaseModel):
  name:str
  password:str


@app.post("/userdata")
def userdata(data:Annotated[userform,Form()]):
  return data