# NOTE: uses python-multipart
from typing import Annotated, Any

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]) -> dict[str, Any]:
    if not file:
        return {"message": "No File sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile) -> dict[str, Any]:
    # NOTE: if you await this like suggested in the tutorial,
    # PyRight will complain that "bytes is not awaitable"
    #  contents = file.file.read()
    #  print("contents :=>", contents)
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
