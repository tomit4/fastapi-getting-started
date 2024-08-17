from typing import Annotated, Any

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(
    q: str | None = None, skip: int = 0, limit: int = 100
) -> dict[str, Any]:
    return {"q": q, "skip": skip, "limit": limit}


CommonDeps = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_items(commons: CommonDeps) -> dict[str, Any]:
    return commons


@app.get("/users/")
async def read_users(commons: CommonDeps) -> dict[str, Any]:
    return commons
