from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__) 

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


@app.route('/')     #Decorator to make it run in flask --> '/' = root page in flask webapp
def welcome():
    return "Welcome All"

@app.route('/predict')        #Decorator to make it run in flask --> '/' = predict page in flask webapp, by default it will be a GET method
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])

    return "The predicted value is {}".format(prediction)


@app.route('/predict_file', methods=["POST"])        #Specifically mentioning POST method as all values of test file needs to be provided to the Body
def predict_note_file():

    df_test = pd.read_csv(request.files.get("file"))    # to get the csv data through request --> we use request.files.get()
    prediction = classifier.predict(df_test)
    return "The predicted value for the csv is {}".format(list(prediction))


if __name__ == '__main__':
    app.run()