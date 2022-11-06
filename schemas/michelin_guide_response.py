from pydantic import BaseModel
from typing import Optional, Any

class Coordinates(BaseModel):
    lat: float
    lng: float

class MichelinGuideResponse(BaseModel):
    coordinates: Optional[Coordinates] = None #previously _geoloc
    area_name: Optional[str] = None
    image: Optional[str] = None
    city: Optional[str] = None #name
    country: Optional[str] = None #name
    currency: Optional[str] = None
    currency_symbol: Optional[str] = None
    identifier: Optional[str] = None
    main_image: Optional[str] = None #url
    michelin_award: Optional[Any] = None #???
    name: Optional[str] = None
    price_category: Optional[Any] = None #Need to decipher more
    region: Optional[str] = None #name
    cuisines: Optional[list[Any]] = None #Need to decipher more
    objectID: Optional[str] = None
    description: Optional[str] = None #from _snippetResult.main_desc.value
    postcode: Optional[str] = None # from _highlightResult.postcode.value
    address: Optional[str] = None # from _highlightResult.street.value