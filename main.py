from pyaurn import importMeta
import pymongo
import urllib.parse
import os

metadata = importMeta()
metadata = metadata.rename(columns={"site_id": "_id"})
metadata = metadata.reset_index(drop=True)
metadata_records = metadata.to_dict("records")

mongo_username = os.getenv("MONGO_DB_USER")
mongo_password = os.getenv("MONGO_DB_PASS")

if (mongo_username is None or mongo_password is None):
    raise ValueError("MONGO_DB_USER or MONGO_DB_PASS not set")

client = pymongo.MongoClient(f"""mongodb+srv://{urllib.parse.quote(mongo_username)}:{urllib.parse.quote(mongo_password)}@comp3000-air-quality.ltwo0iu.mongodb.net/?retryWrites=true&w=majority""")

db = client.metadata

batch_operations = [pymongo.ReplaceOne({"_id": x.get("_id")}, x, upsert=True) for x in metadata_records]

db.metadata.bulk_write(batch_operations)