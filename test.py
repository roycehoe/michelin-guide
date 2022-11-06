from scripts.michelin_guide_request import _get_michelin_guide_response
from schemas.michelin_guide_request import MichelinGuideRequest
from pydantic import BaseModel, Field

class Test(BaseModel):
    wee: str = Field(alias="_wee")


something = {"_wee": "wah"}

print(Test(**something).wee)


# test = _get_michelin_guide_response(0)
# print(test[0])
# print(MichelinGuideRequest(**test[0])._geoloc)


