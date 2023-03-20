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

if __name__ == '__main__':
    app.run(debug=True) 


# def read_csv(file_path):
#     with open(file_path, 'r') as file:
#         reader = csv.DictReader(file)
#         return [dict(row) for row in reader]

# def write_csv(file_path, data):
#     with open(file_path, 'a', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=data.keys())
#         writer.writerow(data)

# @app.route('/api/register', methods=['POST'])
# def register():
#     data = request.json
#     if not data:
#         return jsonify({"error": "Invalid request."}), 400
#     if 'username' not in data or 'email' not in data or 'password' not in data or 'confirm_password' not in data:
#         return jsonify({"error": "All fields are required."}), 400
#     users = read_csv('path/to/csv/file.csv')
#     if any(user['username'] == data['username'] for user in users):
#         return jsonify({"error": "Username already exists. Login instead"}), 409
#     if data['password'] != data['confirm_password']:
#         return jsonify({"error": "Passwords do not match."}), 400
#     new_user = {'username': data['username'], 'email': data['email'], 'password': data['password']}
#     write_csv('path/to/csv/file.csv', new_user)
#     return jsonify(new_user), 201


# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.json
#     if not data:
#         return jsonify({"error": "Invalid request."}), 400
#     if 'username' not in data and 'email' not in data:
#         return jsonify({"error": "Username or email is required."}), 400
#     if 'password' not in data:
#         return jsonify({"error": "Password is required."}), 400
#     users = read_csv('path/to/csv/file.csv')
#     if 'username' in data:
#         user = next((user for user in users if user['username'] == data['username']), None)
#     elif 'email' in data:
#         user = next((user for user in users if user['email'] == data['email']), None)
#     if not user:
#         return jsonify({"error": "Invalid username or email."}), 401
#     if user['password'] != data['password']:
#         return jsonify({"error": "Invalid password."}), 401
#     return jsonify(user), 200
