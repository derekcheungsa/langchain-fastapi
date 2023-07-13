from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    is_offer: bool = None

# assuming this is our "database"
items_db = {
    "1": {"name": "item1", "description": "This is item 1", "price": 25.0, "is_offer": True},
    "2": {"name": "item2", "description": "This is item 2", "price": 45.0, "is_offer": False},
}

app = FastAPI()

class ItemID(BaseModel):
    id: str

@app.post("/items/")
async def retrieve_item(item_id: ItemID):
    item_id_dict = item_id.dict()
    id = item_id_dict['id']
    if id in items_db:
        return {"message": f"Item retrieved: {items_db[id]['name']}", "data": items_db[id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
