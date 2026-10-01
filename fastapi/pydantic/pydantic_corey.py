from fastapi import FastAPI

from pydantic import BaseModel, ValidationError, Field

app = FastAPI()

class User(BaseModel):
  uid:int
  username:str
  email:str
  fullname:str | None = None
  is_active: bool = True
  skills:list[str] = Field(default_factory=list)


user = User(uid=1,username="Raju",email="raju@gmail.com")
print(user)
print(user.username)