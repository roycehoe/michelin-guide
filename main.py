from typing import Any

from fastapi import FastAPI

from database import MichelinGuideDb
from schemas.michelin_data import MichelinGuideDataRequest, MichelinGuideDataResponse
from schemas.parsed_michelin_website_response import ParsedMichelinWebsiteResponse
from scripts.init_data import init_michelin_guide_data

app = FastAPI()


@app.post("/", response_model=list[MichelinGuideDataResponse])
def get_michelin_data(
    michelin_request: MichelinGuideDataRequest = MichelinGuideDataRequest(),
):
    data = MichelinGuideDb().get(michelin_request)
    response = [MichelinGuideDataResponse(**i) for i in data]
    return response


if __name__ == "__main__":
    init_michelin_guide_data()
