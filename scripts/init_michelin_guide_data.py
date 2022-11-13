from database import MongoDBMichelinGuide
from scripts.michelin_guide_data import get_parsed_michelin_data
from scripts.michelin_guide_request import get_michelin_guide_request_data


def init_michelin_guide_data() -> None:
    michelin_guide_request_data = get_michelin_guide_request_data()
    parsed_michelin_guide_data = map(
        get_parsed_michelin_data, michelin_guide_request_data
    )
    MongoDBMichelinGuide().create_all(
        [data.dict() for data in parsed_michelin_guide_data]
    )
