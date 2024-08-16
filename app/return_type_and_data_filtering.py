from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user


# As you can see this is better than the example in
# response_model_return_type.py.

# Instead of filtering out two very similar classes,
# we instead EXTEND the BaseUser class to the UserIn
# class, adding only the password. Thusly our UserIn
# class has all the fields of BaseUser along with a
# password field, but by returning the BaseUser,
# we can still look for the needed fields of username,
# email, and full_name
