from typing import Any, Literal, Union

import pymongo
from bson.objectid import ObjectId
from pydantic import BaseModel, Field

from schemas.parsed_michelin_website_response import ParsedMichelinWebsiteResponse

SortDirection = Literal[-1, 1]
MichelinGuideKey = Literal[
    "coordinates",
    "area_name",
    "image",
    "city",
    "country",
    "currency",
    "currency_symbol",
    "identifier",
    "main_image",
    "michelin_award",
    "michelin_award_sort",
    "name",
    "price_category",
    "region",
    "cuisines",
    "objectID",
    "description",
    "postcode",
    "address",
    "id",
]

DEFAULT_SORT: list[tuple[MichelinGuideKey, SortDirection]] = [
    ("michelin_award_sort", pymongo.DESCENDING)
]


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class MichelinGuideResponse(ParsedMichelinWebsiteResponse):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class MichelinGuideRequest(BaseModel):
    filter: dict[
        MichelinGuideKey, Union[int, str]
    ] = {}  # {attribute_of_MichelinGuideDataResponse: filter_param}
    sort: list[tuple[MichelinGuideKey, SortDirection]] = DEFAULT_SORT
    limit: int = 0
