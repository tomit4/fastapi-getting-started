from typing import Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", tags=["items"])
async def read_items() -> list[dict[str, Any]]:
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users() -> list[dict[str, str]]:
    return [{"username": "johndoe"}]


# OpenAPI greys out this route and marks it as "Warning: Deprecated"
@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements() -> list[dict[str, str]]:
    return [{"item_id": "Foo"}]
