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


@app.route('/api_post', methods=['POST'])
def process_json():
    data = request.get_json()
    # process the JSON data to obtain an integer value
    result = data['header'] + data['body']  # for example, add two values
    return jsonify(result=result)


# @app.route("/")

# @app.route("/Heart")

# def cancer():
#     return render_template("form.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).astype(np.float16)
    to_predict[0] = to_predict[0]/100
    to_predict = to_predict[np.newaxis, :]
    if (size == 13):
        loaded_model = tf.keras.models.load_model('model/model3.h5')
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

    if (result > 0.7):
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

@app.route("/fetch_doc")
def doctor():
    try:
        res = fetch_req("Chandigarh")
        return res
    except:
        return "not working"


# db = client.test


# get users api
@app.route("/get_user", methods=["GET"])
def get_users():
    try:
        # print("wow")
        data = list(db.users.find())
        for d in data:
            d["_id"] = str(d["_id"])

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot read user"}),
            status=500,
            mimetype="application/json"
        )


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

        us = list(db.users.find())
        # print(us)
        for acc in us:
            print(acc["email"])
            if user["email"] == acc["email"] and user["password_rec"] == acc["password_hash"]:
                return Response(
                    response=json.dumps(
                        {"message": "User successfully logged in"}),
                    status=200,
                    mimetype="application/json"
                )
        return Response(
            response=json.dumps(
                {"message": "User does not exist, register instead"}),
            status=401,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot read user"}),
            status=500,
            mimetype="application/json"
        )


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
            "gender": data['genderName']
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
        for us in db.users.find():
            print(us['email'])
            if us['email'] == user["email"]:
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
        print(user["password_hash"])
        dbResponse = db.users.insert_one(user)
        response = Response(
            response=json.dumps(
                {"message": "user registered", "id": f"{dbResponse.inserted_id}"}),
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


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.json.get('data')
    try:
        hashed = data["password"]
        hashed = getHashed(hashed)
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"password_hash": hashed}}
        )
        return Response(
            response=json.dumps({"message": "user updated"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:

        print(ex)

        return Response(
            response=json.dumps({"message": "cannot update user"}),
            status=500,
            mimetype="application/json"
        )
