from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://dscmsitdelhi:0Laf2FB1Fv15ohir@cluster0.x3ezfa1.mongodb.net/?retryWrites=true&w=majority"

mongo_client = MongoClient(
    "mongodb+srv://dscmsitdelhi:0Laf2FB1Fv15ohir@cluster0.x3ezfa1.mongodb.net/?retryWrites=true&w=majority")
db = mongo_client.content


# mongodb_client = PyMongo(app)
# db = mongodb_client.content


from application import main