import os

from fastapi import Header, HTTPException


async def verify_api_key(
    x_api_key: str = Header(None)
):
    expected = os.getenv("MCP_API_KEY")

    if x_api_key != expected:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )