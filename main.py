#@ DEPENDENCIES:
from fastapi import FastAPI                                                  # Importing FastAPI class from fastapi module
import uvicorn                                                               # Importing ASGI server to run app
import pydantic                                                              # Pydantic for data validation

#@ APP INITIALIZATION: 
app = FastAPI()                                                              # Instantiation of FastAPI class and stored in a variable

#@ ROUTES: 
@app.get("/")                                                                # Root endpoint
def home():                                                                  # Function to handle root get request
    return{'message': "Welcome to my app webpage."}                          # Reutrn JSON response

@app.get("/Navigation")                                                      # Get endpoint for navigation
def nav():                                                                   # Function to handle get request
    return{"message": "Search what do you want"}                             # Return JSON Response  
 
