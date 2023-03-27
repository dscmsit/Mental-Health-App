from flask import Flask, render_template, url_for, flash, redirect
# import joblib
from flask import request
import numpy as np
import json
# import tensorflow as tf

app = Flask(__name__, template_folder='templates')

@app.route("/")

@app.route("/Heart")

def cancer():
    return render_template("form.html")

# def ValuePredictor(to_predict_list, size):
#     to_predict = np.array(to_predict_list).astype(np.float16)
#     to_predict[0]=to_predict[0]/100
#     to_predict=to_predict[np.newaxis,:]
#     if(size==16):
#         # loaded_model = joblib.load(r'C:\\Users\\Armaan\\Downloads\\GDSC\\Model (1).pkl')
#         loaded_model=tf.keras.models.load_model('Model_new.h5')
#         result = loaded_model.predict(to_predict)
#     return result[0][0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        if(len(to_predict_list)==16):
            # result = ValuePredictor(to_predict_list,16)
            result = 0.5

    if(result>0.5):
        prediction = { "status" :"Good", "advice":" We feel sorry to inform you that you might have probability of suffering from mental illness. Please consult your doctor immediately for proper therapy and medication."}
    else:
        prediction ={ "status" :"Bad", "advice":" Wohooo!!! You are not suffering from any Mental illness. Stay Healthy :)"}
    print(result)
    return json.dumps(prediction)

if __name__ == "__main__":
    app.run(debug=True)
