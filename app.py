import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd


app = Flask(__name__)
# load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

#define the home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST']) #check with postman
def predict_api():
    data = request.json['data']
    print(data)
    # reshape the data
    print(np.array(list(data.values())).reshape(1,-1))
    #scaling
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0]) # Returned value is an numpy array

#make a prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    ouptut = regmodel.predict(final_input)[0]
    return render_template("home.html", prediction_text='The House price prediction is {}'.format(ouptut))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)