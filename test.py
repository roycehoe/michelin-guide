from scripts.michelin_guide_request import _get_michelin_guide_response
from schemas.michelin_guide_response import MichelinGuideResponse
from pydantic import BaseModel, Field


test = _get_michelin_guide_response(0)
print(test[0])
print(MichelinGuideResponse(**test[0]).dict())
