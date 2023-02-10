from typing import Literal, Optional, Union

from pydantic import BaseModel, validator

MichelinAward = Union[
    Literal["BIB_GOURMAND", "ONE_STAR", "TWO_STARS", "THREE_STARS"], None
]

MICHELIN_AWARD_FILTER_MAP = {
    None: 0,
    "BIB_GOURMAND": 1,
    "ONE_STAR": 2,
    "TWO_STARS": 3,
    "THREE_STARS": 4,
}


class Coordinates(BaseModel):
    lat: float
    lng: float


class ParsedMichelinWebsiteResponse(BaseModel):
    coordinates: Coordinates
    area_name: Optional[str] = None
    image: str
    city: str
    country: str
    currency: str
    currency_symbol: str
    identifier: str
    main_image: str
    michelin_award: MichelinAward
    michelin_award_sort: int = 0
    name: str
    price_category: Optional[int]
    region: str
    cuisines: list[str]
    objectID: str
    description: str
    postcode: str
    address: str

    @validator("michelin_award_sort", always=True)
    def populate_michelin_award_sort(cls, v, values) -> int:
        michelin_award_name = values["michelin_award"]
        return MICHELIN_AWARD_FILTER_MAP[michelin_award_name]
