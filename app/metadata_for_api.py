from typing import Any

from fastapi import FastAPI

description = """
ChimichangApp helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title="ChimichangApp",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",  # alternative to url:
        # "identifier": "MIT",
    },
    openapi_tags=tags_metadata,
    # Default OpenAPI schema. You can set your own if so desired
    #  openapi_url="/openapi.json"
    # Default docs and redoc url, you can change it, or set it to None to disable OpenAPI
    # docs_url="/docs",
    # redoc_url="/redoc"
)


@app.get("/users/", tags=["users"])
async def get_users() -> list[dict[str, Any]]:
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.get("/items/")
async def read_items() -> list[dict[str, Any]]:
    return [{"name": "wand"}, {"name": "flying broom"}]
