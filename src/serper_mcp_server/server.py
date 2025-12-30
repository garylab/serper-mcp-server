from dotenv import load_dotenv

load_dotenv()

from typing import Any, List, Sequence
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
import json
import asyncio

from .core import google, scape, SERPER_API_KEY, deep_research
from .enums import SerperTools
from .schemas import (
    SearchRequest,
    MapsRequest,
    ReviewsRequest,
    ShoppingRequest,
    LensRequest,
    AutocorrectRequest,
    PatentsRequest,
    WebpageRequest,
    DeepResearchRequest
)


server = Server("Serper")

google_request_map = {
    SerperTools.GOOGLE_SEARCH: SearchRequest,
    SerperTools.GOOGLE_SEARCH_IMAGES: SearchRequest,
    SerperTools.GOOGLE_SEARCH_VIDEOS: SearchRequest,
    SerperTools.GOOGLE_SEARCH_PLACES: AutocorrectRequest,
    SerperTools.GOOGLE_SEARCH_MAPS: MapsRequest,
    SerperTools.GOOGLE_SEARCH_REVIEWS: ReviewsRequest,
    SerperTools.GOOGLE_SEARCH_NEWS: SearchRequest,
    SerperTools.GOOGLE_SEARCH_SHOPPING: ShoppingRequest,
    SerperTools.GOOGLE_SEARCH_LENS: LensRequest,
    SerperTools.GOOGLE_SEARCH_SCHOLAR: AutocorrectRequest,
    SerperTools.GOOGLE_SEARCH_PATENTS: PatentsRequest,
    SerperTools.GOOGLE_SEARCH_AUTOCOMPLETE: AutocorrectRequest,
}


@server.list_tools()
async def list_tools() -> List[Tool]:
    tools = []

    for k, v in google_request_map.items():
        tools.append(
            Tool(
                name=k.value,
                description="Search Google for results",
                inputSchema=v.model_json_schema(),
            ),
        )

    tools.append(Tool(
        name=SerperTools.WEBPAGE_SCRAPE,
        description="Scrape webpage by url",
        inputSchema=WebpageRequest.model_json_schema(),
    ))

    tools.append(Tool(
        name=SerperTools.DEEP_RESEARCH.value,
        description="Performs a deep dive by searching 3 distinct angles (General, Technical, Reddit) in parallel and aggregating unique results.",
        inputSchema=DeepResearchRequest.model_json_schema(),
    ))

    return tools

@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    if not SERPER_API_KEY:
        return [TextContent(text=f"SERPER_API_KEY is empty!", type="text")]

    try:
        # Handle Deep Research tool
        if name == SerperTools.DEEP_RESEARCH.value:
            request = DeepResearchRequest(**arguments)
            result = await deep_research(request)
            return [TextContent(text=json.dumps(result, indent=2), type="text")]

        if name == SerperTools.WEBPAGE_SCRAPE.value:
            request = WebpageRequest(**arguments)
            result = await scape(request)
            return [TextContent(text=json.dumps(result, indent=2), type="text")]

        if not SerperTools.has_value(name):
            raise ValueError(f"Tool {name} not found")

        tool = SerperTools(name)
        request = google_request_map[tool](**arguments)
        result = await google(tool, request)
        return [TextContent(text=json.dumps(result, indent=2), type="text")]
    except Exception as e:
        return [TextContent(text=f"Error: {str(e)}", type="text")]


async def main():
    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options)

if __name__ == "__main__":
    asyncio.run(main())
