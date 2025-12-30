import os
import ssl
from typing import Dict, Any
import certifi
import aiohttp
from pydantic import BaseModel
from .enums import SerperTools
from .schemas import WebpageRequest, SearchRequest, DeepResearchRequest
import asyncio as _asyncio

SERPER_API_KEY = str.strip(os.getenv("SERPER_API_KEY", ""))
AIOHTTP_TIMEOUT = int(os.getenv("AIOHTTP_TIMEOUT", "15"))



async def google(tool: SerperTools, request: BaseModel) -> Dict[str, Any]:
    uri_path = tool.value.split("_")[-1]
    url = f"https://google.serper.dev/{uri_path}"
    return await fetch_json(url, request)


async def scape(request: WebpageRequest) -> Dict[str, Any]:
    url = "https://scrape.serper.dev"
    return await fetch_json(url, request)



async def deep_research(request: DeepResearchRequest) -> list[Dict[str, Any]]:
    query = request.q

    # Generate 3 sub-queries for different search angles
    sub_queries = [
        query,  # General
        f"{query} technical specifications benchmarks",  # Technical
        f"{query} site:reddit.com OR site:hackernews.com",  # Community
    ]

    # Create SearchRequest objects for each sub-query
    search_requests = [SearchRequest(q=sq, num="10") for sq in sub_queries]

    # Fire all 3 requests in parallel using asyncio.gather
    # CRITICAL: return_exceptions=True ensures one failure doesn't crash the batch
    results = await _asyncio.gather(
        *[google(SerperTools.GOOGLE_SEARCH, req) for req in search_requests],
        return_exceptions=True
    )

    # Prune and deduplicate results
    unique_results: Dict[str, Dict[str, Any]] = {}

    for result in results:
        # Skip failed requests (exceptions)
        if isinstance(result, Exception):
            continue

        # Focus ONLY on the "organic" list in the JSON response
        organic = result.get("organic", [])
        
        for item in organic:
            link = item.get("link")
            if link and link not in unique_results:
                # Extract only high-value fields for token economy
                unique_results[link] = {
                    "title": item.get("title"),
                    "link": link,
                    "snippet": item.get("snippet"),
                    "date": item.get("date"),
                }

    # Return pruned, unique list
    return list(unique_results.values())


async def fetch_json(url: str, request: BaseModel) -> Dict[str, Any]:
    payload = request.model_dump(exclude_none=True)
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    timeout = aiohttp.ClientTimeout(total=AIOHTTP_TIMEOUT)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        async with session.post(url, headers=headers, json=payload) as response:
            try:
                response.raise_for_status()
                return await response.json()
            except aiohttp.ClientResponseError as e:
                 # Return empty dict or re-raise? Original code didn't handle much.
                 # But we rely on exceptions for gathering.
                 raise e

