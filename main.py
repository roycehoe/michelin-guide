from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import MichelinGuideDb
from schemas.michelin_data import (
    MichelinGuideKey,
    MichelinGuideRequest,
    MichelinGuideResponse,
)

app = FastAPI()
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/", response_model=list[MichelinGuideResponse])
def get_michelin_data(
    michelin_request: MichelinGuideRequest = MichelinGuideRequest(),
):
    michelin_guide_data = MichelinGuideDb().get(michelin_request)
    return [MichelinGuideResponse(**data) for data in michelin_guide_data]


@app.get("/{metadata_name}", response_model=Any)
def get_michelin_metadata(metadata_name: MichelinGuideKey):
    """Returns all unique values for the specified key"""
    return MichelinGuideDb().get_distinct(metadata_name)
