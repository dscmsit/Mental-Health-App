from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__, template_folder='templates')

@app.route("/")

@app.route("/Heart")

def cancer():
    return render_template("form.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).astype(np.float16)
    to_predict[0]=to_predict[0]/100
    to_predict=to_predict[np.newaxis,:]
    if(size==14):
        # loaded_model = joblib.load(r'C:\\Users\\Armaan\\Downloads\\GDSC\\Model (1).pkl')
        directory = os.getcwd()
        loaded_model=tf.keras.models.load_model(directory+'\\model.h5')
        result = loaded_model.predict(to_predict)
    return result[0][0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==14):
            result = ValuePredictor(to_predict_list,14)
    
    if(result>0.8):
        prediction =" We feel sorry to inform you that you are prone to Coronary Heart Disease. You are suffering from serious symptoms. Please consult your doctor immediately for proper medication and healthy diet."
    else:
        prediction =" Wohooo!!! You are not suffering from any Coronary Heart Disease. Stay Healthy :)"
    return(render_template("result.html", prediction_text=prediction))       

if __name__ == "__main__":
    app.run(debug=True)
