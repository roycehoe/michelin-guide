from pydantic import BaseModel
from typing import Optional, Literal, Union

MichelinAward = Union[
    Literal["BIB_GOURMAND", "ONE_STAR", "TWO_STARS", "THREE_STARS"], None
]


class Coordinates(BaseModel):
    lat: float
    lng: float


class MichelinData(BaseModel):
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
    name: str
    price_category: Optional[int]
    region: str
    cuisines: list[str]
    objectID: str
    description: str
    postcode: str
    address: str

    class Config:
        orm_mode = True
