from enum import Enum
import pickle
from schemas.michelin_data import MichelinData

MICHELIN_DATA_PATH = "data.pkl"


def get_michelin_data():
    with open(MICHELIN_DATA_PATH, "rb") as f:
        return pickle.load(f)


# print(get_michelin_data()[0])


michelin_data = [MichelinData(**i).postcode for i in get_michelin_data()]
for i in michelin_data:
    if i is None:
        print("ooh no")

current_page = 1


class SortSequence(Enum):
    ASCENDING = 1
    DESCENDING = 2


class SortOrder(Enum):
    PRICE = 1
    MICHELIN_STARS = 2


# class Filter(Enum):
#     PRICE = 1
#     LOCATION = 2
#     MICHELIN_STARS = 3


URL = f"www.something.com/?p={current_page}&ss={SortSequence.ASCENDING}&so={SortOrder.PRICE}"
