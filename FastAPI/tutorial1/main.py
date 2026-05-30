from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
items = []

class Item(BaseModel):
    text: str
    is_done: bool = False




@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def read_items(item_id: int):
    if item_id == 00:
        return items
    if item_id <= len(items):
        return {"item_id": items[item_id]}
    else: 
        raise HTTPException(status_code=404, detail="Item  {item_id} not found")




