#@ DEPENDENCIES:
from fastapi import FastAPI, HTTPException                                   # Importing FastAPI class for API creation and HTTPExe for error handling 
import uvicorn                                                               # Importing ASGI server to run app
import pydantic                                                              # Pydantic for data validation
import json                                                                  # Interchange data format
#@ APP INITIALIZATION: 
app = FastAPI()                                                              # Instantiation of FastAPI class and stored in a variable

#@ DATA RETREIVAL AND IMPORTATION
def load_data():                                                             # Function for data loading
    """Load data from a json file named as patients.json"""                  
    with open('patients.json', 'r') as f:                                    # Open the file in read mode 
        data = json.load(f)                                                  # Loading data from json to python dictionary and reserving in a variable

    return data                                                              # Return the loaded data



#@ ROUTES: 
@app.get("/")                                                                # Root endpoint
def home():                                                                  # Function to handle root get request
    return{'message': "Patient Physical Information Management API."}                          # Reutrn JSON response

@app.get("/Navigation")                                                      # Get endpoint for navigation
def nav():                                                                   # Function to handle get request
    return{"message": "API"}                             # Return JSON Response  

@app.get("/view")                                                             # Get endpoint for viewing the patients data 
def view():   
                                                                    # Function for viewing data
    data = load_data()                                                        # Data saving in a variable

    return data                                                               # Returning the loaded data

@app.get("/patient/{patient_id}")                                             # GET endpoint for viewing specific patients data
def view_patient(patient_id: str):                                            
    data = load_data()                                                        # Load data from json file

    if patient_id in data:                                                    # Checking if patient id is in the data
        return data[patient_id]                                               # Return specific patient data
    raise HTTPException(status_code = 404, detail = "Patient not found" )     # If patient_id is not found in data raise HTTP 404 error






 
