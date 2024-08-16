from typing import Annotated, Any

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None) -> dict[str, Any]:
    # NOTE: Actually looks for a cookie name "ads_id" in the request object's "Cookie" header
    # Analaogous to request.COOKIES in django and other backend frameworks
    return {"ads_id": ads_id}
