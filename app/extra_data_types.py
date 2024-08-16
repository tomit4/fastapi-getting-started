from datetime import datetime, time, timedelta
from typing import Annotated, TypedDict, Union
from uuid import UUID

from fastapi import Body, FastAPI


class ItemResponseDict(TypedDict):
    item_id: UUID
    start_datetime: Annotated[datetime, Body()]
    end_datetime: Annotated[datetime, Body()]
    process_after: Annotated[timedelta, Body()]
    repeat_at: Union[time, None]
    start_process: datetime
    duration: timedelta


app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
) -> ItemResponseDict:
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
