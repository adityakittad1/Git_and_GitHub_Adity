from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from uuid import uuid4
import hashlib
import os

app = Flask(__name__)

# A working local setup needs MongoDB running or MONGODB_URI configured.
def get_collection():
    client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/"), serverSelectionTimeoutMS=1500)
    return client[os.getenv("MONGODB_DATABASE", "git_workflow")]["todo_items"]

@app.get("/")`ndef index():
    return render_template("index.html")

@app.get("/api")
def api():
    return jsonify({"project": "Git and GitHub Flask workflow", "status": "ready"})

@app.post("/submittodoitem")
def submit_todo_item():
    payload = request.get_json(silent=True) or request.form
    item_name = str(payload.get("itemName", "")).strip()
    item_description = str(payload.get("itemDescription", "")).strip()
    if not item_name or not item_description:
        return jsonify({"error": "itemName and itemDescription are required"}), 400

    item = {
        "itemId": str(payload.get("itemId", "")).strip(),
        "itemUUID": str(uuid4()),
        "itemHash": hashlib.sha256(f"{item_name}\0{item_description}".encode()).hexdigest(),
        "itemName": item_name,
        "itemDescription": item_description,
    }
    try:
        result = get_collection().insert_one(item)
        item["_id"] = str(result.inserted_id)
        return jsonify({"message": "To-do item saved", "item": item}), 201
    except PyMongoError as exc:
        return jsonify({"error": "MongoDB is unavailable", "detail": str(exc)}), 503

if __name__ == "__main__":
    app.run(debug=True)

