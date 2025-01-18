#!/usr/bin/python
"""Main module for the FastAPI application."""

import logging
import os
from typing import Annotated

import requests
from dotenv import load_dotenv
from fastapi import (
    FastAPI,
    HTTPException,
    Query,
)
from pydantic import BaseModel

# Load the environment variables
load_dotenv()

# Create logger and use the uvicorn logger
logger = logging.getLogger("uvicorn")

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
    logger.info("Hello World")
    return {"message": "Hello World"}


@app.get("/get-env-vars")
async def get_env_vars() -> dict:
    """Return the environment variables.

    Returns:
        dict: The environment variables.

    """
    logger.info("Getting environment variables")
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


class WebhookPayload(BaseModel):
    """Webhook payload model."""

    object: str
    entry: list


@app.post("/webhook")
async def handle_webhook(payload: WebhookPayload) -> dict:
    """Handle incoming webhook messages.

    Returns:
        dict: The response status.

    """
    # Log incoming messages
    logger.info("Incoming webhook message: %s", payload.dict())

    # Extract message details
    entry = payload.entry[0]
    changes = entry.get("changes", [{}])
    value = changes[0].get("value", {})
    message = value.get("messages", [{}])[0]

    if message.get("type") == "text":
        business_phone_number_id = value.get("metadata", {}).get("phone_number_id")
        user_message = message.get("text", {}).get("body", "")
        sender_id = message.get("from")
        message_id = message.get("id")

        # Send a reply message
        reply_url = (
            f"https://graph.facebook.com/v18.0/{business_phone_number_id}/messages"
        )
        headers = {"Authorization": f"Bearer {GRAPH_API_TOKEN}"}
        reply_payload = {
            "messaging_product": "whatsapp",
            "to": sender_id,
            "text": {"body": f"Echo Juan: {user_message}"},
            "context": {"message_id": message_id},
        }
        response = requests.post(
            reply_url,
            headers=headers,
            json=reply_payload,
            timeout=10,
        )
        logger.info("Reply sent: %s", response.json())

        # Mark the message as read
        mark_read_payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id,
        }
        requests.post(
            reply_url,
            headers=headers,
            json=mark_read_payload,
            timeout=10,
        )

    return {"status": "success"}


@app.get("/webhook")
async def verify_webhook(
    mode: Annotated[str, Query(..., alias="hub.mode")],
    verify_token: Annotated[str, Query(..., alias="hub.verify_token")],
    challenge: Annotated[str, Query(..., alias="hub.challenge")],
) -> str:
    """Verify that the webhook is working.

    Raises:
        HTTPException: If the webhook is not verified.

    Returns:
        str: The challenge string.

    """
    # Validate the webhook
    if mode == "subscribe" and verify_token == WEBHOOK_VERIFY_TOKEN:
        logger.info("Webhook verified successfully!")
        return challenge
    raise HTTPException(status_code=403, detail="Forbidden")
