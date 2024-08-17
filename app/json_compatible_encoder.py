from datetime import date, datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


# Essentially encodes non-JSON structures (like datetime) into JSON structures (like str)
@app.put("/items/{id}")
def update_item(id: str, item: Item) -> None:
    json_ccompatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_ccompatible_item_data
