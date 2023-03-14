from flask import Flask, request, jsonify
from scraper import fetch_req

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



if __name__ == '__main__':
    app.run()
