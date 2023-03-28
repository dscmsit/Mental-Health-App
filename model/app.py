from flask import Flask, render_template, url_for, flash, redirect
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
    if(size == 13):
        loaded_model=tf.keras.models.load_model("model_3/model3.h5")
        result = loaded_model.predict(to_predict)
    return result[0][0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==13):
            result = ValuePredictor(to_predict_list,13)
    
    if(result>0.5):
        prediction =str(result)+" We feel sorry to inform you that you are prone to Coronary Heart Disease. You are suffering from serious symptoms. Please consult your doctor immediately for proper medication and healthy diet."
    else:
        prediction =str(result)+ " Wohooo!!! You are not suffering from any Coronary Heart Disease. Stay Healthy :)"
    print(result)
    return(render_template("result.html", prediction_text=prediction))       

if __name__ == "__main__":
    app.run(debug=True)
