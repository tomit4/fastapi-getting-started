from typing import Annotated, Any

from fastapi import FastAPI, Form

app = FastAPI()


# Forms, uses python-multipart
# NOTE: When you need to receive form fields instead of JSON, use `Form`
#  Uses HTML forms(<form></form>) that uses "special" encoding different from JSON
@app.post("/login/")
async def login(
    username: Annotated[str, Form()], password: Annotated[str, Form()]
) -> dict[str, Any]:
    return {"username": username}
