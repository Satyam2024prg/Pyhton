from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
  id:int
  name:str
  age:int

TODO = []

@app.post("/create_todo")
def create_todo(todo:Todo):
  TODO.append(todo)
  return {
    "message" : "todo created"
  }


@app.get("/get_todos")
def get_todos():
  return {
    "message" : "Todo",
    "TODO" : TODO
  }


@app.get("/get_todo{user_id}")
def get_todo(user_id:int):
  for todo in TODO:
    if todo.id == user_id:
      return todo
  return {
    "message" : "Error! Todo not found"
  }

@app.put("/update_todo")
def update_todo(user_id:int, todo:Todo):
  for index,todo in enumerate(TODO):
    if todo.id ==  user_id:
      TODO[index] = todo
      return {
        "message" : "Todo Updated",
        "Todo"  : todo
      }
  return {
    "message" : "Error! todo not found"
  }