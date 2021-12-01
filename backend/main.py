import pickle
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.pipeline import Pipeline
from typing import Dict

from starlette.requests import Request

app = FastAPI()


loaded_objects:Dict = {}

@app.on_event("startup")
def startup_event():
    loaded_objects['model'] = pickle.load(open("static/model.bin", "rb"))


# example query:
#   ?gender=Male&age=67&hypertension=1&heart_disease=1&ever_married=Yes&work_type=Private&Residence_type=Urban&avg_glucose_level=200&body_mass=90&body_height=1.7&smoking_status=smokes
@app.get("/stroke_proba")
def predict_proba(gender: str, age: float, hypertension: int, 
                    heart_disease: int, ever_married: str, work_type: str, 
                    Residence_type: str, avg_glucose_level: float, body_mass: float, 
                    body_height: float, smoking_status: str):
    brf = loaded_objects['model']
    request_dict = {
        'gender': [gender],
        'age': [age], 
        'hypertension': [hypertension], 
        'heart_disease': [heart_disease],
        'ever_married': [ever_married],
        'work_type': [work_type], 
        'Residence_type': [Residence_type], 
        'avg_glucose_level': [avg_glucose_level], 
        'body_mass': [body_mass], 
        'body_height': [body_height], 
        'smoking_status': [smoking_status]
    }
    mass = request_dict.pop('body_mass')[0]
    height = request_dict.pop('body_height')[0]
    bmi = mass / height**2
    request_dict['bmi'] = [bmi]
    data = pd.DataFrame.from_dict(request_dict)
    return {'Proba' : brf.predict_proba(data)}
    



@app.get("/")
def hello_world():
    return loaded_objects['model'].n_features_in_

origins = [
	"https://spages.mini.pw.edu.pl/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"]
)