import numpy as np  
import pandas as pd  
import mlflow 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.datasets import load_iris 
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split 

data=load_iris()
x_train,x_test,y_train,y_test = train_test_split(data.data,data.target,test_size=0.2,random_state=42)

with mlflow.start_run():
    model=RandomForestClassifier(n_estimators=100)
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test,y_pred)

    # log_param
    mlflow.log_param('n_esitmator',100)

    #  log_metrics 
    mlflow.log_metric('accuracy',accuracy*100) 

    #  log model 
    mlflow.sklearn.log_model(model,'iris_model')