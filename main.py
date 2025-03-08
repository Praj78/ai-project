from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import List,Optional

app = FastAPI()

items=[]

class Item(BaseModel):
    id:int
    name:str
    description:Optional[str]=None
    price:float

@app.post("/items/",response_model=Item)
def create_item(item:Item):
    for existing_item in items:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400,detail="Item with this id already exists")
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def get_items():
    return items


@app.get("/items/{item_id}",response_model=Item)
def get_item(item_id:int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404,detail="item not found")

@app.put("/items/{item_id}",response_model=Item)
def update_item(item_id:int,updated_item:Item):
    for index,item in enumerate(items):
        if item.id == item_id:
            items[index]=updated_item
            return updated_item
    raise HTTPException(status_code=404,detail='item not found')

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    for index,item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return {"message":"item deleted sucessfully"}  
    raise HTTPException(status_code=404,detail='item not found')
    