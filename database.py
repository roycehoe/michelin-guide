from typing import Union

import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection

from schemas.michelin_data import MichelinGuideRequest

# DATABASE_URL = "mongodb://localhost:27017/"
DATABASE_URL = "mongodb://localhost:27017/"
MICHELIN_GUIDE_DATABASE_NAME = "michelin_guide_database"

MONGO_DB_CLIENT = MongoClient(DATABASE_URL)

MICHELIN_GUIDE_DB = MONGO_DB_CLIENT[MICHELIN_GUIDE_DATABASE_NAME]

MICHELIN_GUIDE_COLLECTION = MICHELIN_GUIDE_DB[MICHELIN_GUIDE_DATABASE_NAME]


class MongoDBMichelinGuideCreateError(Exception):
    pass


class MongoDBMichelinGuideGetError(Exception):
    pass


class MichelinGuideDb:
    def __init__(self, collection: Collection = MICHELIN_GUIDE_COLLECTION):
        self.collection = collection

    def create(self, michelin_guide_datapoint: dict) -> ObjectId:
        if id := self.collection.insert_one(michelin_guide_datapoint).inserted_id:
            return id
        raise MongoDBMichelinGuideCreateError(
            f"Unable to create the following data in the Michelin Guide database: {michelin_guide_datapoint}"
        )

    def create_all(self, michelin_guide_data: list[dict]) -> list[ObjectId]:
        if id := self.collection.insert_many(michelin_guide_data):
            return id
        raise MongoDBMichelinGuideCreateError(
            f"Unable to create the following data in the Michelin Guide database: {michelin_guide_data}"
        )

    def get(
        self,
        search_params: MichelinGuideRequest = MichelinGuideRequest(),
    ) -> list[dict]:
        if (
            retrieved_data := self.collection.find(search_params.filter)
            .limit(search_params.limit)
            .sort(search_params.sort)
        ):
            return [data for data in retrieved_data]
        raise MongoDBMichelinGuideGetError(
            f"Unable to retrieve the following data in the Michelin Guide database with the following search params: {search_params}"
        )

    def get_distinct(self, some_arg) -> list[Union[dict, str, int]]:
        if retrieved_data := self.collection.distinct(some_arg):
            return retrieved_data
        raise MongoDBMichelinGuideGetError(
            f"Unable to retrieve the following data in the Michelin Guide database with the following search params: {some_arg}"
        )

    def update(self):
        """Not implmenented"""
        raise NotImplementedError

    def delete(self):
        """Not implmenented"""
        raise NotImplementedError
