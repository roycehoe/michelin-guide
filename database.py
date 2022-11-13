from pymongo import MongoClient

DATABASE_URL = "mongodb://localhost:27017/"
MICHELIN_GUIDE_DATABASE_NAME = "michelin_guide_database"

database_client = MongoClient(DATABASE_URL)
