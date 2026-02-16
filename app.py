from fastapi import FastAPI
import pandas as pd  
import mlflow.pyfunc 
import pydantic 
from pydantic import BaseModel
from typing import Annotated,Literal


class Base_class(BaseModel):
    sepal_length:float 
    sepal_width:float
    petal_length:float
    petal_width:float


app=FastAPI()  
model = mlflow.pyfunc.load_model('runs:/3a6f785cd536466d931010c82ca86f22/iris_model') 

@app.get('/')
def home_page():
    return {'message':'welcome fastapi !..'}

@app.post('/predict')
def predict(input_data:Base_class):
    df = pd.DataFrame([[
            input_data.sepal_length,
            input_data.sepal_width,
            input_data.petal_length,
            input_data.petal_width
        ]], columns=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ])
    predictions = model.predict(df)[0]
    if predictions==0:
        return {'predictions':'setosa'}
    elif predictions==1:
        return  {'predictions':'versicolor'}
    else: 
        return  {'predictions':'virginica' }
    
    