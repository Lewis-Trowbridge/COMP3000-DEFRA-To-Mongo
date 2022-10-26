from pyaurn import importMeta
import pymongo
import urllib.parse
import os

metadata = importMeta()

mongo_username = os.getenv("MONGO_DB_USER")
mongo_password = os.getenv("MONGO_DB_PASS")

if (mongo_username is None or mongo_password is None):
    raise ValueError("MONGO_DB_USER or MONGO_DB_PASS not set")

client = pymongo.MongoClient(f"""mongodb+srv://{urllib.parse.quote(mongo_username)}:{urllib.parse.quote(mongo_password)}@comp3000-air-quality.ltwo0iu.mongodb.net/?retryWrites=true&w=majority""")

db = client.metadata

db.metadata.insert_many(metadata.to_dict("records"))