from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client.business_analyst

# Collections
users_collection = db.users
data_collection = db.business_data
query_collection = db.query_history
