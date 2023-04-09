from flask import Flask, request, jsonify,render_template, request

# from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from hashlib import sha256
import json
from jsonschema import validate, ValidationError
from models.user import User
from models.company import Company

client = pymongo.MongoClient('mongodb+srv://LocalLeaf:LoGalLea88@localleaf.eqqtjs0.mongodb.net/?retryWrites=true&w=majority')
db = client.LocalLeaf
info = db.auth


app = Flask(__name__)





@app.route('/register-client', methods=['POST'])
def register_client():
    user = User(request.form['logeuser'],request.form['logemail'],request.form['logpass'])
    info.insert_one(user.__dict__)
    return render_template('auth/sign-up.html')
 
@app.route('/register-company', methods=['POST'])
def register_company():
    company = Company(request.form['company_name'],request.form['location'],request.form['website'],request.form['about'])
    info.insert_one(company.__dict__)
    return render_template('auth/sign-up.html')
   
    
    return render_template('auth/sign-up.html')

@app.route('/find', methods=['GET'])
def is_registered():
    if info.find_one({ "username": "alanka" }).count() > 0:
        return "200"
    return "-1"

@app.route('/login', methods=['POST'])
def login():
    logemail = "n"
    logpass = "majnju@gmail.com"
        
        # Query the MongoDB collection to check for matching user account
    user = info.find_one({'email': logemail, 'password': logpass})
    if user:
        return render_template('dash/main-dash.html')
    else:
            # User account not found, show error message
        return render_template('index.html')

        # Render login form page
    


# def validate_data(data, schema):
#     try:
#         validate(instance=data, schema=schema)
#         return True
#     except ValidationError as e:
#         print(e)
#         return False

# # User Registration
# @app.route("/user/register", methods=["POST"])
# def user_register():
#     db.db.collection.insert_one({"name": "John"})
#     return "Connected to the data base!"
# #     users = mongo.db.users
# #     data = request.json
# #     if validate_data(data, user_schema):
# #         email = data["email"]
# #         password = data["password"]
# #         hashed_password = sha256(password.encode("utf-8")).hexdigest()
# #         user_score = 0
# #         transactions = []

# #         user = {
# #             "email": email,
# #             "password": hashed_password,
# #             "user_score": user_score,
# #             "transactions": transactions,
# #         }

# #         result = users.insert_one(user)
# #         if result.inserted_id:
# #             return jsonify({"status": "success", "message": "User registered"}), 201
# #         else:
# #             return jsonify({"status": "failure", "message": "Registration failed"}), 500
# #     else:
# #         return jsonify({"status": "failure", "message": "Invalid data"}), 400

# # Store Registration
# @app.route("/store/register", methods=["POST"])
# def store_register():
#     stores = mongo.db.stores
#     data = request.json
#     if validate_data(data, store_schema):
#         email = data["email"]
#         password = data["password"]
#         hashed_password = sha256(password.encode("utf-8")).hexdigest()
#         sustainability_score = 0
#         transactions = []

#         store = {
#             "email": email,
#             "password": hashed_password,
#             "sustainability_score": sustainability_score,
#             "transactions": transactions,
#         }

#         result = stores.insert_one(store)
#         if result.inserted_id:
#             return jsonify({"status": "success", "message": "Store registered"}), 201
#         else:
#             return jsonify({"status": "failure", "message": "Registration failed"}), 500
#     else:
#         return jsonify({"status": "failure", "message": "Invalid data"}), 400

# # User Login
# @app.route("/user/login", methods=["POST"])
# def user_login():
#     users = mongo.db.users
#     email = request.json["email"]
#     password = request.json["password"]
#     hashed_password = sha256(password.encode("utf-8")).hexdigest()
#     user = users.find_one({"email": email, "password": hashed_password})
#     if user:
#         return jsonify({"status": "success", "message": "Login successful"}), 200
#     else:
#         return jsonify({"status": "failure", "message": "Invalid email or password"}), 401
    
# # Store Login
# @app.route("/store/login", methods=["POST"])
# def store_login():
#     stores = mongo.db.stores
#     email = request.json["email"]
#     password = request.json["password"]
#     hashed_password = sha256(password.encode("utf-8")).hexdigest()
#     store = stores.find_one({"email": email, "password": hashed_password})
#     if store:
#         return jsonify({"status": "success", "message": "Login successful"}), 200
#     else:
#         return jsonify({"status": "failure", "message": "Invalid email or password"}), 401
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
	return render_template('auth/sign-up.html')

@app.route('/submit', methods=['POST'])
def submit():
    account_type = request.form['account-type']
    return f'Thank you for signing up as a {account_type}!'


if __name__ == "__main__":
    app.run(debug=True)