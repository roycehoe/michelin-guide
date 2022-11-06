import pickle

from pydantic import BaseModel
from schemas.michelin_guide_response import MichelinGuideResponse
from scripts.michelin_guide_request import get_michelin_guide_request_data
from scripts.michelin_guide_response import get_michelin_guide_response_data


data = get_michelin_guide_request_data()
response = [get_michelin_guide_response_data(i).dict() for i in data]
with open('data.pkl', 'wb') as f:
    pickle.dump(response, f)