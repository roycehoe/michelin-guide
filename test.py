from database import SessionLocal
from crud import get_michelin_guide_data


db = SessionLocal()
test = get_michelin_guide_data(db)
print(test)
