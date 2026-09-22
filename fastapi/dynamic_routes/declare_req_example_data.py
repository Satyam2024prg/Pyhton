from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
  name:str
  price:int = Field(gt=0)
  description:str
  model_config = {
    'json_schema_extra':{
      "examples":[
        {
          "name" : "Foo",
          "price" : 100,
          "description" : "Foo is an item"
        }
      ]
    }
  }

@app.put("/items/{item_id}")
def items(item_id:int, item:Item):
  return {
    "message" : "Items",
    "Item id" : item_id,
    "Item" : item
  }