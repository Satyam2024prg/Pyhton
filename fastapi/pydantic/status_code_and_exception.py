from fastapi import FastAPI,status, HTTPException

app = FastAPI()

@app.get('/users',status_code=status.HTTP_200_OK)
def users():
  return {
    "message":"User data fetched",
    "data" : {
      "name": "Raj",
      "age":29
    }
  }

@app.get("/user/{user_id}")
def user(user_id:int):
  if user_id != 1:
      raise HTTPException(
        status_code=404,
        detail="User not found"
      )
  return{
     user_id : 1,
     "Name" : "Raj"
  }