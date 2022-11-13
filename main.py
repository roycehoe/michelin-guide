import pickle
from enum import Enum

from schemas.michelin_data import MichelinData
from scripts.init_michelin_guide_data import init_michelin_guide_data

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

if __name__ == "__main__":
    init_michelin_guide_data()
