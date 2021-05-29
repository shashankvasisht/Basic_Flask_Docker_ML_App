# from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
# import flasgger
# from flasgger import Swagger    ##used to automatically generate Front End UI part.

import streamlit as st

from PIL import Image



# app = Flask(__name__)
# Swagger(app)   #Init Swagger with your App

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


# @app.route('/')    
def welcome():
    return "Welcome All"



# # # Here the docstring description is given to use it in our Frontend UI. 
# # # While writing this description, **INDENTATION SHOULD BE AS SPECIFIED BELOW** (IMPORTANT!)
# # @app.route('/predict' , methods=["Get"])        
# def predict_note_authentication():

#     """Let's Authenticate the Banks Note 
#     This is using docstrings for specifications.
#     ---
#     parameters:  
#       - name: variance
#         in: query
#         type: number
#         required: true
#       - name: skewness
#         in: query
#         type: number
#         required: true
#       - name: curtosis
#         in: query
#         type: number
#         required: true
#       - name: entropy
#         in: query
#         type: number
#         required: true
#     responses:
#         200:
#             description: The output values
        
#     """



#     variance = request.args.get('variance')
#     skewness = request.args.get('skewness')
#     curtosis = request.args.get('curtosis')
#     entropy = request.args.get('entropy')

#     prediction=classifier.predict([[variance,skewness,curtosis,entropy]])

#     return "The predicted value is {}".format(prediction)


# # This time the in: formData and type:file , 
# # name: file should be same as given in `pd.read_csv(request.files.get("file"))``

# @app.route('/predict_file', methods=["POST"])
# def predict_note_file():

#     """Let's Authenticate the Banks Note 
#     This is using docstrings for specifications.
#     ---
#     parameters:
#       - name: file
#         in: formData
#         type: file
#         required: true
      
#     responses:
#         200:
#             description: The output values
        
#     """

#     df_test = pd.read_csv(request.files.get("file"))    # to get the csv data through request --> we use request.files.get()
#     prediction = classifier.predict(df_test)
#     return "The predicted value for the csv is {}".format(list(prediction))



def predict_note_authentication(variance,skewness,curtosis,entropy):

    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """


    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("Skewness","Type Here")
    curtosis = st.text_input("Curtosis","Type Here")
    entropy = st.text_input("Entropy","Type Here")
    result=""

    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with streamlit")


# To open this app with flasgger , use 127.0.0.1:5000/apidocs/
if __name__ == '__main__':
    # app.run(host = "0.0.0.0", port = 8000)
    main()