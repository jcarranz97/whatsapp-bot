#!/usr/bin/python3
"""Main module for the FastAPI application."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """Return a simple message.

    Returns:
        dict: A simple message.

    """
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict:
    """Return the item_id and query parameter.

    Returns:
        dict: The item_id and query parameter.

    """
    return {"item_id": item_id, "q": q}
