from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["shiksha_mitra"]

def create_mongo_entry(data):
    result = db.teachers.insert_one(data)
    return result.inserted_id