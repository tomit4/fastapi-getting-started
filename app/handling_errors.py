from typing import Any

from fastapi import FastAPI, HTTPException

app = FastAPI()

items: dict[str, str] = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str) -> dict[str, Any]:
    if item_id not in items:
        # NOTE: Normally headers aren't strictly necessary
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}
