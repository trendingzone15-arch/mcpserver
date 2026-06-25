from fastapi import FastAPI
from pydantic import BaseModel
from mcp.server.fastmcp import FastMCP

from app.tools.health import ping
from app.tools.tracking import get_tracking
from app.tools.orders import get_order_summary

# MCP
mcp = FastMCP("Divine Vision MCP Server")
mcp.tool()(ping)
mcp.tool()(get_tracking)
mcp.tool()(get_order_summary)

# FastAPI app
api = FastAPI(title="Divine Vision MCP API")

class ExecuteToolRequest(BaseModel):
    name: str
    args: dict = {}

@api.get("/health")
async def health():
    return {
        "success": True, 
        "message": "MCP API running"
        }

@api.get("/tools")
async def list_tools():
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
                    "slug":{"type":"string"}
                },
                "required": ["tracking_number","slug"]
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

@api.post("/execute")
async def execute_tool(payload: ExecuteToolRequest):
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