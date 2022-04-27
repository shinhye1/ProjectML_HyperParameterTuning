from flask import Flask, render_template, request
import jsonify
import requests
import joblib
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = joblib.load("drive/Shareddrives/major_project/data/rfGridnew_model.pkl")
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
  if request.method == 'POST':
    Year = int(request.form['Year'])
    # change as required
    Year=2021-Year
    mileage = request.form['mileage']
    engine = int(request.form['engine'])
    maxp = request.form['maxpow']
    seats = int(request.form['seats'])
    Kms_Driven=int(request.form['Kms_Driven'])

    Owner=request.form['owner_count']

    if owner_count=='First':
      owner_Fourth_Above=0	
      owner_Second=0	
      owner_First=1	
      owner_Third=0
    elif owner_count=='Second':
      owner_Fourth_Above=0	
      owner_Second=1
      owner_First=0
      owner_Third=0
    elif owner_count=='Third':
      owner_Fourth_Above=0	
      owner_Second=0	
      owner_First=0	
      owner_Third=1
    else:
      owner_Fourth_Above=1	
      owner_Second=0	
      owner_First=0	
      owner_Third=0

    Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']


    if Fuel_Type_Petrol=='Petrol':
      fuel_Diesel=0	
      fuel_LPG=0
      fuel_Petrol=1
    elif Fuel_Type_Petrol=='Diesel':
      fuel_Diesel=1	
      fuel_LPG=0
      fuel_Petrol=0
    else:
      fuel_Diesel=0	
      fuel_LPG=1
      fuel_Petrol=0

    Seller_Type_Individual=request.form['Seller_Type_Individual']
    if Seller_Type_Individual=='Individual':
      Seller_Type_Individual=1
      Seller_Type_Dealer=0
    else:
      Seller_Type_Individual=0
      Seller_Type_Dealer=1	

    manual=0
    prediction=model.predict([Kms_Driven,mileage,engine,maxp,seats,Year,fuel_Diesel,fuel_LPG,fuel_Petrol,Seller_Type_Individual,Seller_Type_Dealer,manual,owner_Fourth_Above,owner_Second,owner_First,owner_Third])
    output=round(prediction[0],2)
    if output<0:
      return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
    else:
      return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
  else:
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)