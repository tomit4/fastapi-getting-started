from typing import Annotated

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str | None = None) -> str | None:
    return q


# NOTE: the `use_cache` flag should only be used if you DON'T want
# the dependencies return value to be cached when utilized in the route
# (i.e. setting it to False, defaults to True)
def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor, use_cache=False)],
    last_query: Annotated[str | None, Cookie()] = None,
) -> Annotated[str | None, Cookie()]:
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
) -> dict[str, Annotated[str | None, Cookie()]]:
    return {"q_or_cookie": query_or_default}
