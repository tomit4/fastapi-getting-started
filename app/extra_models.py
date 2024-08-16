from typing import TypedDict, Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str) -> str:
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn) -> UserInDB:
    hashed_password = fake_password_hasher(user_in.password)
    # NOTE: model.dump() returns a dict of the user_in prototype (based off the UserIn model)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


# NOTE: The UserOut model restricts the sending of the hashed password back to the client
@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn) -> UserInDB:
    user_saved = fake_save_user(user_in)
    return user_saved
