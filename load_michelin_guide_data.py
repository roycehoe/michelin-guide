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

# with open("data.pkl", "wb") as f:
#     pickle.dump(parsed_michelin_guide_data, f)
