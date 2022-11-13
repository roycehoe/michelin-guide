from scripts.michelin_guide_request import get_michelin_guide_request_data
from scripts.michelin_guide_data import get_parsed_michelin_data
from database import database_client


michelin_guide_request_data = get_michelin_guide_request_data()
parsed_michelin_guide_data = [
    get_parsed_michelin_data(michelin_data).dict()
    for michelin_data in michelin_guide_request_data
]

michelin_guide_database = database_client.michelin_guide_database
