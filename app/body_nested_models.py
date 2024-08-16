from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


# image is a nested Image dictionary within Item
# images is a nested list of Image dictionaries
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags_list: list[str] = []
    tags_set: set[str] = set()
    image: Image | None = None
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item) -> dict[str, Any]:
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers/")
async def create_offer(offer: Offer) -> Offer:
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]) -> list[Image]:
    for image in images:
        # pydanatic has full editor support
        print(f"{image.url}")
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]) -> dict[int, float]:
    return weights
