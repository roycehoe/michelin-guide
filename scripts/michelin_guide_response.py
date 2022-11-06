from schemas.michelin_guide_request import MichelinGuideRequest
from schemas.michelin_guide_response import MichelinGuideResponse, Coordinates

def get_michelin_guide_response_data(data: MichelinGuideRequest) -> MichelinGuideResponse:
    coordinates = Coordinates(lat=data._geoloc.lat, lng=data._geoloc.lng) if data._geoloc is not None else None

    return MichelinGuideResponse(coordinates=coordinates, area_name=data.area_name, image=data.image, city=data.city.name, country=data.country.name, currency=data.currency, currency_symbol=data.currency_symbol, identifier=data.identifier, main_image=data.main_image.url, michelin_award=data.michelin_award, name=data.name, price_category=data.price_category, region=data.region.name, cuisines=data.cuisines, objectID=data.objectID, description=data._snippetResult.main_desc.value, postcode=data._highlightResult.postcode.value, address=data._highlightResult.street.value)
