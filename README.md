# Divine Vision MCP Server

An industry-ready **FastAPI + Model Context Protocol (MCP)** server powering the **Divine Vision AI Order Tracking Assistant**.

The MCP Server acts as a secure middleware between the AI Agent and enterprise services. It exposes tools that can be discovered and executed dynamically, enabling the AI assistant to retrieve shipment tracking details, order summaries, and future logistics operations without hardcoding APIs.

---

# Features

- MCP Tool Discovery (`/tools`)
- MCP Tool Execution (`/execute`)
- Shipment Tracking Tool
- Order Summary Tool
- Health Check Endpoint
- Secure API Key Authentication
- Restricted CORS
- Environment Variable Configuration
- Pydantic Request Validation
- Industry Ready Folder Structure
- Easily Extendable Tool Architecture
- FastAPI Async APIs
- HTTPX Async Client
- Production Ready Error Handling

---

# Tech Stack

- Python 3.12+
- FastAPI
- FastMCP
- Pydantic
- HTTPX
- Uvicorn
- python-dotenv

---

# Project Structure

```
mcpserver/
│
├── app/
│   │
│   ├── config/
│   │     └── settings.py
│   │
│   ├── middleware/
│   │     └── api_key.py
│   │
│   ├── schemas/
│   │     └── tracking_schema.py
│   │
│   ├── services/
│   │     └── shipment_service.py
│   │
│   ├── tools/
│   │     ├── tracking.py
│   │     ├── orders.py
│   │     └── health.py
│   │
│   └── main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Architecture

```
                    +----------------------+
                    |      Next.js UI      |
                    +----------+-----------+
                               |
                               |
                               ▼
                    +----------------------+
                    |     Express API      |
                    +----------+-----------+
                               |
                     Gemini Function Calling
                               |
                               ▼
                    +----------------------+
                    |      MCP Server       |
                    +----------+-----------+
                               |
                    Executes Selected Tool
                               |
                               ▼
               Shipment API / Database / ERP
```

---

# Available Tools

## ping

Checks whether the MCP server is running.

### Input

```json
{}
```

### Response

```json
{
  "success": true
}
```

---

## get_tracking

Retrieves shipment tracking information using the tracking number.

### Input

```json
{
    "tracking_number":"DV100000001IN"
}
```

### Response

```json
{
  "success": true,
  "data": {
    "trackingNumber": "DV100000001IN",
    "status": "Reached Hub",
    "estimatedDelivery": "2026-06-28T10:30:00Z",
    "customer": {
      "name": "Customer 1"
    }
  }
}
```

---

## get_order_summary

Retrieves complete order summary using Order ID.

### Input

```json
{
    "order_id":"ORD-202600001"
}
```

---

# API Endpoints

## Health

```
GET /health
```

---

## Discover Tools

```
GET /tools
```

---

## Execute Tool

```
POST /execute
```

Body

```json
{
    "name":"get_tracking",
    "args":{
        "tracking_number":"DV100000001IN"
    }
}
```

---

# Security

The MCP Server is secured using multiple layers.

## API Key Authentication

Every request from the Express Backend must include

```
x-api-key
```

Example

```
x-api-key: your-secret-key
```

Unauthorized requests receive

```
401 Unauthorized
```

---

## Restricted CORS

Only trusted backend origins are allowed.

Example

```
http://localhost:5000
```

Production

```
https://api.divinevision.com
```

---

## Environment Variables

Create a `.env` file.

Example

```env
SHIPMENT_API_BASE_URL=https://YOUR_SHIPMENT_API/api/shipments/
ALLOWED_ORIGIN=http://localhost:5000
MCP_API_KEY=your-secret-api-key
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/mcpserver.git
```

Move into the project

```bash
cd mcpserver
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create environment variables

```bash
cp .env.example .env
```

Run

```bash
uvicorn app.main:api --reload
```

Server

```
http://localhost:8000
```

---

# Integration with Express

Discover tools

```
GET /tools
```

Execute tool

```
POST /execute
```

Headers

```
x-api-key: your-secret-key
```

---

# Adding New Tool

Create a tool

```
app/tools/payment.py
```

Register

```python
mcp.tool()(payment)
```

Expose

```
GET /tools
```

Handle execution

```
POST /execute
```

That's all.

---

# Future Roadmap


- JWT Authentication
- Tool Permissions
- Role Based Access
- Tool Logging
- Tool Metrics
- Distributed Tracing
- Redis Caching
- Retry Policies
- OpenTelemetry
- Docker Support
- Kubernetes Deployment
- Prometheus Metrics
- Grafana Dashboard
- CI/CD Pipeline
- Tool Versioning
- Multi-Tenant Support

---

# Development Guidelines

- Keep tools independent.
- Business logic belongs inside `services`.
- API routes should remain thin.
- Validate all request payloads using Pydantic.
- Never expose secrets in code.
- Store configuration in environment variables.
- Follow async programming practices.

---

# License

MIT License

---

# Author

**Sanket Mane**

Full stack developer
contact - sanketmane0407@gmail.com

AI | Backend | MCP | FastAPI | Next.js | Express.js

---

# Divine Vision

> **See Beyond the Shipment**
>
> AI-powered conversational shipment tracking built on the Model Context Protocol.