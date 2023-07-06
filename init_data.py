import json
from typing import Optional
from pydantic import BaseModel

import requests

from database import MichelinGuideDb
from schemas.michelin_website_response import Cuisine, MichelinWebsiteResponse
from schemas.parsed_michelin_website_response import (
    Coordinates,
    ParsedMichelinWebsiteResponse,
)

DEFAULT_URL = "https://8nvhrd7onv-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.44.0)%3B%20JS%20Helper%20(3.10.0)&x-algolia-application-id=8NVHRD7ONV&x-algolia-api-key=3222e669cf890dc73fa5f38241117ba5"


DEFAULT_HEADERS = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "1971",
    "Host": "8nvhrd7onv-dsn.algolia.net",
    "Origin": "https://guide.michelin.com",
    "Referer": "https://guide.michelin.com/sg/en/selection/singapore/restaurants/page/13?showMap=true",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26",
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}


def _get_michelin_guide_request_body(page_number: int) -> str:
    body = {
        "requests": [
            {
                "indexName": "prod-restaurants-en",
                "params": f"aroundLatLng=1.323173806860688%2C103.95738068488276&aroundLatLngViaIP=false&aroundRadius=all&attributesToRetrieve=%5B%22_geoloc%22%2C%22region%22%2C%22area_name%22%2C%22chef%22%2C%22city%22%2C%22country%22%2C%22cuisines%22%2C%22currency%22%2C%22good_menu%22%2C%22identifier%22%2C%22image%22%2C%22main_image%22%2C%22michelin_award%22%2C%22name%22%2C%22slug%22%2C%22new_table%22%2C%22offers%22%2C%22offers_size%22%2C%22online_booking%22%2C%22other_urls%22%2C%22site_slug%22%2C%22site_name%22%2C%22take_away%22%2C%22price_category%22%2C%22currency_symbol%22%2C%22url%22%2C%22green_star%22%5D&facetFilters=%5B%5B%22country.cname%3Asingapore%22%5D%5D&facets=%5B%22country.cname%22%2C%22country.slug%22%2C%22region.slug%22%2C%22city.slug%22%2C%22good_menu%22%2C%22new_table%22%2C%22take_away%22%2C%22distinction.slug%22%2C%22green_star.slug%22%2C%22offers%22%2C%22cuisines.slug%22%2C%22area_slug%22%2C%22online_booking%22%2C%22facilities.slug%22%2C%22price_category.slug%22%2C%22categories.lvl0%22%5D&filters=status%3APublished&hitsPerPage=20&maxValuesPerFacet=200&optionalFilters=sites%3Asg&page={page_number}&query=&tagFilters=",
            },
            {
                "indexName": "prod-restaurants-en",
                "params": "analytics=false&aroundLatLng=1.323173806860688%2C103.95738068488276&aroundLatLngViaIP=false&aroundRadius=all&attributesToRetrieve=%5B%22_geoloc%22%2C%22region%22%2C%22area_name%22%2C%22chef%22%2C%22city%22%2C%22country%22%2C%22cuisines%22%2C%22currency%22%2C%22good_menu%22%2C%22identifier%22%2C%22image%22%2C%22main_image%22%2C%22michelin_award%22%2C%22name%22%2C%22slug%22%2C%22new_table%22%2C%22offers%22%2C%22offers_size%22%2C%22online_booking%22%2C%22other_urls%22%2C%22site_slug%22%2C%22site_name%22%2C%22take_away%22%2C%22price_category%22%2C%22currency_symbol%22%2C%22url%22%2C%22green_star%22%5D&clickAnalytics=false&facets=country.cname&filters=status%3APublished&hitsPerPage=0&maxValuesPerFacet=200&optionalFilters=sites%3Asg&page=0&query=",
            },
        ]
    }
    return json.dumps(body)


def _get_michelin_guide_response(page_number: int) -> dict:
    response = requests.post(
        DEFAULT_URL,
        headers=DEFAULT_HEADERS,
        data=_get_michelin_guide_request_body(page_number),
    )
    data, _ = response.json()["results"]
    return data["hits"]


def _get_michelin_guide_request_data(
    request_limit: int = 1000,
) -> list[MichelinWebsiteResponse]:
    data: list[MichelinWebsiteResponse] = []
    for i in range(request_limit):
        michelin_guide_response = _get_michelin_guide_response(i)
        if not michelin_guide_response:
            return [MichelinWebsiteResponse(**datapoint) for datapoint in data]
        data = [*data, *michelin_guide_response]
    return []


def _get_cuisines(cuisines: list[Cuisine]) -> list[str]:
    return [cuisine.label for cuisine in cuisines]


def _get_price_category(data: MichelinWebsiteResponse) -> Optional[int]:
    try:
        return int(data.price_category.code[-1])
    except AttributeError:
        return None


def _get_parsed_michelin_data(
    data: MichelinWebsiteResponse,
) -> ParsedMichelinWebsiteResponse:
    coordinates = Coordinates(lat=data.geoloc.lat, lng=data.geoloc.lng)
    cuisines = _get_cuisines(data.cuisines)
    price_category = _get_price_category(data)

    return ParsedMichelinWebsiteResponse(
        coordinates=coordinates,
        area_name=data.area_name,
        image=data.image,
        city=data.city.name,
        country=data.country.name,
        currency=data.currency,
        currency_symbol=data.currency_symbol,
        identifier=data.identifier,
        main_image=data.main_image.url,
        michelin_award=data.michelin_award,
        name=data.name,
        price_category=price_category,
        region=data.region.name,
        cuisines=cuisines,
        objectID=data.objectID,
        description=data.snippet_result.main_desc.value,
        postcode=data.highlight_result.postcode.value,
        address=data.highlight_result.street.value,
    )


def init_michelin_guide_data() -> None:
    michelin_guide_request_data = _get_michelin_guide_request_data()
    parsed_michelin_guide_data = map(
        _get_parsed_michelin_data, michelin_guide_request_data
    )
    MichelinGuideDb().create_all([data.dict() for data in parsed_michelin_guide_data])


def is_michelin_guide_data_not_loaded() -> bool:
    if MichelinGuideDb().get():
        return False
    return True


if __name__ == "__main__":
    init_michelin_guide_data()