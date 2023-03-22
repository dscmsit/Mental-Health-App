import json
from flask import Flask, Response, request, jsonify
from scraper import fetch_req
import pymongo

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, World!'



@app.route('/api_post', methods=['POST'])
def process_json():
    data = request.get_json()
    # process the JSON data to obtain an integer value
    result = data['header'] + data['body']  # for example, add two values
    return jsonify(result=result)

@app.route("/fetch_doc")
def doctor():
    try:
        res = fetch_req("Chandigarh")
        return res
    except:
        return "not working"


try:
    mongo=pymongo.MongoClient(host="localhost",port=27017, serverSelectionTimeoutMS=1000)
    db=mongo.content
    mongo.server_info()  #triggers exception if unable to connect to the database
except:
    print("ERROR-Cannot connect to the database")

@app.route("/users",methods=["POST"])
def create_user():
    try:
        user={
            "first name":request.form["first name"], 
            "last name":request.form["last name"],
            "email":request.form['email'],
            "password_hash":request.form['password'],
            "confirm_pass":request.form['confirm password']
        }
        # user={
        #     'firstname':'saanvi',
        #     'lastname':'bhagat',
        #     'age':20
        # }
        dbResponse=db.users.insert_one(user)
        return Response(
            response=json.dumps({"message":"user registered", "id": f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)

if __name__=='__main__':
    app.run(debug=True)