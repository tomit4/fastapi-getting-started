from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    item = Item(
        name="Foo",
        description="The pretender",
        price=42.0,
        tax=3.2,
    )
    user = User(
        username="dave",
        full_name="Dave Grohl",
    )
    results = {"item_id": item_id, "item": item, "user": user}
    return results
