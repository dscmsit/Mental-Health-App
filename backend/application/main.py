from application import app
from application import db
import os
from flask import Flask, Response, request, jsonify
from application.scraper import fetch_req
import numpy as np
import tensorflow as tf      # remove if not necessary
import json
import hashlib
from bson.objectid import ObjectId


@app.route("/")
def hello_world():
    return 'welcome to mental api health'

# ________________________________ ML MODEL ROUTES _____________


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).astype(np.float16)
    to_predict[0] = to_predict[0]/100
    to_predict = to_predict[np.newaxis, :]
    if (size == 13):
        loaded_model = tf.keras.models.load_model('../model/model3.h5')
        result = loaded_model.predict(to_predict)
    return result[0][0]


@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.json.get("data")
        print(to_predict_list)
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        if (len(to_predict_list) == 13):
            result = ValuePredictor(to_predict_list, 13)

    if (result > 0.5):
        prediction = {"status": "Good", "result": result*100}
    else:
        prediction = {"status": "Bad", "result": result*100}
    print(result)
    return json.dumps(prediction)


'''
{
    "data":{'Age': '20', 'Gender': '1', 'self_employed': '1', 'family_history': '1', 'work_interfere': '1', 'no_employees': '2', 'remote_work': '1', 'tech_company': '1', 'benefits': '1', 'care_options': '1', 'wellness_program': '1', 'seek_help': '1', 'anonymity': '1', 'leave': '1', 'mental_health_consequence': '1', 'coworkers': '1'}
}
'''


# _______________________________ SCRAPPING ROUTES ____________________

@app.route("/fetch_doc/<name>")
def doctor(name):
    res = fetch_req(name)
    return res
    # return "not working"


# db = client.test


# get users api
@app.route("/get_user/<id>", methods=["GET"])
def get_users(id):
    try:
        # print("wow")
        data = db.users.find_one({"_id": ObjectId(id)})
        response = Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response
    except Exception as ex:
        print(ex)
        response = Response(
            response=json.dumps({"message": "cannot read user"}),
            status=500,
            mimetype="application/json"
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response


# login api

@app.route("/login", methods=["POST"])
def login_user():
    data = request.json.get('data')
    try:
        # print("wow")
        user = {
            "email": data['email'],
            "password_rec": data["password"]
        }
        user["password_rec"] = getHashed(user["password_rec"])
        if user["email"] == "" or user["password_rec"] == "":
            return Response(
                response=json.dumps(
                    {"message": "Enter the details correctly!!"}),
                status=400,
                mimetype="application/json"
            )

        us = db.users.find_one({"email": user["email"]})
        if us:
            print(us)
            if us["password_hash"] == user["password_rec"]:
                response = Response(
                    response=json.dumps(
                        {"status": "true", "message": "User successfully logged in", "id": f'{str(us["_id"])}'}),
                    status=200,
                    mimetype="application/json"
                )
                response.headers.add('Access-Control-Allow-Origin', '*')
                response.headers.add(
                    'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
                response.headers.add(
                    'Access-Control-Allow-Headers', 'Content-Type, Authorization')
                return response
        response = Response(
            response=json.dumps(
                {"message": "User does not exist, register instead"}),
            status=401,
            mimetype="application/json"
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response
    except Exception as ex:
        print(ex)
        response = Response(
            response=json.dumps({"message": "cannot read user"}),
            status=500,
            mimetype="application/json"
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response


# function for hashing password

def getHashed(text):  # function to get hashed email/password as it is reapeatedly used
    salt = "ITSASECRET"  # salt for password security
    hashed = text + salt  # salting password
    hashed = hashlib.md5(hashed.encode())  # encrypting with md5 hash
    hashed = hashed.hexdigest()  # converting to string
    return hashed  # give hashed text back

# function for registration


# function for registration
@app.route("/register", methods=["POST"])
def create_user():
    try:
        data = request.json.get('data')
        # hashed=bcrypt.hashpw(password_h,bcrypt.gensalt())
        user = {
            "first name": data['first_name'],
            "last name": data['last_name'],
            "email": data['email'],
            "password_hash": data['password'],
            "dob": data['dob'],
            "gender": data['genderName'],
            "state": data['stateName'],
        }
        if user["password_hash"] == "" or user["first name"] == "" or user["last name"] == "" or user["email"] == "":
            response = Response(
                response=json.dumps(
                    {"message": "Enter the details correctly!!"}),
                status=400,
                mimetype="application/json"
            )
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add(
                'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
            response.headers.add(
                'Access-Control-Allow-Headers', 'Content-Type, Authorization')
            return response
        us = db.users.find_one({"email": user["email"]})
        if us:
            response = Response(
                response=json.dumps(
                    {"message": "user already exists,login instead"}),
                status=401,
                mimetype="application/json"
            )
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add(
                'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
            response.headers.add(
                'Access-Control-Allow-Headers', 'Content-Type, Authorization')
            return response
        user["password_hash"] = getHashed(user["password_hash"])
        dbResponse = db.users.insert_one(user)
        response = Response(
            response=json.dumps(
                {"status": "true", "message": "user registered", "id": f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response
    except Exception as ex:
        print(ex)
        response = Response(
            response=json.dumps({"message": "cannot create user"}),
            status=500,
            mimetype="application/json"
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response
