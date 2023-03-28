from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

mongo_client = MongoClient(
    "mongodb+srv://dscmsitdelhi:0Laf2FB1Fv15ohir@cluster0.x3ezfa1.mongodb.net/?retryWrites=true&w=majority")
db = mongo_client.content


from application import main