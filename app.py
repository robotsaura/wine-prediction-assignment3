#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained models
model_red = pickle.load(open('model_red.pkl', 'rb'))
model_white = pickle.load(open('model_white.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        wine_type = data.pop('wine_type', None)
        
        if wine_type == 0:
            prediction = model_red.predict(pd.DataFrame([data]))
        elif wine_type == 1:
            prediction = model_white.predict(pd.DataFrame([data]))
        else:
            return jsonify({"error": "Invalid wine_type. Use 0 for red wine and 1 for white wine."}), 400

        return jsonify(prediction[0])
    except Exception as e:
        # Print the error to the console for debugging
        print(e)
        return jsonify({"error": "Internal server error"}), 500

@app.route('/predict_form', methods=['POST'])
def predict_form():
    try:
        wine_type = int(request.form['wine_type'])
        data = {
            'fixed acidity': float(request.form['fixed_acidity']),
            'volatile acidity': float(request.form['volatile_acidity']),
            'citric acid': float(request.form['citric_acid']),
            'residual sugar': float(request.form['residual_sugar']),
            'chlorides': float(request.form['chlorides']),
            'free sulfur dioxide': float(request.form['free_sulfur_dioxide']),
            'total sulfur dioxide': float(request.form['total_sulfur_dioxide']),
            'density': float(request.form['density']),
            'pH': float(request.form['pH']),
            'sulphates': float(request.form['sulphates']),
            'alcohol': float(request.form['alcohol']),
        }
        
        if wine_type == 0:
            prediction = model_red.predict(pd.DataFrame([data]))
        elif wine_type == 1:
            prediction = model_white.predict(pd.DataFrame([data]))
        else:
            return "Invalid wine_type. Use 0 for red wine and 1 for white wine."

        return f'Predicted Wine Quality: {prediction[0]}'
    except Exception as e:
        # Print the error to the console for debugging
        print(e)
        return "Internal server error"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
