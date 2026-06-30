from fastapi import FastAPI
from pydantic import BaseModel

from mcp.server.fastmcp import FastMCP

from app.tools.health import ping
from app.tools.tracking import get_tracking
from app.tools.orders import get_order_summary
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import ALLOWED_ORIGIN
from app.middleware.api_key import verify_api_key
from fastapi import Depends

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request


# MCP
mcp = FastMCP("Divine Vision MCP Server")
mcp.tool()(ping)
mcp.tool()(get_tracking)
mcp.tool()(get_order_summary)

limiter = Limiter(
    key_func=get_remote_address
)

# FastAPI app
api = FastAPI(title="Divine Vision MCP API")
api.state.limiter = limiter
api.add_middleware(SlowAPIMiddleware)
api.add_middleware(
    CORSMiddleware,

    allow_origins=[
        ALLOWED_ORIGIN
    ],

    allow_credentials=True,

    allow_methods=[
        "GET",
        "POST",
    ],

    allow_headers=[
        "Content-Type",
        "Authorization",
    ],
)

class ExecuteToolRequest(BaseModel):
    name: str
    args: dict = {}

@api.exception_handler(RateLimitExceeded)
async def rate_limit_handler(
    request: Request,
    exc: RateLimitExceeded,
):
    return JSONResponse(
        status_code=429,
        content={
            "success": False,
            "message": "Too many requests. Please try again later.",
        },
    )

@api.get("/health")
async def health():
    return {
        "success": True, 
        "message": "MCP API running"
        }

@api.get("/tools")
async def list_tools(
    _: None = Depends(verify_api_key),
):
    return [
        {
            "name": "ping",
            "description": "Health check tool",
            "inputSchema": {
                "type": "object",
                "properties": {},
            },
        },
        {
            "name": "get_tracking",
            "description": "Get shipment tracking details using tracking_number ",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "tracking_number": {"type": "string"},
                },
                "required": ["tracking_number"]
            },
        },
        {
            "name": "get_order_summary",
            "description": "Get order summary using order id",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string"}
                },
                "required": ["order_id"]
            },
        },
    ]

ALLOWED_TOOLS = {
    "ping": ping,
    "get_tracking": get_tracking,
    "get_order_summary": get_order_summary,
}

@api.post("/execute")
@limiter.limit("20/minute")
async def execute_tool(payload: ExecuteToolRequest,request: Request,):

    tool = ALLOWED_TOOLS.get(payload.name)
    
    if payload.name == "ping":
        return await ping()

    if payload.name == "get_tracking":
        return await get_tracking(**payload.args)

    if payload.name == "get_order_summary":
        return await get_order_summary(**payload.args)

    return {
        "success": False,
        "message": f"Unknown tool: {payload.name}"
    }