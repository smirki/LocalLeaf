from flask import Flask, request, jsonify, render_template, request

# from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from hashlib import sha256
import json
from jsonschema import validate, ValidationError
from models.user import User
from models.company import Company

client = pymongo.MongoClient(
    "mongodb+srv://LocalLeaf:LoGalLea88@localleaf.eqqtjs0.mongodb.net/?retryWrites=true&w=majority"
)
db = client.LocalLeaf
info = db.auth


app = Flask(__name__)


@app.route("/register-client", methods=["POST"])
def register_client():
    user = User(
        request.form["logeuser"], request.form["logemail"], request.form["logpass"]
    )
    info.insert_one(user.__dict__)
    return render_template("auth/sign-up.html")


@app.route("/register-company", methods=["POST"])
def register_company():
    company = Company(
        request.form["company_name"],
        request.form["location"],
        request.form["website"],
        request.form["about"],
    )
    info.insert_one(company.__dict__)

    return render_template('auth/sign-up.html')
   
    

    return render_template("auth/sign-up.html")




@app.route("/find", methods=["GET"])
def is_registered():
    if info.find_one({"username": "alanka"}).count() > 0:
        return "200"
    return "-1"


@app.route("/login", methods=["POST"])
def login():
    logemail = request.form["logemail"]
    logpass = request.form["logpass"]

    user = info.find_one({"email": logemail, "password": logpass})
    if user:
        local_stores = [
        {'name': 'Store 1', 'description': 'A great store!', 'url': 'https://www.store1.com', 'image': 'https://www.example.com/store1.jpg'},
        {'name': 'Store 2', 'description': 'Another great store!', 'url': 'https://www.store2.com', 'image': 'https://www.example.com/store2.jpg'},
        {'name': 'Store 3', 'description': 'Yet another great store!', 'url': 'https://www.store3.com', 'image': 'https://www.example.com/store3.jpg'}
        ]
        recent_transactions = [
            {'store': 'Store 1', 'amount': 50.00, 'date': '2023-04-01'},
            {'store': 'Store 2', 'amount': 25.00, 'date': '2023-03-31'},
            {'store': 'Store 3', 'amount': 10.00, 'date': '2023-03-30'},
            {'store': 'Store 1', 'amount': 75.00, 'date': '2023-03-29'},
            {'store': 'Store 2', 'amount': 20.00, 'date': '2023-03-28'}
        ]
        credit_factors = [
            'Pay bills on time',
            'Keep credit utilization low',
            'Don\'t open too many new accounts',
            'Maintain a long credit history'
        ]
        tips = [
            'Use credit for everyday purchases to build credit',
            'Set up automatic payments to avoid missed payments',
            'Check your credit report regularly for errors'
        ]
        return render_template('dash/main-dash.html', local_stores=local_stores, recent_transactions=recent_transactions, credit_factors=credit_factors, tips=tips)
    else:

        return render_template("index.html")


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("auth/sign-up.html")


@app.route("/submit", methods=["POST"])
def submit():
    account_type = request.form["account-type"]
    return f"Thank you for signing up as a {account_type}!"

@app.route('/user')
def user_dash():
	return render_template('auth/user-dash.html')


if __name__ == "__main__":
    app.run(debug=True)
