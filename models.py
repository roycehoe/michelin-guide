from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, PickleType

from database import Base


class MichelinGuideData(Base):
    __tablename__ = "michelin_guide_data"

    id = Column(Integer, primary_key=True, index=True)
    coordinates = Column(PickleType)  # TODO: Refactor to coordinates object
    area_name = Column(String)
    image = Column(String)
    city = Column(String)
    country = Column(String)
    currency = Column(String)
    currency_symbol = Column(String)
    identifier = Column(String)
    main_image = Column(String)
    michelin_award = Column(String)
    name = Column(String)
    price_category = Column(Integer)
    region = Column(String)
    cuisines = Column(PickleType)
    objectID = Column(String)
    description = Column(String)
    postcode = Column(String)
    address = Column(String)
