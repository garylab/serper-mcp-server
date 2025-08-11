import os
import ssl
from typing import Dict, Any
import certifi
import aiohttp
from pydantic import BaseModel
from .enums import SerperTools
from .schemas import WebpageRequest

SERPER_API_KEY = str.strip(os.getenv("SERPER_API_KEY", ""))
AIOHTTP_TIMEOUT = int(os.getenv("AIOHTTP_TIMEOUT", "15"))


async def google(tool: SerperTools, request: BaseModel) -> Dict[str, Any]:
    uri_path = tool.value.split("_")[-1]
    url = f"https://google.serper.dev/{uri_path}"
    return await fetch_json(url, request)


async def scape(request: WebpageRequest) -> Dict[str, Any]:
    url = "https://scrape.serper.dev"
    return await fetch_json(url, request)


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
            response.raise_for_status()
            return await response.json()
