from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017")
db = client['online_store']
products_collection = db['products']

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/catalog', methods=['GET'])
def get_catalog():
    products = list(products_collection.find({}, {"_id": 0}))
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)

