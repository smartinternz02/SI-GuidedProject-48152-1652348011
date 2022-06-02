# -*- coding: utf-8 -*-
"""
Created on Tue May 31 12:51:54 2022

@author: HP
"""

from flask import Flask, request, render_template
#import pickle
#model = pickle.load(open("model.pkl","rb"))
#model1 = pickle.load(open("model1.pkl","rb"))
import requests
app=Flask(__name__)
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "C_kKqVayySQGU1SASahc5nnFVmlogVM4Slpj5GsrXx-E"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

#response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/da14b2af-e790-4ef9-aefc-4e03647d8c04/predictions?version=2022-05-31', json=payload_scoring,
 #headers={'Authorization': 'Bearer ' + mltoken})
#print("Scoring response")
#print(response_scoring.json())
@app.route('/')
def hello():    
    return render_template('index.html')
@app.route('/prediction', methods=['GET','POST'])
def prediction():
    a=int(request.form['method'])
    print(a)
    p=int(request.form["year"])
    q=int(request.form["month"])
    r=int(request.form["day"])
    option=[[a,p,q,r]]
    print(option)
    #option = [[int(x) for x in request.form.values()]]
    #p=request.form["year"]
    if option[0][0] == 2:        
        del option[0][0]        
        x_test = option        
        print(x_test)        
        payload_scoring = {"input_data": [{"field": [["year", "month", "day"]], "values": x_test}]}
        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/121af84c-5fca-429f-b3f3-53fafcba2fde/predictions?version=2022-05-31', json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
        print("Scoring response")
        pred=response_scoring.json()
        print(pred)
        output=pred['predictions'][0]['values'][0][0]
        print(output)
    else:        
        del option[0][0]        
        x_test = option        
        print(x_test)        
        payload_scoring = {"input_data": [{"field": [["year", "month", "day"]], "values": x_test}]}
        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/da14b2af-e790-4ef9-aefc-4e03647d8c04/predictions?version=2022-05-31', json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
        print("Scoring response")
        pred=response_scoring.json()
        print(pred)
        output=pred['predictions'][0]['values'][0][0]
        print(output)
    return render_template('index.html', predic_text='The predicted price is ' + str(output))
if __name__ == "__main__":
    app.run(debug=False)