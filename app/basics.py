from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


# First Steps
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    # still can only be "resnet" to get this:
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Query Parameters

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


#  http://127.0.0.1:8000/items/?skip=0&limit=10
#  @app.get("/items/")
#  async def read_item(skip: int = 0, limit: int = 10):
#  return fake_items_db[skip : skip + limit]


# Optional Parameters
#  @app.get("/items/{item_id}")
#  async def read_item(item_id: str, q: str | None = None):
#  if q:
#  return {"item_id": item_id, "q": q}
#  return {"item_id": item_id}


# Query parameter type conversion
#  http://127.0.0.1:8000/items/foo?short=1
#  @app.get("/items/{item_id}")
#  async def read_item(item_id: str, q: str | None = None, short: bool = False):
#  item = {"item_id": item_id}
#  if q:
#  item.update({"q": q})
#  if not short:
#  item.update(
#  {"description": "this is an amazing item that has a long description"}
#  )
#  return item


# Multiple path and query parameters
#  @app.get("/users/{user_id}/items/{item_id}")
#  async def read_user_item(
#  user_id: int, item_id: str, q: str | None = None, short: bool = False
#  ):
#  item = {"item_id": item_id, "owner_id": user_id}
#  if q:
#  item.update({"q": q})
#  if not short:
#  item.update(
#  {"description": "This is an amazing item that has a long description"}
#  )
#  return item


# Required query parameters
#  @app.get("/items/{item_id}")
#  async def read_user_item(item_id: str, needy: str):
#  item = {"item_id": item_id, "needy": needy}
#  return item


#  In this case, there are 3 query parameters:
#  -needy, a required str.
#  -skip, an int with a default value of 0.
#  -limit, an optional int.
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
