from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
  return {"message":"Home Page"}

@app.get("/user/{user_id}")
def user(user_id:int):
  return {"user":user_id}