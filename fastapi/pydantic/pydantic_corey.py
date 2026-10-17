from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, ValidationError, Field, SecretStr, EmailStr, HttpUrl
from datetime import datetime
app = FastAPI()

class User(BaseModel):
  uid:int
  username:str
  email:EmailStr
  passsword:SecretStr
  website:HttpUrl | None = None
  age:Annotated[int,Field(ge=13, le=150)]
  fullname:str | None = None
  is_active: bool = True
  skills:list[str] = Field(default_factory=list)
  verified_at:datetime | None = None


user = User(uid=1,username="Raju",email="raju@gmail.com")
print(user)
print(user.username)