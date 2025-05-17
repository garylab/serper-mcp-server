import os
import ssl
from typing import Dict, Any
import certifi
import aiohttp
from pydantic import BaseModel

from .schemas import WebpageRequest


async def google(request: BaseModel) -> Dict[str, Any]:
    url = "https://google.serper.dev/search"
    return await fetch_json(url, request)


async def scape(request: WebpageRequest) -> Dict[str, Any]:
    url = "https://scrape.serper.dev"
    return await fetch_json(url, request)


async def fetch_json(url: str, request: BaseModel) -> Dict[str, Any]:
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
