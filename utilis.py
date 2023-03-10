import pickle
import json
import numpy as np
import warnings
warnings.filterwarnings("ignore")

class MedicalInsurance():   
    
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        
    def load_model(self):
        with open("Linear_model.pkl","rb") as f:
            self.model = pickle.load(f)
                
        with open("project_data.json","r") as f:
            self.json_data = json.load(f)
                
    def get_predication(self):
        self.load_model()
        

        test_array = np.zeros(len(self.json_data["columns"]))
        
        test_array[0] = self.age
        test_array[1] = self.json_data["sex"][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data["smoker"][self.smoker]
        region_index = np.where(self.json_data["columns"] == "region_"+ self.region)
        test_array[region_index] = 1
        print("Test Array",test_array) 
        # model = self.model
        prediction = np.around(self.model.predict([test_array])[0][0],2)
        print("Medical Insurance Charges is RS.",prediction)
        return prediction
                  
            
if __name__ =="__main__": 
    print("Welcome to Medical Insurance Project")          
    # obj = MedicalInsurance()
    # obj.get_predication()
    
   
            
  

            