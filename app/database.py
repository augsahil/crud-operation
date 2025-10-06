from pymongo import MongoClient
from pymongo.errors import PyMongoError
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

class MongoDBClient:
    def __init__(self):
        username = os.getenv("MONGO_USERNAME")
        password = os.getenv("MONGO_PASSWORD")
        cluster_uri = os.getenv("MONGO_CLUSTER_URI")
        db_name = os.getenv("MONGO_DB_NAME", "crud")
        self.uri = f"mongodb+srv://{username}:{password}@{cluster_uri}/?retryWrites=true&w=majority&appName=Cluster0"
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print(f"Connected to MongoDB at {self.uri}, database: {self.db_name}")
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
