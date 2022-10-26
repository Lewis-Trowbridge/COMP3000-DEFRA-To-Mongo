from pyaurn import importMeta
import os

metadata = importMeta()

mongo_username = os.getenv("MONGO_DB_USER")
mongo_password = os.getenv("MONGO_DB_PASS")

if (mongo_username is None or mongo_password is None):
    raise ValueError("MONGO_DB_USER or MONGO_DB_PASS not set")
