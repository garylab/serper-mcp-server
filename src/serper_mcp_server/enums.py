from enum import StrEnum


class SerperTools(StrEnum):
    GOOGLE_SEARCH = "google_search"
    GOOGLE_SEARCH_IMAGES = "google_search_images"
    GOOGLE_SEARCH_VIDEOS = "google_search_videos"
    GOOGLE_SEARCH_PLACES = "google_search_places"
    GOOGLE_SEARCH_MAPS = "google_search_maps"
    GOOGLE_SEARCH_REVIEWS = "google_search_reviews"
    GOOGLE_SEARCH_NEWS = "google_search_news"
    GOOGLE_SEARCH_SHOPPING = "google_search_shopping"
    GOOGLE_SEARCH_LENS = "google_search_lens"
    GOOGLE_SEARCH_SCHOLAR = "google_search_scholar"
    GOOGLE_SEARCH_PARENTS = "google_search_parents"
    GOOGLE_SEARCH_AUTOCOMPLETE = "google_search_autocomplete"
    WEBPAGE_SCRAPE = "webpage_scrape"

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_


class ReviewSortBy(StrEnum):
    mostRelevant = "mostRelevant"
    newest = "newest"
    highestRating = "highestRating"
    lowestRating = "lowestRating"
