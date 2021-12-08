'''

Build a predictive service based on certain features that provide a classification of whether the bike is likely to be returned or not.

Here's some examples of features in json, that you could use to test in the body of the POST request:

[
    {"Occurrence_Year": 2015, "Occurrence_DayOfMonth": 14, "Division": 22, "Report_hour": 18, "Bike_Speed": 30, "Cost_of_Bike": 1600, "Bike_Colour_RED": 1, "Bike_Colour_BLK": 0 },
    {"Occurrence_Year": 2020, "Occurrence_DayOfMonth": 5, "Division": 31, "Report_hour": 14, "Bike_Speed": 10, "Cost_of_Bike": 500, "Bike_Colour_RED": 0, "Bike_Colour_BLK": 1 }
]

'''

from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import pandas as pd
import joblib
import sys
import os


app = Flask(__name__)
# Adding cors to flask
CORS(app)

@app.route("/", methods=['GET'])
def home():
    return "COMP-306 Group Project 2 -  Group #2 - Flask API"

@app.route("/predict", methods=['GET','POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            print(query)
            from sklearn import preprocessing
            scaler = preprocessing.StandardScaler()
            # Fit your data on the scaler object
            scaled_df = scaler.fit_transform(query)
            # return to data frame
            query = pd.DataFrame(scaled_df, columns=model_columns)
            print(query)
            prediction = list(lr.predict(query))
            print({'returned': str(prediction)})
            return jsonify({'returned': str(prediction)})
            return "Toronto Bike Prediction API"
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No models are available')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 12345

    path = os.path.dirname(os.path.realpath(__file__))
    filename1 = 'data\\models\\logistic\\model_lr2.pkl'
    filename2 = 'data\\models\\logistic\\model_columns.pkl'

    # Load lr model
    lr = joblib.load(os.path.join(path, filename1)) 
    print ('Model loaded')

    # Load columns model
    model_columns = joblib.load(os.path.join(path, filename2))
    print ('Model columns loaded')
    app.run(port=port, debug=True)

