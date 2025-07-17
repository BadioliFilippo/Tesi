from pymongo import MongoClient
import json

client = MongoClient("mongodb://mongo:27017") 

db = client["SensorData"]
collection = db["Sensor"]

documents = list(collection.find({}))

file_path = "/data/exported_data.txt"

with open(file_path, "w", encoding="utf-8") as f:
    for doc in documents:
        doc.pop("_id", None)
        f.write(json.dumps(doc) + "\n")

print(f"Esportati {len(documents)} documenti in {file_path}")
