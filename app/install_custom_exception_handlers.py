from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(
    request: Request, exc: UnicornException
) -> JSONResponse:
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! {exc.name} did something. There goes a rainbow...did I mention I'm a teapot?"
        },
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
