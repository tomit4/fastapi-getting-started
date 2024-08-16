from typing import Annotated, Any

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    user_agent: Annotated[str | None, Header()] = None
) -> dict[str, Any]:
    return {"User-Agent": user_agent}


@app.get("/items/")
async def read_items_with_duplicate_headers(
    x_token: Annotated[list[str] | None, Header()] = None
) -> dict[str, Any]:
    return {"X-Token values": x_token}
