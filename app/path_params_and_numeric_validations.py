from typing import Annotated, Any

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
    size: Annotated[float, Query(gt=0, lt=10.5)] = 0.0,
):
    results: dict[str, Any] = {"item_id": item_id}
    # Note: You can ASSIGN the size to larger than 10.5,
    # but the param cannot have an input greater than 10.5 for size
    size = 3.25
    if q:
        results.update({"q": q})
        print(f"the size is {size}")
    return results
