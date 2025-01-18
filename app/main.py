#!/usr/bin/python
"""Main module for the FastAPI application."""

import os

from dotenv import load_dotenv
from fastapi import FastAPI

# Load the environment variables
load_dotenv()

# Create the FastAPI app
app = FastAPI()

# Environment variables
WEBHOOK_VERIFY_TOKEN = os.getenv("WEBHOOK_VERIFY_TOKEN")
GRAPH_API_TOKEN = os.getenv("GRAPH_API_TOKEN")


@app.get("/")
async def root() -> dict:
    """Return a simple message.

    Returns:
        dict: A simple message.

    """
    return {"message": "Hello World"}


@app.get("/get-env-vars")
async def get_env_vars() -> dict:
    """Return the environment variables.

    Returns:
        dict: The environment variables.

    """
    return {
        "webhook_verify_token": WEBHOOK_VERIFY_TOKEN,
        "graph_api_token": GRAPH_API_TOKEN,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict:
    """Return the item_id and query parameter.

    Returns:
        dict: The item_id and query parameter.

    """
    return {"item_id": item_id, "q": q}
