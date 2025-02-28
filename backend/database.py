from pymongo import MongoClient
import os

# Fetch MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://TanushkaRaj:<db_password>@cluster0.ckefx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  

client = MongoClient(MONGO_URI)
db = client["survey_db"]
collection = db["responses"]