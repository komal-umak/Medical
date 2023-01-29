
from flask import Flask,jsonify,render_template,request
from project_app.utilis import MedicalInsurance
import json
import pickle
# import config

app = Flask(__name__)

#######################################################################################################
########################################Base API ######################################################
#######################################################################################################

@app.route('/')
def home():
    print("Welcome to Medical Insurance Model")
    return render_template("index.html")

#######################################################################################################
########################################Model API ######################################################
#######################################################################################################

@app.route('/pred',methods = ['POST'])
def get_pred():
    print("*"*10,"Initializing","*"*10)
    
    age = eval(request.form['age'])
    sex = request.form['sex']
    bmi = eval(request.form['bmi'])
    children = eval(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']
    
    print(f"AGE >>{age},Sex >>{sex},BMI >> {bmi}, Children >> {children},Smoker >> {smoker}, Region >> {region}")
          
    ob = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charge = ob.get_predication()
    print(charge)
    return render_template("after.html",predicted_charge=charge)
   
        




if __name__ == "__main__":
    app.run(debug=True)