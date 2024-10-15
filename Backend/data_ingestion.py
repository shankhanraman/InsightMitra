from database import data_collection

def ingest_data(data):
    data_collection.insert_one(data)
    return True
