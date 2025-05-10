# will read the dataset from notebook then upload it to MongoDB
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# url
url = "mongodb+srv://Aman:1234r4321@cluster0.jkdgmlk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to server 
client = MongoClient(url)

# create a database name and collection name
DATABASE_NAME = "general"
COLLECTION_NAME = "sensorfault"

df = pd.read_csv("F:\Aman New\DATA ANALYTICS\SensorFaultDetection\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis = 1)

json_record=list(json.loads(df.T.to_json()).values())

type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record) # all the object has been inserted