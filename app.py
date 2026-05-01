from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
db = client["devopsdb"]
collection = db["users"]

@app.route('/')
def home():
    return "DevOps Project Running 🚀"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "User added"})

@app.route('/users')
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)