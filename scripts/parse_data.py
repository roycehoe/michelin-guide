from typing import Optional

from schemas.michelin_website_response import Cuisine, MichelinWebsiteResponse
from schemas.parsed_michelin_website_response import (
    Coordinates,
    ParsedMichelinWebsiteResponse,
)


def _get_cuisines(cuisines: list[Cuisine]) -> list[str]:
    return [cuisine.label for cuisine in cuisines]


def _get_price_category(data: MichelinWebsiteResponse) -> Optional[int]:
    try:
        return int(data.price_category.code[-1])
    except AttributeError:
        return None


def get_parsed_michelin_data(
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
