from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    # Either way, you're rick-rolled...
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


# Annotate a Response Subclass
@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# Invalid Return Type Annotations
# NOTE: This fails because the type annotation is not a Pydantic
# type and is not just a single Response class or subclass, it's a
# union (any of the two) between a Response and a dict.
@app.get("/portal")
async def get_portal_failure(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}


# HOWEVER, you can fix this by defining the response_model as None
@app.get("/portal", response_model=None)
async def get_portal_acceptable(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}


# Response Model encoding patterns


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


# NOTE: the response_model_exclude_unset flag will
# omit values that have not been set in the response.
# This is useful if you have a large amount of `null` values in a DB return
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


# Response Model Include and Response Model Exclude
# NOTE: essentially take a `set` of `str` values and
# ensures that they are always included
# or always excluded from the response
# NOTE, if you assign either response_model_include or
# response_model_exclude to lists instead of sets, it
# will still (converting them to sets under the hood)
@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]
