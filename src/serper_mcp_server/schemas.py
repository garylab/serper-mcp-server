from typing import Optional
from pydantic import BaseModel, Field

from .enums import ReviewSortBy


class BaseRequest(BaseModel):
    q: str = Field(..., description="The query to search for")
    gl: Optional[str] = Field(
        None, description="The country to search in, e.g. us, uk, ca, au, etc."
    )
    location: Optional[str] = Field(
        None, description="The location to search in, e.g. San Francisco, CA, USA"
    )
    hl: Optional[str] = Field(
        None, description="The language to search in, e.g. en, es, fr, de, etc."
    )
    page: Optional[str] = Field(
        "1",
        pattern=r"^[1-9]\d*$",
        description="The page number to return, first page is 1 (integer value as string)",
    )


class SearchRequest(BaseRequest):
    tbs: Optional[str] = Field(
        None, description="The time period to search in, e.g. d, w, m, y"
    )
    num: str = Field(
        "10",
        pattern=r"^([1-9]|[1-9]\d|100)$",
        description="The number of results to return, max is 100 (integer value as string)",
    )


class AutocorrectRequest(BaseRequest):
    autocorrect: Optional[str] = Field(
        "true",
        pattern=r"^(true|false)$",
        description="Automatically correct (boolean value as string: 'true' or 'false')",
    )


class MapsRequest(BaseModel):
    q: str = Field(..., description="The query to search for")
    ll: Optional[str] = Field(None, description="The GPS position & zoom level")
    placeId: Optional[str] = Field(None, description="The place ID to search in")
    cid: Optional[str] = Field(None, description="The CID to search in")
    gl: Optional[str] = Field(
        None, description="The country to search in, e.g. us, uk, ca, au, etc."
    )
    hl: Optional[str] = Field(
        None, description="The language to search in, e.g. en, es, fr, de, etc."
    )
    page: Optional[str] = Field(
        "1",
        pattern=r"^[1-9]\d*$",
        description="The page number to return, first page is 1 (integer value as string)",
    )


class ReviewsRequest(BaseModel):
    fid: str = Field(..., description="The FID")
    cid: Optional[str] = Field(None, description="The CID to search in")
    placeId: Optional[str] = Field(None, description="The place ID to search in")
    sortBy: Optional[str] = Field(
        "mostRelevant",
        pattern=r"^(mostRelevant|newest|highestRating|lowestRating)$",
        description="The sort order to use (enum value as string: 'mostRelevant', 'newest', 'highestRating', 'lowestRating')",
    )
    topicId: Optional[str] = Field(None, description="The topic ID to search in")
    nextPageToken: Optional[str] = Field(None, description="The next page token to use")
    gl: Optional[str] = Field(
        None, description="The country to search in, e.g. us, uk, ca, au, etc."
    )
    hl: Optional[str] = Field(
        None, description="The language to search in, e.g. en, es, fr, de, etc."
    )


class ShoppingRequest(BaseRequest):
    autocorrect: Optional[str] = Field(
        "true",
        pattern=r"^(true|false)$",
        description="Automatically correct (boolean value as string: 'true' or 'false')",
    )
    num: str = Field(
        "10",
        pattern=r"^([1-9]|[1-9]\d|100)$",
        description="The number of results to return, max is 100 (integer value as string)",
    )


class LensRequest(BaseModel):
    url: str = Field(..., description="The url to search")
    gl: Optional[str] = Field(
        None, description="The country to search in, e.g. us, uk, ca, au, etc."
    )
    hl: Optional[str] = Field(
        None, description="The language to search in, e.g. en, es, fr, de, etc."
    )


class ParentsRequest(BaseModel):
    q: str = Field(..., description="The query to search for")
    num: str = Field(
        "10",
        pattern=r"^([1-9]|[1-9]\d|100)$",
        description="The number of results to return, max is 100 (integer value as string)",
    )
    page: Optional[str] = Field(
        "1",
        pattern=r"^[1-9]\d*$",
        description="The page number to return, first page is 1 (integer value as string)",
    )


class WebpageRequest(BaseModel):
    url: str = Field(..., description="The url to scrape")
    includeMarkdown: Optional[str] = Field(
        "false",
        pattern=r"^(true|false)$",
        description="Include markdown in the response (boolean value as string: 'true' or 'false')",
    )
