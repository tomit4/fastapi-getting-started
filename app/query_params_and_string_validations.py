from typing import Annotated, Any

from fastapi import FastAPI, Query

app = FastAPI()


# NOTE: q is automatically optional when declared this way
@app.get("/items/")
async def read_items(q: str | None = None):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Additional validation
# Note:
# q: str | None = None
#  is the same as:
# q: Annotated[str | None] = None


@app.get("/items/")
async def read_items_annotated(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None
):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items_regex(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items_default_values(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = "fixedquery"
):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


#  http://localhost:8000/items/?q=foo&q=bar
@app.get("/items")
async def read_items_multiple_values(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


@app.get("/items")
async def read_items_multiple_values_with_list(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items


# returns:
#  {
#    "q": [
#      "foo",
#      "bar"
#    ]
#  }


@app.get("/items/")
async def read_items_with_more_meta_data(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items_with_hyphenated_param(
    q: Annotated[str | None, Query(alias="item-query")] = None
):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items_with_deprecated_params(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items_hide_from_openapi(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not Found"}
