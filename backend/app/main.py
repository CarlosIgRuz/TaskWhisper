# Copyright (c) 2025 CarlosIgRuz. MIT License.

from fastapi import FastAPI
from .intent_parser import parse_intent

app = FastAPI()


@app.get("/")
async def health() -> dict:
    """Simple health check endpoint."""
    return {"status": "ok"}


@app.post("/parse_intent")
async def parse_intent_endpoint(payload: dict) -> dict:
    """Parse text from the request body and return the detected intent."""
    text = payload.get("text", "")
    return parse_intent(text)
