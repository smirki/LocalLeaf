from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from hashlib import sha256
import json
from jsonschema import validate, ValidationError

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://LocalLeaf:LoGalLea88@localleaf.eqqtjs0.mongodb.net/?retryWrites=true&w=majority"

mongo = PyMongo(app)

CONNECTION_STRING = "mongodb+srv://LocalLeaf:LoGalLea88@localleaf.eqqtjs0.mongodb.net/?retryWrites=true&w=majority"
client = PyMongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = PyMongo.collection.Collection(db, 'user_collection')

# User schema
user_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["email", "password"],
}
 
# Store schema
store_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["email", "password"],
}

def validate_data(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        print(e)
        return False

# User Registration
@app.route("/user/register", methods=["POST"])
def user_register():
    db.db.collection.insert_one({"name": "John"})
    return "Connected to the data base!"
#     users = mongo.db.users
#     data = request.json
#     if validate_data(data, user_schema):
#         email = data["email"]
#         password = data["password"]
#         hashed_password = sha256(password.encode("utf-8")).hexdigest()
#         user_score = 0
#         transactions = []

#         user = {
#             "email": email,
#             "password": hashed_password,
#             "user_score": user_score,
#             "transactions": transactions,
#         }

#         result = users.insert_one(user)
#         if result.inserted_id:
#             return jsonify({"status": "success", "message": "User registered"}), 201
#         else:
#             return jsonify({"status": "failure", "message": "Registration failed"}), 500
#     else:
#         return jsonify({"status": "failure", "message": "Invalid data"}), 400

# Store Registration
@app.route("/store/register", methods=["POST"])
def store_register():
    stores = mongo.db.stores
    data = request.json
    if validate_data(data, store_schema):
        email = data["email"]
        password = data["password"]
        hashed_password = sha256(password.encode("utf-8")).hexdigest()
        sustainability_score = 0
        transactions = []

        store = {
            "email": email,
            "password": hashed_password,
            "sustainability_score": sustainability_score,
            "transactions": transactions,
        }

        result = stores.insert_one(store)
        if result.inserted_id:
            return jsonify({"status": "success", "message": "Store registered"}), 201
        else:
            return jsonify({"status": "failure", "message": "Registration failed"}), 500
    else:
        return jsonify({"status": "failure", "message": "Invalid data"}), 400

# User Login
@app.route("/user/login", methods=["POST"])
def user_login():
    users = mongo.db.users
    email = request.json["email"]
    password = request.json["password"]
    hashed_password = sha256(password.encode("utf-8")).hexdigest()
    user = users.find_one({"email": email, "password": hashed_password})
    if user:
        return jsonify({"status": "success", "message": "Login successful"}), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid email or password"}), 401
    
# Store Login
@app.route("/store/login", methods=["POST"])
def store_login():
    stores = mongo.db.stores
    email = request.json["email"]
    password = request.json["password"]
    hashed_password = sha256(password.encode("utf-8")).hexdigest()
    store = stores.find_one({"email": email, "password": hashed_password})
    if store:
        return jsonify({"status": "success", "message": "Login successful"}), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid email or password"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)