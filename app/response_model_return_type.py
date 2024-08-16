from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="plumbus", price=32.0),
    ]


# Don't do this in production!
# (i.e. send back the user data with password in plain text)
@app.post("/user/")
async def create_user_bad(user: UserIn) -> UserIn:
    return user


# Better, by declaring a separate model, UserOut,
# that doesn't include the user's password, we can
# take a UserIn with the password, and return the UserOut,
# which has the same data, but without the password field
# included due to the restriction of declaring our `response_model`
@app.post("/user/", response_model=UserOut)
async def create_user_good(user: UserIn) -> Any:
    return user


# But this is still somewhat less ergonomic than what we want,
# plus the type checkings of our editors can't work well with
# the Any type, see return_type_and_data_filtering.py for a
# better solution to filtering data.
