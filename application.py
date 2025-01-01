from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import pickle

## import ridge regressor, and standar scaler
model = pickle.load(open('models/ridge.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))


application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata", methods =['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        input_data = pd.DataFrame([{
            'Temperature': Temperature,
            'RH': RH,
            'Ws': Ws,
            'Rain': Rain,
            'FFMC': FFMC,
            'DMC': DMC,
            'ISI': ISI,
            'Classes': Classes,
            'Region': Region
        }])

        new_data_scaled = scaler.transform(input_data)
        result = model.predict(new_data_scaled)
        print(result)
        #result = new_data_scaled

        return render_template('home.html', results = result[0])

    else : 
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")

