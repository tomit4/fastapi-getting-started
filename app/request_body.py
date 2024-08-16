from pydantic import BaseModel

from fastapi import FastAPI


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


# Use the model
@app.post("/items/")
async def create_item(item: Item):
    item = Item(name="Chair", description="An object for sitting", price=25.04, tax=1.4)
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Request body + path parameters
@app.put("/items/item_id")
async def update_item(item_id: int, item: Item):
    item = Item(name="Chair", description="An object for sitting", price=25.04, tax=1.4)
    return {"item_id": item_id, **item.model_dump()}


# Request body + path + query parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    item = Item(name="Foo", description="the pretender", price=42.1, tax=3.14)
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
