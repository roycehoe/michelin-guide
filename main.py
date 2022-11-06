import json
import pickle
from schemas.michelin_guide_response import MichelinGuideResponse



MICHELIN_DATA_PATH = 'data.pkl'

# def get_michelin_data():
#     with open(MICHELIN_DATA_PATH, "rb") as f:
#         return pickle.load(f)


# michelin_data = [MichelinGuideResponse(**i).postcode for i in get_michelin_data()]
# print(michelin_data)

from scripts.michelin_guide_request import get_michelin_guide_request_data

test = get_michelin_guide_request_data()[0]
print(test.dict())