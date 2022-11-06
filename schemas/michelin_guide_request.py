from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class _Geoloc(BaseModel):
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


class _SnippetResult(BaseModel):
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


class _HighlightResult(BaseModel):
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


class MichelinGuideRequest(BaseModel):
    _geoloc: Optional[_Geoloc] = None
    area_name: Optional[str] = None
    image: Optional[str] = None
    chef: Optional[Any] = None
    city: Optional[City] = None
    country: Optional[Country] = None
    currency: Optional[str] = None
    currency_symbol: Optional[str] = None
    good_menu: Optional[int] = None
    green_star: Optional[Any] = None
    identifier: Optional[str] = None
    main_image: Optional[MainImage] = None
    michelin_award: Optional[Any] = None
    name: Optional[str] = None
    new_table: Optional[int] = None
    offers: Optional[int] = None
    offers_size: Optional[int] = None
    online_booking: Optional[int] = None
    price_category: Optional[PriceCategory] = None
    region: Optional[Region] = None
    site_name: Optional[str] = None
    site_slug: Optional[str] = None
    slug: Optional[str] = None
    take_away: Optional[int] = None
    cuisines: Optional[List[Cuisine]] = None
    url: Optional[str] = None
    other_urls: Optional[List[str]] = None
    objectID: Optional[str] = None
    _snippetResult: Optional[_SnippetResult] = _SnippetResult()
    _highlightResult: Optional[_HighlightResult] = _HighlightResult()
