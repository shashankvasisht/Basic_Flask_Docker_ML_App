# Basic_Flask_Docker_Implementation
Simple Flask + Docker Implementation

This implementation is from Krish Naik's [Docker End to End Implementation](https://youtube.com/playlist?list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs) playlist - specifically video lectures 2-7.


Install the dependencies using :
```
pip install -r requirements.txt
```


## About the ML model: 
* The file **_ModelTraining.ipynb_** contains a simple Bank Note Authentication app built using sklearn's _RandomForestClassifier()_. 
* It takes in the **_BankNote_Authentication.csv_** as Input data. 
* Prediction is 0 or 1 depending on whether the Note is Authentic or not. 
* The _ModelTraining.ipynb_ file is used to dump the Random forest classifier into a pickle file - **_classifier.pkl_**.
* All this was explained in [Lecture 2](https://www.youtube.com/watch?v=ipFUANeStYE&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=2) of the Video series.


## About various Flask Applications:
* The **_flask_app.py_**'s _predict_note_authentication()_ is a simple flask GET function to accept 4 inputs required to predict from pickled classifier file.These inputs are given in the url itself. ( [Lecture 2](https://www.youtube.com/watch?v=ipFUANeStYE&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=2) )
* The _flask_app.py_'s _predict_note_file()_  is a simple flask POST function. We can use the [_POSTMAN_](https://www.postman.com/downloads/) app to post _TestFile.csv_ and check the output through the pickled model. ( [Lecture 2](https://www.youtube.com/watch?v=ipFUANeStYE&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=2) )
* The **_flask_app_copy.py_** has the same functionality as _flask_app.py_. Additionally it uses [flasgger](https://github.com/flasgger/flasgger) API to create a simple Front End UI to the Input values/File to the model.( [Lecture 3](https://www.youtube.com/watch?v=8vNBW98LbfI&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=3) ).



## About the Docker File:
* The repo contains **_Dockerfile_** which has basic docker commands (explained in [Lecture 5](https://www.youtube.com/watch?v=YWz94gBwvx4&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=5) ) to create a docker image.
* To install docker, refer to its official [Installation Guide](https://docs.docker.com/engine/install/). ([Lecture 6](https://www.youtube.com/watch?v=cDwsaQoP4Lk&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=6) )
* Build the docker image using ``` sudo docker build -t <app_name> <app_dir> ```. ([Lecture 6](https://www.youtube.com/watch?v=cDwsaQoP4Lk&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=6) )
* Run the image using ``` sudo docker run -p <host_port>:<docker_port> <app_name>```.([Lecture 6](https://www.youtube.com/watch?v=cDwsaQoP4Lk&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=6) )

## Additional:
* The repo also consists of a file named **_app_streamlit.py_** which uses [streamlit](https://streamlit.io/) library instead of flask to generate the Front End UI of the web app. ([Lecture 7](https://www.youtube.com/watch?v=5XnHlluw-Eo&list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs&index=7) )