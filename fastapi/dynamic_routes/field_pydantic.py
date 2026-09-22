from fastapi import FastAPI ,Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
  name : str
  description : str | None = Field(default=None ,title="Description of item " ,max_length=300)
  price : int = Field(gt=0, title="Price of the item must be greater than 0 ")  


@app.put("/items/{item_id}")
def items(item_id:int,item:Annotated[Item,Body(embed=True)]):
  results = {
    "item id" : item_id,
    "item": item
  }
  return results