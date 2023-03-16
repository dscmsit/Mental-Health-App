from flask import Flask, request, jsonify
from scraper import fetch_req
import csv

app = Flask(__name__)


@app.route("/api")
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


@app.route("/login")
def login():
    data = request.get_json()
    if users[data["email"]]:
        if users[data["email"]] == data["pass"]:
            return "Successfull"
        else:
            return "wrong password"
    else:
        return "user doesn't exist"
    

def update_data(username, email, password):
    fieldnames = ["username", "password", "email"]

    # open the CSV file in write mode
    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # write the header row with fieldnames
        writer.writeheader()

        # write each dictionary as a row in the CSV
        for row in users:
            writer.writerow(row)


users = []
with open('backend/data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        d={}
        d["username"] = row[0]
        d["password"] = row[1]
        d["email"] = row[2]
        users.append(d)

print(users)

app.run()