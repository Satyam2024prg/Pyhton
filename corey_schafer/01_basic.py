from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts:list[dict] = [
  {
    "id" : 1,
    "author" : "John",
    "title"  : "color",
    "content" : "This is about colors",
    "date_posted" : "22/09/2026"
  },
  {
      "id" : 2,
      "author" : "Smith",
      "title"  : "Bird",
      "content" : "This is about Birds",
      "date_posted" : "22/09/2026"
    }
]

@app.get("/",response_class=HTMLResponse)
def home():
  return f"<h1>{posts}</h1>"

@app.get("/get_posts")
def get_posts():
  return {
    "message" : "List of Posts",
    "Posts" : posts
  }