from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('Breast_Cancer_Model.pkl')

feature_names = ['radius_mean', 'area_worst', 'smoothness_worst', 'symmetry_worst']

@app.route('/')
def home():
    try:
        with open("accuracy.txt", "r") as f:
            accuracy = float(f.read())
    except:
        accuracy = None
    return render_template("index.html", feature_names=feature_names, accuracy=accuracy)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        values = [float(data[feature]) for feature in feature_names]
        input_df = pd.DataFrame([values], columns=feature_names)
        prediction = model.predict(input_df)[0]
        return jsonify({'result': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
