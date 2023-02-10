from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Geoloc(BaseModel):
    lat: float
    lng: float


class City(BaseModel):
    name: str
    slug: str
    exonyms: List


class Country(BaseModel):
    name: str
    slug: str
    exonyms: List[str]
    code: str
    cname: str


class MainImage(BaseModel):
    copyright: str
    identifier: str
    order: int
    topic: str
    url: str
    source: Any


class PriceCategory(BaseModel):
    code: str
    label: str
    slug: str


class Region(BaseModel):
    name: str
    slug: str
    exonyms: List


class Cuisine(BaseModel):
    code: str
    label: str
    slug: str


class MainDesc(BaseModel):
    value: str = ""
    matchLevel: str = ""


class SnippetResult(BaseModel):
    main_desc: MainDesc = MainDesc()


class Lat(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class Lng(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class _Geoloc1(BaseModel):
    lat: Lat
    lng: Lng


class AreaName(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class Name(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class City1(BaseModel):
    name: Name


class Name1(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class Exonym(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class Country1(BaseModel):
    name: Name1
    exonyms: List[Exonym]


class Name2(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class Postcode(BaseModel):
    value: str = ""
    matchLevel: str = ""
    matchedWords: List = []


class Name3(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class Region1(BaseModel):
    name: Name3


class Street(BaseModel):
    value: str = ""
    matchLevel: str = ""
    matchedWords: List = ""


class Label(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class Cuisine1(BaseModel):
    label: Label


class CityName(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class CountryName(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class CuisineType(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class RegionName(BaseModel):
    value: str
    matchLevel: str
    matchedWords: List


class HighlightResult(BaseModel):
    _geoloc: _Geoloc1 = None
    area_name: AreaName = None
    city: City1 = None
    country: Country1 = None
    name: Name2 = None
    postcode: Postcode = Postcode()
    region: Region1 = None
    street: Street = Street()
    cuisines: List[Cuisine1] = []
    city_name: CityName = None
    country_name: CountryName = None
    cuisine_type: CuisineType = None
    region_name: RegionName = None


class MichelinWebsiteResponse(BaseModel):
    geoloc: Optional[Geoloc] = Field(default=None, alias="_geoloc")
    area_name: Optional[str] = None
    image: str
    chef: Optional[Any] = None
    city: City
    country: Country
    currency: str
    currency_symbol: str
    good_menu: Optional[int] = None
    green_star: Optional[Any] = None
    identifier: str
    main_image: MainImage
    michelin_award: Optional[Any] = None
    name: str
    new_table: Optional[int] = None
    offers: Optional[int] = None
    offers_size: Optional[int] = None
    online_booking: Optional[int] = None
    price_category: Optional[PriceCategory] = None
    region: Region
    site_name: Optional[str] = None
    site_slug: Optional[str] = None
    slug: Optional[str] = None
    take_away: Optional[int] = None
    cuisines: Optional[List[Cuisine]] = None
    url: Optional[str] = None
    other_urls: Optional[List[str]] = None
    objectID: str
    snippet_result: SnippetResult = Field(
        default=SnippetResult(), alias="_snippetResult"
    )
    highlight_result: HighlightResult = Field(
        default=HighlightResult(), alias="_highlightResult"
    )
