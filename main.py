from enum import Enum
import pickle
from database import SessionLocal
from schemas.michelin_data import MichelinData
import crud, models, schemas
from database import SessionLocal, engine

# MICHELIN_DATA_PATH = "data.pkl"


# def get_michelin_data():
#     with open(MICHELIN_DATA_PATH, "rb") as f:
#         return pickle.load(f)


# # print(get_michelin_data()[0])


# michelin_data = [MichelinData(**i).area_name for i in get_michelin_data()]
# print(set(michelin_data))

# current_page = 1


# class SortSequence(Enum):
#     ASCENDING = 1
#     DESCENDING = 2


# class SortOrder(Enum):
#     PRICE = 1
#     MICHELIN_STARS = 2


# # class Filter(Enum):
# #     PRICE = 1
# #     LOCATION = 2
# #     MICHELIN_STARS = 3


# URL = f"www.something.com/?p={current_page}&ss={SortSequence.ASCENDING}&so={SortOrder.PRICE}"

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


import pickle
from crud import create_michelin_guide_data
from database import SessionLocal

from scripts.michelin_guide_request import get_michelin_guide_request_data
from scripts.michelin_guide_data import get_parsed_michelin_data


michelin_guide_request_data = get_michelin_guide_request_data()
parsed_michelin_guide_data = [
    get_parsed_michelin_data(michelin_data).dict()
    for michelin_data in michelin_guide_request_data
]
[
    create_michelin_guide_data(SessionLocal(), data)
    for data in parsed_michelin_guide_data
]
