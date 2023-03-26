import json
from flask import Flask, Response, request, jsonify
from scraper import fetch_req
import pymongo
import hashlib
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'welcome to mental api health'



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

@app.route("/get_user",methods=["GET"])
def get_users():
    try:
        print("wow")
        data=list(db.users.find())
        for d in data:
            d["_id"]=str(d["_id"])

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot read user"}),
            status=500,
            mimetype="application/json"
        )



@app.route("/login",methods=["POST"])
def login_user():
    data=request.json.get('data')
    try:
        # print("wow")
        user={
            "email":data['email'],
            "password_rec": data["password"]
        }
        user["password_rec"]=getHashed(user["password_rec"])
        if user["email"]=="" or user["password_rec"]=="":
            return  Response(
                    response=json.dumps({"message":"Enter the details correctly!!"}),
                    status=400,
                    mimetype="application/json"
                )
        
        us=list(db.users.find())
        # print(us)
        for acc in us:
            print(acc["email"])
            if user["email"]==acc["email"] and user["password_rec"]==acc["password_hash"]:
                return Response(
                    response=json.dumps({"message":"User successfully logged in"}),
                    status=200,
                    mimetype="application/json"
                )
        return Response(
            response=json.dumps({"message":"User does not exist, register instead"}),
            status=401,
            mimetype="application/json"
        )
                
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot read user"}),
            status=500,
            mimetype="application/json"
        )
    


def getHashed(text): #function to get hashed email/password as it is reapeatedly used
    salt = "ITSASECRET" #salt for password security
    hashed = text + salt #salting password
    hashed = hashlib.md5(hashed.encode()) #encrypting with md5 hash
    hashed = hashed.hexdigest() #converting to string
    return hashed #give hashed text back

@app.route("/users",methods=["POST"])
def create_user():
    print("helloo")
    try:      
        data=request.json.get('data')
        
        # hashed=bcrypt.hashpw(password_h,bcrypt.gensalt())
        user={
            "first name":data['first name'], 
            "last name":data['last name'],
            "email":data['email'],
            "password_hash":data['password']
        }
        if user["password_hash"]=="" or user["first name"]=="" or user["last name"]=="" or user["email"]==""  : 
            return Response(
                response=json.dumps({"message":"Enter the details correctly!!"}),
                status=400,
                mimetype="application/json"
            )

        # user={
        #     'firstname':'saanvi',
        #     'lastname':'bhagat',
        #     'age':20
        # }
        for us in db.users.find():
            print(us['email'])
            if us['email']==user["email"]:
                return  Response(
                    response=json.dumps({"message":"user already exists,login instead"}),
                    status=401,
                    mimetype="application/json"
                )
        user["password_hash"] =getHashed(user["password_hash"])
        print(user["password_hash"])
        dbResponse=db.users.insert_one(user)
        return Response(
            response=json.dumps({"message":"user registered", "id": f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
       

    except Exception as ex:
        print(ex)
        return "chal jaa saale"


@app.route("/users/<id>",methods=["PUT"])
def update_user(id):
    data=request.json.get('data')
    try:
        hashed=data["password"]
        hashed=getHashed(hashed)
        dbResponse=db.users.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"password_hash":hashed}}
        )
        return Response(
            response=json.dumps({"message":"user updated"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot update user"}),
            status=500,
            mimetype="application/json"
        )

if __name__=='__main__':
    app.run(debug=True)





# from flask import Flask, render_template, url_for, flash, redirect
# import joblib
# from flask import request
# import numpy as np
# import tensorflow as tf

# app = Flask(__name__, template_folder='templates')

# @app.route("/")

# @app.route("/Heart")

# def cancer():
#     return render_template("form.html")

# def ValuePredictor(to_predict_list, size):
#     to_predict = np.array(to_predict_list).astype(np.float16)
#     to_predict[0]=to_predict[0]/100
#     to_predict=to_predict[np.newaxis,:]
#     if(size==16):
#         # loaded_model = joblib.load(r'C:\\Users\\Armaan\\Downloads\\GDSC\\Model (1).pkl')
#         loaded_model=tf.keras.models.load_model('Model_new.h5')
#         result = loaded_model.predict(to_predict)
#     return result[0][0]

# @app.route('/predict', methods = ["POST"])
# def predict():
#     if request.method == "POST":
#         to_predict_list = request.form.to_dict()
#         to_predict_list = list(to_predict_list.values())
#         to_predict_list = list(map(float, to_predict_list))
#         if(len(to_predict_list)==16):
#             result = ValuePredictor(to_predict_list,16)
    
#     if(result>0.5):
#         prediction =" We feel sorry to inform you that you might have probability of suffering from mental illness. Please consult your doctor immediately for proper therapy and medication."
#     else:
#         prediction =" Wohooo!!! You are not suffering from any Mental illness. Stay Healthy :)"
#     print(result)
#     return(render_template("result.html", prediction_text=prediction))       

# if __name__ == "__main__":
#     app.run(debug=True)
