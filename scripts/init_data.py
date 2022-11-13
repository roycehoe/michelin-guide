from database import MichelinGuideDb
from scripts.get_data import get_michelin_guide_request_data
from scripts.parse_data import get_parsed_michelin_data


def init_michelin_guide_data() -> None:
    michelin_guide_request_data = get_michelin_guide_request_data()
    parsed_michelin_guide_data = map(
        get_parsed_michelin_data, michelin_guide_request_data
    )
    MichelinGuideDb().create_all([data.dict() for data in parsed_michelin_guide_data])


def is_michelin_guide_data_not_loaded() -> bool:
    if MichelinGuideDb().get():
        return False
    return True
