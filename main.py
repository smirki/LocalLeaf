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
    logemail = request.form['logemail']
    logpass = request.form['logpass']
        
      
    user = info.find_one({'email': logemail, 'password': logpass})
    if user:
        return render_template('dash/main-dash.html')
    else:
           
        return render_template('index.html')

       

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