from fastapi import FastAPI, Depends, HTTPException
from auth import verify_token, create_token
from database import users_collection, data_collection, query_collection
from data_ingestion import ingest_data
from query_processing import process_query
from report_generation import generate_report

app = FastAPI()

# User registration and login
@app.post("/register")
def register(username: str, password: str):
    user = {"username": username, "password": password}
    users_collection.insert_one(user)
    return {"message": "User registered successfully"}

@app.post("/login")
def login(username: str, password: str):
    user = users_collection.find_one({"username": username})
    if user and user["password"] == password:
        token = create_token({"username": username})
        return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Data Ingestion
@app.post("/data/upload")
def upload_data(data: dict, token: str = Depends(verify_token)):
    ingest_data(data)
    return {"message": "Data uploaded successfully"}

# Query Processing
@app.post("/query")
def query(query: str, token: str = Depends(verify_token)):
    response = process_query(query)
    return response

# Report Generation
@app.get("/report")
def get_report(token: str = Depends(verify_token)):
    pdf_path = generate_report()
    return {"pdf_path": pdf_path}
