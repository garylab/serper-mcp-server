from typing import Optional, Dict, Any, List, Sequence
import os
from enum import StrEnum
from pydantic import BaseModel, Field
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from dotenv import load_dotenv
import json
import aiohttp
import ssl
import certifi

load_dotenv()

server = Server("Serper")

class SerperTools(StrEnum):
    GOOGLE_SEARCH = "google_search"


class GoogleSearchRequest(BaseModel):
    q: str = Field(..., description="The query to search for")
    gl: Optional[str] = Field(None, description="The country to search in, e.g. us, uk, ca, au, etc.") 
    location: Optional[str] = Field(None, description="The location to search in, e.g. San Francisco, CA, USA")
    hl: Optional[str] = Field(None, description="The language to search in, e.g. en, es, fr, de, etc.")
    tbs: Optional[str] = Field(None, description="The time period to search in, e.g. d, w, m, y")
    num: Optional[int] = Field(10, max=100, description="The number of results to return, max is 100")
    page: Optional[int] = Field(1, min=1, description="The page number to return, first page is 1")


async def google_search(request: GoogleSearchRequest) -> Dict[str, Any]:
    url = "https://google.serper.dev/search"

    payload = request.model_dump(exclude_none=True)
    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.post(url, headers=headers, json=payload) as response:
            response.raise_for_status()
            return await response.json()


@server.list_tools()
async def list_tools() -> List[Tool]:
    return [
        Tool(
            name=SerperTools.GOOGLE_SEARCH,
            description="Search Google for a query",
            inputSchema=GoogleSearchRequest.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    try:
        if name == SerperTools.GOOGLE_SEARCH.value:
            request = GoogleSearchRequest(**arguments)
            result = await google_search(request)
            return [TextContent(text=json.dumps(result, indent=2), type="text")]
        else:
            raise ValueError(f"Tool {name} not found")
    except Exception as e:
        return [TextContent(text=f"Error: {str(e)}", type="text")]


async def main():
    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options)
