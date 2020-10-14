import os
import redis
import pymongo

session = redis.Redis(host=os.environ.get("REDIS_HOST", "127.0.0.1"), port=os.environ.get("REDIS_PORT", 6379), db=0)
mongo_client = pymongo.MongoClient(os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017/"))
database = mongo_client["example_dataset"]
db_data = database["data"]
