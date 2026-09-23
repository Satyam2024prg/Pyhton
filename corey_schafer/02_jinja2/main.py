from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

templates = Jinja2Templates(directory="templates")

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

@app.get("/")
def home(request:Request):
  return templates.TemplateResponse(request,"home.html",{"posts":posts, "title" : "Home"})

@app.get("/get_posts")
def get_posts():
  return {
    "message" : "List of Posts",
    "Posts" : posts
  }