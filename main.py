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
        request.form["logeuser"], request.form["logemail"], request.form["logpass"], score=0
    )
    info.insert_one(user.__dict__)
    return render_template("auth/sign-up.html")


@app.route('/update-score', methods=['POST'])
def update_score():
    user_email = request.form['user_email']
    new_score = request.form['new_score']

    info.update_one({"email": user_email}, {"$set": {"score": new_score}})

    return "Score updated successfully", 200

@app.route('/update-score-page', methods=['GET'])
def update_score_page():
    user_email = request.args.get('user_email')
    return render_template('dash/update_score.html', user_email=user_email)

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


@app.route("/login", methods=["POST"])
def login():
    logemail = request.form["logemail"]
    logpass = request.form["logpass"]

    user = info.find_one({"email": logemail, "password": logpass})
    if user:
        local_stores = [
        {'name': 'Green Market', 'location': 'Durham,NC', 'description': 'A grocery store specializing in locally-sourced, organic produce and sustainable household products.', 'url': 'https://www.greenmarket.com', 'image': '/Users/Vrishank/Desktop/Hack_NC /hackstate/templates/green.jpeg'},
        {'name': 'Eco Essentials', 'location': 'Cary,NC', 'description': 'A store selling eco-friendly products, from reusable bags and water bottles to bamboo utensils and natural cleaning supplies.', 'url': 'https://www.ecoessentials.com', 'image': '/Users/Vrishank/Desktop/Hack_NC /hackstate/templates/green.jpeg'},
        {'name': 'The Refillery', 'location': 'Zebulon,NC', 'description': 'A shop focused on reducing waste by selling bulk goods like grains, spices, and soaps, encouraging customers to bring their own containers.', 'url': 'https://www.therefillery.com', 'image': '/Users/Vrishank/Desktop/Hack_NC /hackstate/templates/green.jpeg'},
        {'name': 'Sustainably Chic', 'location': 'Morrisville,NC', 'description': 'A boutique offering ethically-made, stylish clothing and accessories made from sustainable materials.', 'url': 'https://www.sustainablychic.com', 'image': '/Users/Vrishank/Desktop/Hack_NC /hackstate/templates/green.jpeg'}
        ]
        recent_transactions = [
            {'store': 'Store 1', 'amount': 50.00, 'date': '2023-04-01'},
            {'store': 'Store 2', 'amount': 25.00, 'date': '2023-03-31'},
            {'store': 'Store 3', 'amount': 10.00, 'date': '2023-03-30'},
            {'store': 'Store 1', 'amount': 75.00, 'date': '2023-03-29'},
            {'store': 'Store 2', 'amount': 20.00, 'date': '2023-03-28'}
        ]
        crypto_factors = [
            'Hold LocalLeaf coin for long-term growth',
            'Keep an eye on market trends',
            'Diversify your cryptocurrency investments',
            'Stay informed about LocalLeaf coin developments'
        ]

        crypto_tips = [
            'Use LocalLeaf coin for everyday purchases to support local businesses',
            'Set up a secure wallet to store your LocalLeaf coins',
            'Research and follow LocalLeaf coin updates and news'
        ]
        return render_template('dash/main-dash.html', user_name=user['username'], user_score=750, local_stores=local_stores, recent_transactions=recent_transactions, credit_factors=crypto_factors, tips=crypto_tips)
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
